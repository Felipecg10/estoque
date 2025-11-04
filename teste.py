import sqlite3

# --- Criar o banco e a tabela ---
def criar_banco():
    conexao = sqlite3.connect("cadastro.db")
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


# --- Função para adicionar uma pessoa ---
def adicionar_pessoa():
    nome = input("Nome: ").strip()
    idade = input("Idade: ").strip()
    email = input("Email: ").strip()
    genero = input("Gênero (M/F/Outro): ").strip()

    # Conecta ao banco e insere
    conexao = sqlite3.connect("cadastro.db")
    cursor = conexao.cursor()
    cursor.execute(
        "INSERT INTO pessoas (nome, idade, email, genero) VALUES (?, ?, ?, ?)",
        (nome, idade, email, genero)
    )
    conexao.commit()
    conexao.close()
    print(f"\n✅ Pessoa '{nome}' cadastrada com sucesso!\n")


# --- Função para listar todas as pessoas ---
def listar_pessoas():
    conexao = sqlite3.connect("cadastro.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM pessoas")
    pessoas = cursor.fetchall()
    conexao.close()

    if len(pessoas) == 0:
        print("\n⚠️ Nenhum registro encontrado.\n")
        return

    print("\n=== Lista de Pessoas Cadastradas ===")
    for p in pessoas:
        print(f"ID: {p[0]} | Nome: {p[1]} | Idade: {p[2]} | Email: {p[3]} | Gênero: {p[4]}")
    print()


# --- Função para buscar pessoas por nome ---
def buscar_por_nome():
    nome_busca = input("Digite o nome (ou parte do nome): ").strip()
    conexao = sqlite3.connect("cadastro.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM pessoas WHERE nome LIKE ?", (f"%{nome_busca}%",))
    resultados = cursor.fetchall()
    conexao.close()

    if len(resultados) == 0:
        print("\n❌ Nenhuma pessoa encontrada com esse nome.\n")
        return

    print("\n=== Resultado da busca ===")
    for r in resultados:
        print(f"ID: {r[0]} | Nome: {r[1]} | Idade: {r[2]} | Email: {r[3]} | Gênero: {r[4]}")
    print()


# --- Programa principal ---
def main():
    criar_banco()

    while True:
        print("=== MENU CADASTRO ===")
        print("1 - Adicionar pessoa")
        print("2 - Listar pessoas")
        print("3 - Buscar por nome")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_pessoa()
        elif opcao == "2":
            listar_pessoas()
        elif opcao == "3":
            buscar_por_nome()
        elif opcao == "0":
            print("\n👋 Saindo do sistema. Até logo!")
            break
        else:
            print("\n⚠️ Opção inválida, tente novamente.\n")


if __name__ == "__main__":
    main()
