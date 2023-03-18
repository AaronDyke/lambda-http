import json


class HttpResponse:
    def __init__(self, status_code: int, headers: dict = {}, body={}, is_base64_encoded: bool = False) -> None:
        self.status_code = status_code
        self.headers = headers
        self.body = body
        self.is_base64_encoded = is_base64_encoded

    def to_dict(self):
        multi_value_headers = {
            k: v for k, v in self.headers.items() if isinstance(v, list)}
        return {
            "statusCode": self.status_code,
            "headers": self.headers,
            "multiValueHeaders": multi_value_headers,
            "body": self.body if self.is_base64_encoded else json.dumps(self.body),
            "isBase64Encoded": self.is_base64_encoded
        }

    def add_header(self, key, value, replace: bool = False):
        if replace == True or key not in self.headers:
            self.headers[key] = value

    def add_headers(self, headers: dict, replace: bool = False):
        for key, value in headers.items():
            self.add_header(key, value, replace=replace)


class HttpError(Exception):
    '''Base Class for Specific Http Errors'''

    def __init__(self, status_code, message):
        self.status_code = status_code
        self.message = message
        super().__init__(self.message)

    @classmethod
    def bad_request(cls, message=None):
        return HttpError400(message) if message is not None else HttpError400()

    @classmethod
    def unauthorized(cls, message=None):
        return HttpError401(message) if message is not None else HttpError401()

    @classmethod
    def payment_required(cls, message=None):
        return HttpError402(message) if message is not None else HttpError402()

    @classmethod
    def forbidden(cls, message=None):
        return HttpError403(message) if message is not None else HttpError403()

    @classmethod
    def not_found(cls, message=None):
        return HttpError404(message) if message is not None else HttpError404()

    @classmethod
    def method_not_allowed(cls, message=None):
        return HttpError405(message) if message is not None else HttpError405()

    @classmethod
    def not_acceptable(cls, message=None):
        return HttpError406(message) if message is not None else HttpError406()

    @classmethod
    def proxy_authentication_required(cls, message=None):
        return HttpError407(message) if message is not None else HttpError407()

    @classmethod
    def conflict(cls, message=None):
        return HttpError409(message) if message is not None else HttpError409()

    @classmethod
    def gone(cls, message=None):
        return HttpError410(message) if message is not None else HttpError410()

    @classmethod
    def precondition_failed(cls, message=None):
        return HttpError412(message) if message is not None else HttpError412()

    @classmethod
    def range_not_satisfiable(cls, message=None):
        return HttpError416(message) if message is not None else HttpError416()

    @classmethod
    def im_a_teapot(cls, message=None):
        return HttpError418(message) if message is not None else HttpError418()

    @classmethod
    def too_early(cls, message=None):
        return HttpError425(message) if message is not None else HttpError425()

    @classmethod
    def unavailable_for_legal_reasons(cls, message=None):
        return HttpError451(message) if message is not None else HttpError451()

    @classmethod
    def internal_server_error(cls, message=None):
        return HttpError500(message) if message is not None else HttpError500()

    @classmethod
    def not_implemented(cls, message=None):
        return HttpError501(message) if message is not None else HttpError501()

    @classmethod
    def service_unavailable(cls, message=None):
        return HttpError503(message) if message is not None else HttpError503()

    @classmethod
    def gateway_timeout(cls, message=None):
        return HttpError504(message) if message is not None else HttpError504()

    @classmethod
    def http_version_not_supported(cls, message=None):
        return HttpError505(message) if message is not None else HttpError505()

    @classmethod
    def variant_also_negotiates(cls, message=None):
        return HttpError506(message) if message is not None else HttpError506()

    @classmethod
    def insufficient_storage(cls, message=None):
        return HttpError507(message) if message is not None else HttpError507()

    @classmethod
    def loop_detected(cls, message=None):
        return HttpError508(message) if message is not None else HttpError508()

    @classmethod
    def not_extended(cls, message=None):
        return HttpError510(message) if message is not None else HttpError510()

    @classmethod
    def network_authentication_required(cls, message=None):
        return HttpError511(message) if message is not None else HttpError511()


class Http200Response(HttpResponse):
    '''200 OK'''

    def __init__(self, headers={}, body={}, is_base64_encoded=True) -> None:
        super().__init__(200, headers, body, is_base64_encoded)


class Http201Response(HttpResponse):
    '''201 Created'''

    def __init__(self, headers={}, body={}, is_base64_encoded=True) -> None:
        super().__init__(201, headers, body, is_base64_encoded)


class Http202Response(HttpResponse):
    '''202 Accepted'''

    def __init__(self, headers={}, body={}, is_base64_encoded=True) -> None:
        super().__init__(202, headers, body, is_base64_encoded)


class Http203Response(HttpResponse):
    '''203 Non-Authoritative Information'''

    def __init__(self, headers={}, body={}, is_base64_encoded=True) -> None:
        super().__init__(203, headers, body, is_base64_encoded)


class Http204Response(HttpResponse):
    '''204 No Content'''

    def __init__(self, headers={}, body={}, is_base64_encoded=True) -> None:
        super().__init__(204, headers, body, is_base64_encoded)


class Http205Response(HttpResponse):
    '''205 Reset Content'''

    def __init__(self, headers={}, body={}, is_base64_encoded=True) -> None:
        super().__init__(205, headers, body, is_base64_encoded)


class Http206Response(HttpResponse):
    '''206 Partial Content'''

    def __init__(self, headers={}, body={}, is_base64_encoded=True) -> None:
        super().__init__(206, headers, body, is_base64_encoded)


class HttpError400(HttpError):
    '''400 Bad Request'''

    def __init__(self, message='Bad Request'):
        self.message = message
        super().__init__(400, self.message)


class HttpError401(HttpError):
    '''401 Unauthorized'''

    def __init__(self, message='Unauthorized'):
        self.message = message
        super().__init__(401, self.message)


class HttpError402(HttpError):
    '''402 Payment Required'''

    def __init__(self, message='Payment Required'):
        self.message = message
        super().__init__(402, self.message)


class HttpError403(HttpError):
    '''403 Forbidden'''

    def __init__(self, message='Forbidden'):
        self.message = message
        super().__init__(403, self.message)


class HttpError404(HttpError):
    '''404 Not Found'''

    def __init__(self, message='Not Found'):
        self.message = message
        super().__init__(404, self.message)


class HttpError405(HttpError):
    '''405 Method Not Allowed'''

    def __init__(self, message='Method Not Allowed'):
        self.message = message
        super().__init__(405, self.message)


class HttpError406(HttpError):
    '''406 Not Acceptable'''

    def __init__(self, message='Not Acceptable'):
        self.message = message
        super().__init__(406, self.message)


class HttpError407(HttpError):
    '''407 Proxy Authentication Required'''

    def __init__(self, message='Proxy Authentication Required'):
        self.message = message
        super().__init__(407, self.message)


class HttpError409(HttpError):
    '''409 Conflict'''

    def __init__(self, message='Conflict'):
        self.message = message
        super().__init__(409, self.message)


class HttpError410(HttpError):
    '''410 Gone'''

    def __init__(self, message='Gone'):
        self.message = message
        super().__init__(410, self.message)


class HttpError412(HttpError):
    '''412 Precondition Failed'''

    def __init__(self, message='Precondition Failed'):
        self.message = message
        super().__init__(412, self.message)


class HttpError416(HttpError):
    '''416 Range Not Satisfiable'''

    def __init__(self, message='Range Not Satisfiable'):
        self.message = message
        super().__init__(416, self.message)


class HttpError418(HttpError):
    '''418 I'm a teapot'''

    def __init__(self, message='I\'m a teapot'):
        self.message = message
        super().__init__(418, self.message)


class HttpError425(HttpError):
    '''425 Too Early'''

    def __init__(self, message='Too Early'):
        self.message = message
        super().__init__(425, self.message)


class HttpError451(HttpError):
    '''451 Unavailable For Legal Reasons'''

    def __init__(self, message='Unavailable For Legal Reasons'):
        self.message = message
        super().__init__(451, self.message)


class HttpError500(HttpError):
    '''500 Internal Server Error'''

    def __init__(self, message='Internal Server Error'):
        self.message = message
        super().__init__(500, self.message)


class HttpError501(HttpError):
    '''501 Not Implemented'''

    def __init__(self, message='Not Implemented'):
        self.message = message
        super().__init__(501, self.message)


class HttpError502(HttpError):
    '''502 Bad Gateway'''

    def __init__(self, message='Bad Gateway'):
        self.message = message
        super().__init__(502, self.message)


class HttpError503(HttpError):
    '''503 Service Unavailable'''

    def __init__(self, message='Service Unavailable'):
        self.message = message
        super().__init__(503, self.message)


class HttpError504(HttpError):
    '''504 Gateway Timeout'''

    def __init__(self, message='Gateway Timeout'):
        self.message = message
        super().__init__(504, self.message)


class HttpError505(HttpError):
    '''505 HTTP Version Not Supported'''

    def __init__(self, message='HTTP Version Not Supported'):
        self.message = message
        super().__init__(505, self.message)


class HttpError506(HttpError):
    '''506 Variant Also Negotiates'''

    def __init__(self, message='Variant Also Negotiates'):
        self.message = message
        super().__init__(506, self.message)


class HttpError507(HttpError):
    '''507 Insufficient Storage'''

    def __init__(self, message='Insufficient Storage'):
        self.message = message
        super().__init__(507, self.message)


class HttpError508(HttpError):
    '''508 Loop Detected'''

    def __init__(self, message='Loop Detected'):
        self.message = message
        super().__init__(508, self.message)


class HttpError510(HttpError):
    '''510 Not Extended'''

    def __init__(self, message='Not Extended'):
        self.message = message
        super().__init__(510, self.message)


class HttpError511(HttpError):
    '''511 Network Authentication Required'''

    def __init__(self, message='Network Authentication Required'):
        self.message = message
        super().__init__(511, self.message)
