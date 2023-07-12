import base64
import requests
from freeMECPlatform.settings import MEC_PLATFORM_HOST, MEC_PLATFORM_PORT
import json

def gen_client_credential(client_id, secret):
    client_id = "0ulJa3GBEnsNAYUPwAxURrNyEi55Vr30VRytmavi"
    secret = "w4RzeaDLtcoENlr5MMi7r6tTEU6M2EqTlGLvPzRLnS6y0O0aJBRi6Q1R4ji33LaLqte2M4lhFgtTBgfwVGUWeJtrmtxB31QAaCons2I49PKBng24Cqw1KSOGmEP3NaWO"
    credential = "{0}:{1}".format(client_id, secret)
    return base64.b64encode(credential.encode("utf-8")).decode("utf-8")


def gen_token(client_credential):
    url = "http://" + MEC_PLATFORM_HOST + ":" + MEC_PLATFORM_PORT + "/o/token/"

    payload='grant_type=client_credentials'
    headers = {
    'Cache-Control': 'no-cache',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Authorization': 'Basic ' + client_credential,
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return (json.loads(response.text))