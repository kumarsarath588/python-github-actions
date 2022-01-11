from client.image_v3 import ImageApiClient


def main():

    pc_info = {
        "hostname": "10.44.19.140",
        "username": "admin",
        "password": "Nutanix.123",
        "port": 9440,
        "ssl_verify": False,
    }

    image_name = "Ubuntu1404"

    client = ImageApiClient(pc_info)

    image = client.get(image_name)

    print(image["status"]["name"])


if __name__ == "__main__":
    main()
