from fastapi import FastAPI, Body

from crud import database

from pydantic import BaseModel


class User(BaseModel):
    nome: str
    idade: int
    email: str | None
    telefone: str | None

class User_id(BaseModel):
    
    id: int
    

app = FastAPI()


# Disponibilização minha API


@app.get("/")
def HealthCheck():
    return {"message":"ok"}


@app.get('/users')
def get_all_users():
    users = database.find_all()
    users_list = []
    for user in users:
        users_list.append({
            "id":user[0],
            "nome":user[1],
            "idade":user[2],
            "email":user[3],
            "telefone":user[4]
            }
        )
    return users_list    


@app.get('/users/{id}')
def get_user(id):
    user = database.find_user(id)
    if user == []:
        return {"message":"not found"}
    else:
        return {
            "id":user[0][0],
            "nome":user[0][1],
            "idade":user[0][2],
            "email":user[0][3],
            "telefone":user[0][4]
            }

@app.post('/users')
def create_user(user: User):
    user = database.create_user(user)
    return  {"message":"user created", "code":"200"}
    

@app.put('/users/{id}')
def update_user(id: int, user: User):
    user = database.find_user(id)
    if user == []:
        return {"message":"not found"}
    else:
        return {
            "id":user[0][0],
            "nome":user[0][1],
            "idade":user[0][2],
            "email":user[0][3],
            "telefone":user[0][4]
            }


@app.delete('/users/{id}')
def update_user(id: int, ):
    user = database.find_user(id)
    if user == []:
        return {"message":"not found"}
    else:
        user = database.delete_user(id)
        return {"message":"sucess"} 
        

if __name__ == "__main__":
    app.run(debug=True)
