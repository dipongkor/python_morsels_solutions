class suppress():
    def __init__(self, *exceptions):
        self.exceptions = exceptions
        self.exception = None
        self.traceback = None
        # print("__init__ called")

    def __enter__(self):
        # print("__enter__ called")
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        # print ("__exit__ called")
        if exc_type:
            self.exception = exc_value
            self.traceback = exc_traceback
            # print('exc_type: {}'.format(exc_type))
            # print('exc_value: {}'.format(exc_value))
            # print('exc_traceback: {}'.format(exc_traceback))

            if exc_type in self.exceptions:
                return True  # Don't raise the exception
            else:
                # exc_type may be a child of another exception class
                for suppressed_exc in self.exceptions:
                    if issubclass(exc_type, suppressed_exc):
                        return True  # exc_type is a child class
            return False  # Raise the exception

        return True  # No exception was raised
