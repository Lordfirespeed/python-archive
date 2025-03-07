from routes.add_to_media_pool import ImportAssetHandler
from routes.base_handler import BaseAPIRequestHandler
from pathlib import Path


class StaticHandler(BaseAPIRequestHandler):
    global routes

    def main(self):
        filename = routes[self.http_handler.selected_path]["template"]
        filepath = Path(f"templates/{filename}")

        if not filepath.is_file():
            self.http_handler.set_status(404)
            return

        self.http_handler.content_type = "text/html"
        with open(filepath, "r") as file:
            self.http_handler.response_content = file.read()


routes = {
    "/": {
        "template": "index.html",
        "handler": StaticHandler
    },
    "/import": {
        "handler": ImportAssetHandler
    }
}

