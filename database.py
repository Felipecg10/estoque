import sqlite3

# Conecta (ou cria) o banco de dados
def conectar():
    conexao = sqlite3.connect("cadastro.db")
    return conexao

# Cria tabela, se não existir
def criar_tabela():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pessoas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER,
        email TEXT,
        genero TEXT
    )
    """)
    conexao.commit()
    conexao.close()

# Adiciona nova pessoa
def adicionar_pessoa(nome, idade, email, genero):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        "INSERT INTO pessoas (nome, idade, email, genero) VALUES (?, ?, ?, ?)",
        (nome, idade, email, genero)
    )
    conexao.commit()
    conexao.close()

# Lista todas as pessoas
def listar_pessoas():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM pessoas")
    pessoas = cursor.fetchall()
    conexao.close()
    return pessoas

# Busca por nome
def buscar_pessoa(nome):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM pessoas WHERE nome LIKE ?", (f"%{nome}%",))
    resultados = cursor.fetchall()
    conexao.close()
    return resultados

# Deleta pessoa pelo ID
def deletar_pessoa(id_pessoa):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM pessoas WHERE id = ?", (id_pessoa,))
    conexao.commit()
    conexao.close()
