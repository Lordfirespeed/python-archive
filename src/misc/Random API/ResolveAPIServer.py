from routes.main import routes
from http.server import BaseHTTPRequestHandler, HTTPServer
from socketserver import BaseServer
from http.client import responses
from threading import Thread
from textwrap import indent
import logging
import re
import os


class ResolveAPIServer(HTTPServer):
    cors_policy_origins = ["http://localhost:63342"]
    cors_policy_headers = {"Access-Control-Allow-Credentials": "true",
                           "Access-Control-Allow-Methods": "GET, POST",
                           "Access-Control-Allow-Headers": "Content-Type",
                           "Access-Control-Max-Age": "600"}

    def __init__(self, server_address, handler, resolve_api):
        self.resolve_api = resolve_api
        HTTPServer.__init__(self, server_address, handler)


class ResolveRequestHandler(BaseHTTPRequestHandler):
    def __init__(self, request, client_address, server):
        self.request_data = None

        self.status = 200
        self.content_type = "text/plain"
        self.response_content = responses[self.status]

        self.selected_path = None
        BaseHTTPRequestHandler.__init__(self, request, client_address, server)

    def read_POST_data(self):
        content_length = int(self.headers['Content-Length'])  # <--- Gets the size of data
        post_data = self.rfile.read(content_length)  # <--- Gets the data itself
        self.request_data = post_data.decode("utf-8")

    def log_this_request(self):
        indented_headers = indent(self.headers.as_string().strip(), 4 * ' ')
        log_message = f"{self.command} request,\nPath: {self.path}\nHeaders: \n{indented_headers}\n"

        if self.command == "POST":
            log_message += f"Data: {self.request_data}\n"

        logging.info(log_message)

    def set_status(self, status, explanation=None):
        self.status = status
        if status is not 200:
            self.content_type = "text/plain"
            self.response_content = responses[status]

            if explanation is not None:
                self.response_content += f" - {explanation}"

    def apply_cors_policy(self):
        if self.headers["Origin"] not in self.server.cors_policy_origins:
            return

        self.send_header("Access-Control-Allow-Origin", self.headers["Origin"])
        for policy_keyword, policy_value in self.server.cors_policy_headers.items():
            self.send_header(policy_keyword, policy_value)

    def send_response_headers(self):
        self.send_response(self.status)
        self.apply_cors_policy()
        self.send_header("Content-type", self.content_type)
        self.end_headers()

    def send_full_response(self):
        self.send_response_headers()
        self.wfile.write(bytes(self.response_content, "UTF-8"))

    def send_blank_response(self):
        self.content_type = "text/plain"
        self.send_response_headers()

    def call_route(self):
        path, path_extension = os.path.splitext(self.path)

        handler = None

        if path_extension is "" or path_extension is ".html":
            for try_route_name in routes.keys():
                if re.fullmatch(try_route_name, path):
                    self.selected_path = try_route_name
                    break

            if self.selected_path is None:
                self.set_status(404)
            else:
                handler = routes[self.selected_path]["handler"]
        elif path_extension is ".py":
            self.set_status(405)
        else:
            handler = None

        if handler is not None:
            handler(self).main()

        self.send_full_response()

    def do_GET(self):
        self.log_this_request()
        self.call_route()

    def do_POST(self):
        self.read_POST_data()
        self.do_GET()

    def do_OPTIONS(self):
        self.log_this_request()
        self.send_response_headers()

    def log_message(self, _format, *args):
        """Log an arbitrary message.

        This is used by all other logging functions.  Override
        it if you have specific logging wishes.

        This has been overridden with a method that does no logging, as
        there is an error when scripts are run from DaVinci Resolve that means
        attempting to print to stdout/stderr will cause a thread to hang.
        """

        pass


class ServerThread(Thread):
    def __init__(self, resolve_api, server_class=ResolveAPIServer, handler_class=ResolveRequestHandler, host="localhost", port=8080):
        self.server_address = (host, port)
        self.server = server_class(self.server_address, handler_class, resolve_api)
        Thread.__init__(self, name="catdv_resolve_listener")

    def run(self):
        logging.info("Starting httpd...\n")
        self.server.serve_forever()

    def stop(self):
        logging.info("Stopping httpd...\n")
        self.server.shutdown()


if __name__ == "__main__":
    import time

    logging.basicConfig(level=logging.DEBUG)

    ServerThreadInstance = ServerThread(None, host="127.0.0.1", port=8089)
    ServerThreadInstance.start()

    try:
        time.sleep(30)
    except KeyboardInterrupt:
        pass
    finally:
        ServerThreadInstance.stop()
