import requests

# interação com outra API
url = "http://127.0.0.1:8000/users"

payload = {
    "nome": "André da Silva",
    "idade": 37,
    "email": "teste@teste.com.br",
    "telefone": "(41)97894-7894"
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

