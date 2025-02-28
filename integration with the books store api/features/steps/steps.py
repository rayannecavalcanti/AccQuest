import random
import string
from behave import given, when, then
from src.api import create_user, generate_token, get_all_books, rent_books, get_user_details

# Contexto para armazenar dados entre os steps
context = {}

def generate_random_string(length=5):
    """Gera uma string aleatória com o comprimento especificado."""
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

@given('Eu crio um usuário com nome "{username}" e senha "{password}"')
def step_create_user(context, username, password):
    """
    Cria um usuário na API DemoQA com o nome e senha fornecidos.
    """
    # Adiciona um sufixo aleatório ao nome de usuário para garantir que seja único
    unique_username = f"{username}_{generate_random_string()}"
    try:
        user = create_user(unique_username, password)
        context.user_id = user["userID"]
        context.username = unique_username
        context.password = password
        print(f"Usuário criado com ID: {context.user_id}")
    except Exception as e:
        print(f"Erro ao criar usuário: {e}")
        raise e

@given('Eu gero um token de acesso')
def step_generate_token(context):
    """
    Gera um token de acesso para o usuário criado.
    """
    try:
        token_response = generate_token(context.username, context.password)
        context.token = token_response["token"]
        print(f"Token gerado: {context.token}")
    except Exception as e:
        print(f"Erro ao gerar token: {e}")
        raise e

@given('Eu listo os livros disponíveis')
def step_list_books(context):
    """
    Lista os livros disponíveis na API DemoQA.
    """
    try:
        context.books = get_all_books()
        print("Livros disponíveis listados.")
    except Exception as e:
        print(f"Erro ao listar livros: {e}")
        raise e

@when('Eu escolho os livros com ISBNs "{isbns}" para alugar')
def step_rent_books(context, isbns):
    """
    Aluga os livros com os ISBNs fornecidos.
    """
    try:
        isbn_list = isbns.split(" e ")
        rent_response = rent_books(context.user_id, context.token, isbn_list)
        context.rent_response = rent_response
        print(f"Livros alugados: {rent_response}")
    except Exception as e:
        print(f"Erro ao alugar livros: {e}")
        raise e

@then('Os livros devem ser alugados com sucesso')
def step_check_rent_success(context):
    """
    Verifica se os livros foram alugados com sucesso.
    """
    try:
        assert context.rent_response, "Falha ao alugar livros."
        print("Livros alugados com sucesso.")
    except Exception as e:
        print(f"Erro ao verificar aluguel de livros: {e}")
        raise e

@then('Eu devo ver os detalhes do usuário com os livros alugados')
def step_check_user_details(context):
    """
    Verifica os detalhes do usuário com os livros alugados.
    """
    try:
        user_details = get_user_details(context.user_id, context.token)
        assert "books" in user_details, "Nenhum livro alugado foi encontrado."
        print("Detalhes do usuário exibidos com sucesso.")
        for book in user_details["books"]:
            print(f"Título: {book['title']}, ISBN: {book['isbn']}")
    except Exception as e:
        print(f"Erro ao verificar detalhes do usuário: {e}")
        raise e