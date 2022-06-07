import requests

# interação com outra API
URL = ""

payload = {
    "nome": "",
    "idade": null,
    "email": "",
    "telefone": ""
}


headers = {
    'content-type': 'application/json',
}

response = requests.post(url=URL, data=payload)

print(
    {
        "status code": response.status_code,
        "message": response.reason
    }
)

# response = requests.delete(url=URL, data=)
#
# print(response.json())
