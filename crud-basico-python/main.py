import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Pi9tr5xw',
    database='dbspring',
)

cursor = conexao.cursor()

query = f'INSERT INTO t_login (id, login, name, senha) VALUES ( %s, %s, %s, %s)'

dados = ('3', 'loggin', 'Py Diaz', 'admin555')
cursor.execute(query, dados)
conexao.commit()

cursor.close()
conexao.close()



# CREATE

# query = f'INSERT INTO t_login (id, login, name, senha) VALUES ( %s, %s, %s, %s)'

# dados = ('3', 'loggin', 'Py Diaz', 'admin555')
# cursor.execute(query, dados)
# conexao.commit()

# READ

# query = f'SELECT * FROM t_login'

# cursor.execute(query)
# resultado = cursor.fetchall()
# print(resultado)

# UPDATE

# query = f'UPDATE t_login SET senha = %s WHERE id = %s'

# dados = ('ademir000', 2)
# cursor.execute(query, dados)
# conexao.commit()

# DELETE

# query = f'DELETE FROM t_login WHERE id = %s'

# dados = (3,)
# cursor.execute(query, dados)
# conexao.commit()

