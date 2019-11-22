from rest_utils import json_response, json_error, catch_exception
from img_borders import laplace, prewitt, roberts, sobel
from img_utils import base64_to_bw_img, img_to_base64

BorderMethods = dict(
    prewitt=prewitt,
    laplace=laplace,
    roberts=roberts,
    sobel=sobel,
)


def process_image(blob_img, method):
    img = base64_to_bw_img(blob_img)
    return BorderMethods[method](img)


@catch_exception
def image_borders(request):
    if request.headers.get('content-type') != 'application/json':
        return json_error("Use application/json")

    request_json = request.get_json(silent=True)
    if not request_json:
        return json_error("JSON is invalid")

    image = request_json['image']
    method = request_json['method']

    processed_img = process_image(image, method)
    return json_response(dict(
        image=img_to_base64(processed_img).decode('utf-8')
    ))
