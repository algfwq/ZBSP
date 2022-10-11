import pyautogui
from flask import Flask, render_template, Response, request
import io

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/pointer')
def pointer():
    x = int(float(request.args["xrate"]) * 1920)
    y = int(float(request.args["yrate"]) * 1080)
    # 执行点击操作
    pyautogui.click(x, y)
    return "success"


def gen():
    while True:
        screenShotImg = pyautogui.screenshot()
        imgByteArr = io.BytesIO()
        screenShotImg.save(imgByteArr, format='JPEG')
        imgByteArr = imgByteArr.getvalue()
        frame = imgByteArr
        yield (b'--frame\r\n Content-Type: image/jpeg\r\n\r\n' + frame)


@app.route('/video_feed')
def video_feed():
    return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(debug=True, threaded=True)
