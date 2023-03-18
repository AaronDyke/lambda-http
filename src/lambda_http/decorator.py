import functools
from src.lambda_http.http_responses import HttpError, HttpError500, HttpResponse


def http_response(default_response: HttpResponse, default_headers: dict = {}, is_base64_encoded: bool = False):
    """
        Decorator that takes the return of a handler function and format it as the body of the default_response HttpResponse.\n
        If a HttpError Exception is thrown this will format the error consistently.\n
        If the return of the function is an instance of HttpResponse the function returns that response.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                body = func(*args, **kwargs)
                if isinstance(body, HttpResponse):
                    body.add_headers(default_headers)
                    return body.to_dict()
                else:
                    default_response.body = body
                    default_response.add_headers(default_headers)
                    return default_response.to_dict()
            except HttpError as e:
                return HttpResponse(status_code=e.status_code, headers=default_headers, body={"message": e.message}, is_base64_encoded=is_base64_encoded).to_dict()
            except Exception as e:
                print(f'Internal Server Error: {e}')
                server_error = HttpError500()
                return HttpResponse(status_code=server_error.status_code, headers=default_headers, body=server_error.message, is_base64_encoded=is_base64_encoded).to_dict()
        return wrapper
    return decorator
