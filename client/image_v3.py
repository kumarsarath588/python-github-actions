import json

from client.helper import is_uuid
from client.v3 import NutanixApiClient


class ImageApiError(Exception):
    pass


class ImageApiClient(NutanixApiClient):
    def __init__(self, object):
        super().__init__(object)
        self.resource = "images"

    def list(self, filter={}):

        image_list_endpoint = "{0}/list".format(self.resource)

        response = self.request(image_list_endpoint, "POST", filter)

        return json.loads(response.content)

    def get_uuid(self, image_name):

        list_payload = {"filter": "name=={0}".format(image_name), "length": 9999}
        image_uuid = None

        images_list_json = self.list(list_payload)

        for image in images_list_json["entities"]:
            if image["status"]["name"] == image_name:
                image_uuid = image["metadata"]["uuid"]
                break

        if not image_uuid:
            raise ImageApiError("Failed to get uuid for image: {0}".format(image_name))

        return image_uuid

    def get(self, image):

        if is_uuid(image):
            uuid = image
        else:
            uuid = self.get_uuid(image)

        images_get_endpoint = "{0}/{1}".format(self.resource, uuid)

        response = self.request(images_get_endpoint, "GET", None)

        return response.json()
