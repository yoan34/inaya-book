from functools import wraps
import time


def retry_api_call(max_attempts=10, delay=1):
    def decorator(api_call_func):
        @wraps(api_call_func)
        def wrapper(self, *args, **kwargs):
            print("hello")
            attempts = 0
            success = False
            response = ("", 0)
            while attempts < max_attempts and not success:
                try:
                    response = api_call_func(self, *args, **kwargs)
                    success = True  # L'appel API a réussi, sortir de la boucle while
                except Exception as e:
                    attempts += 1
                    time.sleep(delay)

            return response
        return wrapper
    return decorator
