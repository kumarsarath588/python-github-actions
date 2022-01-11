import json

from client.v3 import NutanixApiClient


def main():

    pc_info = {
        "hostname": "10.44.19.140",
        "username": "admin",
        "password": "Nutanix.123",
        "port": 9440,
        "ssl_verify": False,
    }

    client = NutanixApiClient(pc_info)

    vms_list_response = client.request("/vms/list", "POST", {})

    vms_list_json=json.loads(vms_list_response.content)

    print(client.headers)

    if isinstance(client, NutanixApiClient):
        print("client is of type NutanixApiClient")

    for entity in vms_list_json["entities"]:
        print(entity["status"]["name"])


if __name__ == "__main__":
    main()
