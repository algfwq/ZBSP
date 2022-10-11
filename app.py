import socket
from io import BytesIO
from  PIL import ImageGrab
import pyautogui
from Flask import Flask, render_template, Response

app = Flask(__name__)


def screencap():
    """
    屏幕截图组装流数据
    :return:
    """
    while True:
        #img = ImageGrab.grab()
        img = pyautogui.screenshot()
        buffer = BytesIO()
        img.save(buffer, 'jpeg')
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + buffer.getvalue() + b'\r\n\r\n')


def getIp():
    """
    获取本机ip地址
    :return: str: 本机ip
    """
    ip = '127.0.0.1'
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
        s.close()
    except Exception as e:
        print(str(e)[0:0] + '获取本机ip失败 默认设置为：127.0.0.1')
    return ip


@app.route('/')
def index():
    """
    首页
    :return:
    """
    return render_template('index.html')


@app.route('/video')
def video():
    """
    截屏Api
    :return:
    """
    return Response(screencap(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    print(' ' * 14 + 'PF屏幕共享')
    print('#' * 40)
    print(' ' * 3 + f'访问地址：http://{getIp()}:7000')
    print('#' * 40)
    print('服务启动->')
    app.run(host='0.0.0.0', port=7000, processes=True)
