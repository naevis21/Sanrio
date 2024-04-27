
#Dicionário para armazenar as figurinhas
album = {i: 0 for i in range (1, 217)}

#Função para adicionar as figurinhas ao álbum
def adicionar_figurinha(figurinha):
    if figurinha in album:
        album[figurinha] += 1
    else:
        print("Figurinha inválida")

def adicionar_multiplas_figurinhas(lista_figurinhas):
    for figurinha in lista_figurinhas:
        adicionar_figurinha(figurinha)


# Função para verificar se uma figurinha está no álbum
def verificar_figurinha(figurinha):
    if figurinha in album:
        if album[figurinha] > 0:
            print(f"Você tem {album[figurinha]} da figurinha {figurinha}.")
        else:
            print(f"Você não tem a figurinha {figurinha}.")
    else:
        print("Figurinha inválida.")

# Função para imprimir o álbum
def print_album():
    for figurinha, quantidade in album.items():
        print(f"Figurinha {figurinha}: {quantidade}")

