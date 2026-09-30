produtos = ["Arroz", "Feijão", "Café", "Açúcar"]

print("Lista original:")
print(produtos)

produtos[1] = "Macarrão"

produtos.remove("Café")

print("Lista final:")
print(produtos)

# Tentar remover um produto que não existe
if "Leite" in produtos:
    produtos.remove("Leite")
else:
    print("Leite não está na lista")