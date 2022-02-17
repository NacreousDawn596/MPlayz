import flask
from youtubesearchpython import VideosSearch
from pytube import YouTube

app = flask.Flask(__name__, template_folder="./")

@app.route("/")
def index():
    return flask.render_template("index.html")

@app.route("/search/<keyword>")
def search(keyword):
    print(keyword)
    html = """<!doctype html>
<html> 
    <head>
        <title>MPplayer</title>
        <style>
            body {
                background-image: url('https://michalsnik.github.io/aos/img/bg.jpg');
                background-repeat: no-repeat;
                background-attachment: fixed;
                background-size: 100% 100%;
            }

            .main {
                font-family: 'Sans-serif';
                font-size: 400%;
                text-align: center;
                margin: 10%;
                padding: 1% 1% 1% 1%;
                border-radius: 25px 50px;
                border-color: dimgrey;
                background-color: aliceblue;
                color: black;
                transition-duration: 0.5s;
                text-decoration: none;
            }

            .main:hover {
                font-family: 'Sans-serif';
                font-size: 450%;
                text-align: center;
                border-radius: 50px 25px;
                border-color: dimgrey;
                background-color: black;
                color: aliceblue;
                text-decoration: none;
                transition-duration: 0.5s;
            }

            .extra-links > ul > li {
                border-top-right-radius: 50px;
                color: aliceblue;
                font-family: 'Sans-serif';
                background: #903C56;
                width: 25%;
                margin-top: 5px;
                padding: 10px;
                font-size: 120%;
                transition-duration: 0.5s;
            }

            .extra-links > ul >li:hover {
                font-family: 'Arial';
                font-size: 122%;
                background: #76969D;
                height: 1%;
                width: 30%;
                transition-duration: 0.5s;
                border-bottom-right-radius: 50px;
            }

            .extra-links > ul > li > a {
                text-decoration: none;
                color: aliceblue;
                font-family: 'Sans-serif';
                font-size: 126%;
            }

            #video-link {
                text-decoration: none;
                font-family: 'Sans-serif';
                font-size: 126%;
            }

            div.container {
                display: flex;
                align-items: flex-start;
                justify-content: space-around;
                margin-top: 30px;
                padding: 21px;
            }
            
            :root {
                --omrs-color-ink-lowest-contrast: rgba(47, 60, 85, 0.18);
                --omrs-color-ink-low-contrast: rgba(60, 60, 67, 0.3);
                --omrs-color-ink-medium-contrast: rgba(19, 19, 21, 0.6);
                --omrs-color-interaction: #1e4bd1;
                --omrs-color-interaction-minus-two: rgba(73, 133, 224, 0.12);
                --omrs-color-danger: #b50706;
                --omrs-color-bg-low-contrast: #eff1f2;
                --omrs-color-ink-high-contrast: #121212;
                --omrs-color-bg-high-contrast: #ffffff;
                
            }
            
            div.omrs-input-group {
            margin-bottom: 1.5rem;
            position: relative;
            width: 20.4375rem;
            }

            .omrs-input-underlined > input,
            .omrs-input-filled > input {
                border-radius: 10px;
                background: rgba(245, 245, 245, 0.6);
                color: black;
                height: 50px;
                width: 100%;
                font-size: 20px;
            }

            .omrs-input-underlined > input:focus,
            .omrs-input-filled > input:focus {
                outline: none;
            }

            .omrs-input-underlined > .omrs-input-label,
            .omrs-input-filled > .omrs-input-label {
                position: absolute;
                top: 0.9375rem;
                left: 0.875rem;
                line-height: 147.6%;
                color: var(--omrs-color-ink-medium-contrast);
                transition: top .2s;
            }

            .omrs-input-underlined > svg,
            .omrs-input-filled > svg {
                position: absolute;
                top: 0.9375rem;
                right: 0.875rem;
                fill: var(--omrs-color-ink-medium-contrast);
            }

            .omrs-input-underlined > .omrs-input-helper,
            .omrs-input-filled > .omrs-input-helper {
                font-size: 0.9375rem;
                color: whitesmoke;
                letter-spacing: 0.0275rem;
                margin: 0.125rem 0.875rem;
            }

            .omrs-input-underlined > input:hover,
            .omrs-input-filled > input:hover {
                background: var(--omrs-color-interaction-minus-two);
                border-color: var(--omrs-color-ink-high-contrast);
                transition-duration: 0.5s;
            }

            .omrs-input-underlined > input:focus + .omrs-input-label,
            .omrs-input-underlined > input:valid + .omrs-input-label,
            .omrs-input-filled > input:focus + .omrs-input-label,
            .omrs-input-filled > input:valid + .omrs-input-label {
                top: 0;
                font-size: 0.9375rem;
                margin-bottom: 32px;;
            }

            .omrs-input-underlined:not(.omrs-input-danger) > input:focus + .omrs-input-label,
            .omrs-input-filled:not(.omrs-input-danger) > input:focus + .omrs-input-label {
                color: var(--omrs-color-interaction);
            }

            .omrs-input-underlined:not(.omrs-input-danger) > input:focus,
            .omrs-input-filled:not(.omrs-input-danger) > input:focus {
                border-color: var(--omrs-color-interaction);
            }

            .omrs-input-underlined:not(.omrs-input-danger) > input:focus ~ svg,
            .omrs-input-filled:not(.omrs-input-danger) > input:focus ~ svg {
                fill: var(--omrs-color-ink-high-contrast);
            }

            .omrs-input-underlined > input:disabled {
                background: var(--omrs-color-bg-low-contrast);
                cursor: not-allowed;
                transition-duration: 0.5s;
            }

            #show-results > div{
                border: 1rem;
                color: black;
                box-shadow: 0px 0px 2rem grey;
                width: 90%;
                margin-left: 0.7rem;
                background-color: #eff1f2;
                border-radius: 2.5rem;
                padding: 2% 2% 2% 2%;
                transition-duration: 0.09s;
            }

            #show-results > div:hover{
                border: 1rem;
                color: #eff1f2;
                box-shadow: 0px 0px 3rem grey;
                width: 92%;
                margin-left: 0.7rem;
                background-color: rgb(39, 14, 31);
                border-radius: 3rem;
                padding: 2% 2% 2% 2%;
                transition-duration: 0.09s;
            }

            #show-results > div > a > img {
                border-radius: 1rem;
            }

            .omrs-input-underlined > input:disabled + .omrs-input-label,
            .omrs-input-underlined > input:disabled ~ .omrs-input-helper{
                color: var(--omrs-color-ink-low-contrast);
                transition-duration: 0.5s;
            }

            .omrs-input-underlined > input:disabled ~ svg {
                fill: var(--omrs-color-ink-low-contrast);
                transition-duration: 0.5s;
            }

            footer {
                min-width: 100%;
                margin: none;
                height: 4rem;
                background-color: seagreen;
            }

            #result > button {
                background-color: grey;
                color: whitesmoke;  
                border-radius: 1rem 1rem 1rem 1rem;
            }

            #result > button:hover {
                background-color: whitesmoke;
                color: black;  
                border-radius: 1rem 1rem 1rem 1rem;
            }
            
        </style>
        <script>
            function daclick(url_part){
                window.location.href = `/download/${url_part}`;
            }
            window.addEventListener("load", function(event) {
                document.getElementById("research").addEventListener("keyup", function(event) {
                    if (event.keyCode === 13) {
                        keyword = document.getElementById("research").value
                        return window.location.replace(`/search/${document.getElementById("research").value.replace('?', "").replace('/', '').replace('#', '')}`)
                    }
                });
            });
        </script>
    </head>
    <body>
        <center>
            <br/><br/><br/>
            <a class="main" href='#'>MPplayz</a>
        </center>
        <br/><br/><br/>
        <center>
            <div class="container">
                <div>
                    <div class="omrs-input-group" type="text" size="30">
                        <label class="omrs-input-underlined">
                            <input required id="research">
                            <span class="omrs-input-label">Search...</span>
                            <span class="omrs-input-helper">whatever comes to your mind-</span>
                        </label>
                    </div>
                </div>
            </div>
        </center>
        <div id="show-results">"""
    html_end = """            <br/>
        </div>
        <footer style="padding-bottom: 2rem;">
            <div>
                <h1>Developers:</h1>
                <a href="https://github.com/NacreousDawn596">NacreousDawn596</a>
                <a href="https://github.com/Atreyaved">Atreyaved</a>
            </div>
        </footer>
    </body>
</html>"""
    videos = VideosSearch(keyword, limit = 10).result()['result']
    divs = []
    for item in range(len(videos)):
        link = videos[item]['link']
        img = videos[item]['thumbnails'][0]['url'].split('?')[0]
        divs.append(f"""<div id="result">
                <a href="{link}"><img src="{img}" width="20%" style="display: inline;vertical-align:middle;"/></a>
                <a id="video-link" href="{link}" style="display: inline;vertical-align:top;">{videos[item]['title']}</a>
                <br/>
                <p style="font-size: 60%;display: inline;vertical-align:middle;">{videos[item]['accessibility']['title']}</p>
                <button style="display: inline;vertical-align:bottom;float: right;" onclick="daclick('{videos[item]["id"]}');">Download</button>

            </div>
            <br/>
            <br/>""")
    di = '\n'.join([div for div in divs])
    return f"{html}\n{di}\n{html_end}"

@app.route("/download/<id>")
def download(id):
    idk = YouTube(str(f'http://youtube.com/watch?v={id}'))
    return flask.send_file(idk.streams.filter(progressive=True, file_extension='mp4').first().download(), as_attachment=True, attachment_filename=f"{idk.title}.mp4")
"""
@app.errorhandler(404)
def fferr(e):
    return flask.render_template("error.html")

@app.errorhandler(500)
def ffverr(e):
    return flask.render_template("error.html")
"""
    

if '__main__' == __name__:
    app.run()