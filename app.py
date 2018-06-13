from flask import Flask, send_file
from concurrent.futures import ThreadPoolExecutor
from utils.camera import Camera

app = Flask(__name__)
executor = ThreadPoolExecutor(1)


@app.route('/shot/<int:w>x<int:h>')
def shot(w=224, h=224):
    cam = Camera()
    cam.resolution = (w, h)
    cam.vflip, cam.hflip = True, True
    try:
        cam.capture('./test.png', resize=(w, h))
        # cam.capture('./test.png')
    finally:
        cam.close()
    return send_file('./test.png')


if __name__ == '__main__':
    app.run(port=2333)
