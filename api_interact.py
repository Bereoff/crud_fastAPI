import requests

# interação com outra API
URL = "http://127.0.0.1:8000/users"

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
