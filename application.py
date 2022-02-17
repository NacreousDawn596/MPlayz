import flask
from youtubesearchpython import VideosSearch
from pytube import YouTube

app = flask.Flask(__name__, template_folder="./")

@app.route("/")
def index():
    return flask.render_template("index.html")

@app.route("/search/<keyword>")
def search(keyword):
    videos = VideosSearch(keyword, limit = 10).result()['result']
    divs = []
    for item in range(len(videos)):
        divs.append(f"""<div id="result">
                <a href="{videos[item]['link']}"><img src="{videos[item]['thumbnails'][0]['url'].split('?')[0]}" width="20%" style="display: inline;vertical-align:middle;"/></a>
                <a id="video-link" href="{videos[item]['link']}" style="display: inline;vertical-align:top;">{videos[item]['title']}</a>
                <br/>
                <p style="font-size: 60%;display: inline;vertical-align:middle;">{videos[item]['accessibility']['title']}</p>
                <br/>
                <button style="display: inline;vertical-align:bottom;float: right;" onclick="daclick('{videos[item]["id"]}');">Download</button>

            </div>
            <br/>
            <br/>""")
    di = '\n'.join([div for div in divs])
    return f"{open('show.html', 'r').read().split('EOF')[0]}\n{di}\n{open('show.html', 'r').read().split('EOF')[1]}"

@app.route("/download/<id>")
def download(id):
    idk = YouTube(str(f'http://youtube.com/watch?v={id}'))
    return flask.send_file(idk.streams.filter(progressive=True, file_extension='mp4').first().download(), as_attachment=True, attachment_filename=f"{idk.title}.mp4")

@app.route("/developers/NacreousDawn596")
def show():
    return flask.send_file("code.png")

@app.errorhandler(404)
def fferr(e):
    return flask.render_template("error.html")

@app.errorhandler(500)
def ffverr(e):
    return flask.render_template("error.html")

    

if '__main__' == __name__:
    app.run()