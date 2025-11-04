import streamlit as st
from database import criar_tabela, adicionar_pessoa, listar_pessoas, buscar_pessoa, deletar_pessoa

# Cria tabela ao iniciar
criar_tabela()

# Configuração da página
st.set_page_config(page_title="Cadastro de Pessoas", page_icon="🧾", layout="centered")
st.title("🧾 Sistema de Cadastro de Pessoas")

menu = ["Cadastrar", "Listar", "Buscar", "Excluir"]
opcao = st.sidebar.selectbox("Menu", menu)

# --- Página de Cadastro ---
if opcao == "Cadastrar":
    st.subheader("Adicionar nova pessoa")

    nome = st.text_input("Nome:")
    idade = st.number_input("Idade:", min_value=0, max_value=120, step=1)
    email = st.text_input("Email:")
    genero = st.selectbox("Gênero:", ["Masculino", "Feminino", "Outro"])

    if st.button("Salvar"):
        if nome.strip() == "":
            st.warning("⚠️ O nome é obrigatório!")
        else:
            adicionar_pessoa(nome, idade, email, genero)
            st.success(f"✅ Pessoa '{nome}' cadastrada com sucesso!")

# --- Página de Listagem ---
elif opcao == "Listar":
    st.subheader("Lista de pessoas cadastradas")
    pessoas = listar_pessoas()

    if len(pessoas) == 0:
        st.info("Nenhuma pessoa cadastrada ainda.")
    else:
        st.dataframe(
            {
                "ID": [p[0] for p in pessoas],
                "Nome": [p[1] for p in pessoas],
                "Idade": [p[2] for p in pessoas],
                "Email": [p[3] for p in pessoas],
                "Gênero": [p[4] for p in pessoas],
            }
        )

# --- Página de Busca ---
elif opcao == "Buscar":
    st.subheader("Buscar pessoa por nome")
    nome_busca = st.text_input("Digite o nome ou parte do nome:")

    if st.button("Buscar"):
        resultados = buscar_pessoa(nome_busca)
        if len(resultados) == 0:
            st.warning("❌ Nenhum resultado encontrado.")
        else:
            st.success(f"{len(resultados)} pessoa(s) encontrada(s):")
            for r in resultados:
                st.write(f"**ID:** {r[0]} | **Nome:** {r[1]} | **Idade:** {r[2]} | **Email:** {r[3]} | **Gênero:** {r[4]}")

# --- Página de Exclusão ---
elif opcao == "Excluir":
    st.subheader("Excluir pessoa")
    pessoas = listar_pessoas()
    if len(pessoas) == 0:
        st.info("Nenhuma pessoa cadastrada.")
    else:
        opcoes = {f"{p[1]} (ID: {p[0]})": p[0] for p in pessoas}
        escolha = st.selectbox("Selecione a pessoa:", list(opcoes.keys()))
        id_pessoa = opcoes[escolha]

        if st.button("Excluir"):
            deletar_pessoa(id_pessoa)
            st.success("✅ Pessoa excluída com sucesso!")
