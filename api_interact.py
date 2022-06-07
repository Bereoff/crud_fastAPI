import requests

# interação com outra API
URL = "http://127.0.0.1:8000/users"

payload = {
    "nome":"Jose Fernandes Ferreira",
    "idade":65,
    "email":"jfferreira@email.com",
    "telefone":"15)78945-4566"
}


headers = {
'content-type' : 'application/json',
}

response = requests.post(url=URL, data=payload)

print(
    {
        "status code": response.status_code,
        "message": response.reason
    }
)

#response = requests.delete(url=URL, data=)
#
#print(response.json())



