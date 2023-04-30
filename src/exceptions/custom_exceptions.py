class CustomException(Exception):
    pass


def handle_custom_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except CustomException as e:
            print(f"There was a custom exception of type: {str(e)}")

    return wrapper
