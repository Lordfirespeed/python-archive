import sys

from routes.base_handler import BaseAPIRequestHandler
import logging
from pathlib import Path
from http.client import responses
import xml.etree.ElementTree as XMLElementTree


class ImportAssetHandler(BaseAPIRequestHandler):
    def get_clip_path(self):

        clip_object = XMLElementTree.fromstring(self.http_handler.request_data)  # raises XMLElementTree.ParseError

        path_element = clip_object.find("Path")
        if path_element is None:
            raise NameError

        path_string = path_element.text
        filepath = Path(path_string)  # raises TypeError if filepath is None

        if not filepath.is_file():
            raise OSError

        return filepath

    def add_filepath_to_media_pool(self, filepath):
        resolve_api = self.server.resolve_api
        project_manager = resolve_api.GetProjectManager()
        current_project = project_manager.GetCurrentProject()
        media_pool = current_project.GetMediaPool()
        new_media_pool_items = media_pool.ImportMedia([filepath])
        logging.debug(f"New Media Pool Items: {new_media_pool_items}")

    def main(self):
        if self.http_handler.command != "POST":
            self.http_handler.set_status(405, "Use HTTP POST.")
            return

        try:
            filepath = self.get_clip_path()
        except (NameError, XMLElementTree.ParseError):
            self.http_handler.set_status(400, "Invalid XML Provided.")
            return
        except (OSError, TypeError):
            self.http_handler.set_status(400, "Invalid file path.")
            return

        try:
            self.add_filepath_to_media_pool(str(filepath))
        except Exception as error:
            logging.exception(error)

