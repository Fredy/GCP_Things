from flask import jsonify


def json_response(data, code=200):
    return jsonify(data), code


def json_error(msg, code=400):
    return json_response(dict(error=msg), code)


def catch_exception(func):
    def internal_func(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError as e:
            return json_error(f'JSON missing a {e} property.')

    return internal_func
