import json
from urllib import request, error
import os

class OpenAiRequest:
    def __init__(self):
        self.organization = os.getenv("OPENAI_ORG")
        self.token = os.getenv("OPENAI_TOKEN")
        if not self.organization:
            raise ValueError(
                "Variável de ambiente OPENAI_ORG não está definida ou está vazia."
            )
        if not self.token:
            raise ValueError(
                "Variável de ambiente OPENAI_TOKEN não está definida ou está vazia."
            )
            
    def gpt_5_nano_response(self, message):

        data = {
            "model": "gpt-5-nano",
            "input": message
        }
        payload = json.dumps(data).encode("utf-8")

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}",
            "Host": "api.openai.com",
            "Content-Length": str(len(payload))
        }

        req = request.Request(
            "https://api.openai.com/v1/responses",
            data=payload,
            headers=headers,
            method="POST"
        )
        print(req.full_url, req.headers)  # debug para checar headers

        try:
            with request.urlopen(req, timeout=100) as resp:
                body = resp.read().decode("utf-8")
                result = json.loads(body)
                #print(result)
                return result
        except error.HTTPError as e:
            print("HTTP Error:", e.code, e.reason)
            print(e.read().decode())  # corpo do erro
            raise
        except error.URLError as e:
            print("URL Error:", e.reason)
            raise
