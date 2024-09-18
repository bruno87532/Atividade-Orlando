import requests

"""
ISBN de alguns livros brasileiros:
9788575225486 (seu livro)
9788550814582
9788542221084
"""

informacoes_livro = ["isbn", "title", "subtitle", "authors", "publisher", "synopsis", "dimensions", "year", "format", "page_count", "subjects", "location", "retail_price", "cover_url", "provider"]
while True:
    isbn = input("Digite o ISBN de um livro: (O ISBN deve ser de um livro brasileiro)\n")
    isbn = isbn.replace(" ", "")
    r = requests.get(f"https://brasilapi.com.br/api/isbn/v1/{isbn}")
    if r.status_code != 200:
        print("Livro não presente no banco de dados da API")
    else:
        livro = r.json()
        for i in informacoes_livro:
            if livro[i]:
                print(f"{i.capitalize().replace("_", " ")}: {livro[i]}")
    consultar_outro = input("Deseja consultar outro ISBN? (s caso sim, qualquer outra tecla caso não)\n")
    if consultar_outro != "s" and consultar_outro != "S":
        break