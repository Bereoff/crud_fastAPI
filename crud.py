from config import cursor, db

class database:
      
    def create_user(user):
        try:
            cursor.execute(
                "INSERT INTO usuario (nome, idade, email, telefone) VALUES (%s, %s, %s, %s);", (user.nome, user.idade, user.email, user.telefone))
            db.commit()
        except Exception as e:
            print(e)

    def find_all():
        cursor.execute("SELECT * FROM usuario ORDER BY id;")
        return cursor.fetchall()


    def find_user(id):
        cursor.execute(f"SELECT * FROM usuario WHERE id={id};")
        return cursor.fetchall()


    def update_user(id, user):
        try:
            cursor.execute(
                "UPDATE usuario SET nome=%s, idade=%s, email=%s, telefone=%s WHERE id=%s;", (user.nome, user.idade, user.email, user.telefone, id))
            db.commit()
        except Exception as e:
            print(e)

    def delete_user(id):
        try:
            cursor.execute(f"DELETE FROM usuario WHERE id={id}")
            db.commit()
        except Exception as e:
            print(e)