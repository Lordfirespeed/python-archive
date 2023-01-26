class BaseAPIRequestHandler:
    def __init__(self, http_handler):
        self.http_handler = http_handler
        self.server = http_handler.server

    def main(self):
        """Handles an API call."""
