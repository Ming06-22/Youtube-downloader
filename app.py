from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
from pytube import YouTube
from flask import send_file

app = Flask(__name__)

error = False

@app.route("/")
def main():
    global error
    if error:
        return render_template("main.html", error=True)
    else:
        return render_template("main.html", error=False)

@app.route("/download", methods=["post"])
def download():
    global error
    try:
        webUrl = request.form.get("webUrl")
        yt = YouTube(webUrl)
        file = yt.streams.first().download()
        error = False
        return send_file(file.split("\\")[-1], as_attachment=True)
    except:
        error = True
        return redirect("/")

if __name__ == "__main__":
    app.run()