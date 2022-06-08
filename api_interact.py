import requests

# interação com outra API
url = ""

payload = {
    "nome": "",
    "idade": null,
    "email": "",
    "telefone": ""
}


headers = {
    'content-type': 'application/json',
}

#response = requests.post(url=URL, data=payload)


def criar_usuario(url, payload):
    response = requests.post(url=url, json=payload)
    print(
    {
        "status code": response.status_code,
        "message": response.reason
    }
)
    return response

# response = requests.delete(url=URL, data=)
#
# print(response.json())

criar_usuario(url, payload)

