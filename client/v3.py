import json

import requests
import requests.exceptions


class NutanixApiError(Exception):
    pass


class NutanixApiClient:
    def __init__(self, object):
        hostname = object["hostname"]
        username = object["username"]
        password = object["password"]
        port = object["port"]

        self.base_url = "https://{0}:{1}/api/nutanix/v3".format(hostname, port)
        self.auth = (username, password)
        self.headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }
        self.ssl_verify = object["ssl_verify"]
        self.session = requests.session()

        if not self.ssl_verify:
            from urllib3.exceptions import InsecureRequestWarning

            requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

    def request(self, endpoint, method, payload, timeout=10):
        """
            Api call request to the api server
        params:
            api_endpoint (required): api endpoint url for the request
            method (required): rest call method
            payload (optional): post call payload
        """

        url = "{0}/{1}".format(self.base_url, endpoint)

        try:
            response = self.session.request(
                url=url,
                method=method,
                auth=self.auth,
                data=json.dumps(payload),
                headers=self.headers,
                verify=self.ssl_verify,
                timeout=timeout,
            )
        except requests.exceptions.RequestException as err:
            raise NutanixApiError("Request Failed {0}".format(err))
        except requests.exceptions.ConnectTimeout as err:
            raise NutanixApiError("Request Timedout {0}".format(err))

        if response.ok:
            return response
        else:
            raise NutanixApiError(
                "Failed api call response_code:{0} content:{1}".format(
                    response.status_code, response.content
                )
            )
