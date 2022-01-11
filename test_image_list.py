import json

from client.image_v3 import ImageApiClient
from client.v3 import NutanixApiClient


def main():

    pc_info = {
        "hostname": "10.44.19.140",
        "username": "admin",
        "password": "Nutanix.123",
        "port": 9440,
        "ssl_verify": False,
    }

    """
    We can get the list of images by accessing NutanixApiClient directly
    or by access ImageApiClient
    """
    # By accessing NutanixApiClient
    nutanix_client = NutanixApiClient(pc_info)

    images_list_response = nutanix_client.request("/images/list", "POST", {})

    images_list_json = json.loads(images_list_response.content)

    for entity in images_list_json["entities"]:
        print(entity["status"]["name"])

    # By accessing ImageApiClient
    image_client = ImageApiClient(pc_info)

    if isinstance(image_client, ImageApiClient):
        print("You are accessing resource: {0}".format(image_client.resource))

    images_list_json = image_client.list()

    for entity in images_list_json["entities"]:
        print(entity["status"]["name"])


if __name__ == "__main__":
    main()
