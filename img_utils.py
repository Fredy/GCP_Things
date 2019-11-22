from base64 import b64decode, b64encode

import numpy as np
import cv2


def base64_to_bw_img(blob):
    """Convert base64 to black and white image."""
    data = b64decode(blob)
    data = np.frombuffer(data, np.uint8)
    img = cv2.imdecode(data, 0)
    return img

def img_to_base64(img):
    retval, buffer = cv2.imencode('.png', img)
    return b64encode(buffer)
