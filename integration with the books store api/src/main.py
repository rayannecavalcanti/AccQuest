import requests
from api import (
    create_user,
    generate_token,
    is_user_authorized,
    get_all_books,
    rent_books,
    get_user_details,
)


def choose_books(books):
    """
    Permite ao usuário escolher livros para alugar a partir de uma lista de livros disponíveis.

    Args:
        books (dict): Dicionário contendo a lista de livros disponíveis.

    Returns:
        list: Lista de ISBNs dos livros escolhidos.
    """
    print("\nLivros disponíveis:")
    for i, book in enumerate(books["books"], start=1):
        print(f"{i}. ISBN: {book['isbn']}, Título: {book['title']}")

    chosen_books = []
    while True:
        choice = input(
            "\nEscolha o número do livro que deseja alugar (ou digite 'sair' para finalizar): "
        )
        if choice.lower() == "sair":
            break
        try:
            choice = int(choice)
            if 1 <= choice <= len(books["books"]):
                chosen_books.append(books["books"][choice - 1]["isbn"])
                print(
                    f"Livro '{books['books'][choice - 1]['title']}' adicionado à lista de aluguel."
                )
            else:
                print("Escolha inválida. Por favor, escolha um número válido.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

    return chosen_books


def display_user_details(user_details):
    """
    Exibe os detalhes do usuário e os livros alugados.

    Args:
        user_details (dict): Dicionário contendo os detalhes do usuário e os livros alugados.
    """
    print("\nDetalhes do Usuário:")
    print(f"ID do Usuário: {user_details['userId']}")
    print(f"Nome de Usuário: {user_details['username']}")
    print("\nLivros Alugados:")
    for book in user_details["books"]:
        print(f"\nTítulo: {book['title']}")
        print(f"Subtítulo: {book['subTitle']}")
        print(f"Autor: {book['author']}")
        print(f"ISBN: {book['isbn']}")
        print(f"Editora: {book['publisher']}")
        print(f"Data de Publicação: {book['publish_date']}")
        print(f"Número de Páginas: {book['pages']}")
        print(f"Descrição: {book['description']}")
        print(f"Website: {book['website']}")
        print("-" * 40)


def main():
    """
    Função principal que orquestra a criação do usuário, geração de token,
    listagem de livros, aluguel de livros e exibição dos detalhes do usuário.
    """
    try:
        print("Criando um usuário...")
        username = "tsdeastxUser123"
        password = "Test@123"
        user = create_user(username, password)
        user_id = user["userID"]
        print(f"Usuário criado com ID: {user_id}")

        print("\nGerando token de acesso...")
        token_response = generate_token(username, password)
        token = token_response["token"]
        print(f"Token gerado: {token}")

        print("\nVerificando se o usuário está autorizado...")
        authorized = is_user_authorized(username, password)
        print(f"Usuário autorizado: {authorized}")

        print("\nListando os livros disponíveis...")
        books = get_all_books()
        for book in books["books"]:
            print(f"ISBN: {book['isbn']}, Título: {book['title']}")

        chosen_isbns = choose_books(books)

        if chosen_isbns:
            print("\nAlugando os livros escolhidos...")
            rent_response = rent_books(user_id, token, chosen_isbns)
            print(f"Livros alugados: {rent_response}")

            print("\nListando os detalhes do usuário com os livros escolhidos...")
            user_details = get_user_details(user_id, token)
            display_user_details(user_details)
        else:
            print("\nNenhum livro foi escolhido para aluguel.")

    except requests.exceptions.HTTPError as err:
        print(f"Erro HTTP: {err}")
        print(f"Resposta do servidor: {err.response.text}")
    except Exception as err:
        print(f"Erro: {err}")


if __name__ == "__main__":
    main()