from flask import request
from flask import url_for
from flask import redirect
from flask import send_file
from flask import render_template
from generator.app import app
from generator.utils import qr_img_gen
from urllib.parse import quote

@app.route("/")
def index():
    result = request.args.get('result')
    if result == "True":
        return render_template('download.html')
    else:
        return render_template('index.html', show_result=result)


@app.route("/create_qrcode", methods=["POST", "GET"])
def start_qr():
    if request.method == "POST":
        url = request.form["qr_link"]
        print(f"url is {url}")
        url = quote(url, safe='')
        print(f"safe quote url is {url}")
        return redirect(url_for("generate_qr", qr_url=url))
    else:
        return redirect(url_for("index", result="Error"))


@app.route("/generate_qr_for/<string:qr_url>")
def generate_qr(qr_url):
    try:
        qr_img_gen(qr_url)
        return redirect(url_for("index", result="True"))
    except Exception as e:
        print(e)
        return redirect(url_for("index", result="Error"))


@app.route("/download")
def download_qr():
    qr_img = "static/temporary/qrcode.png"
    return send_file(qr_img, as_attachment=True)
