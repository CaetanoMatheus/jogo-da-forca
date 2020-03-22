from random import randrange

def imprime_mensagem_abertura():
    print('*'*33)
    print('** Bem vindo ao jogo da Forca! **')
    print('*'*33)

def carrega_palavra_secreta():
    palavras = arquivo_para_array('palavras.txt')
    numero_aleatorio = pegar_numero_aleatorio(palavras)
    return palavras[numero_aleatorio].lower()

def arquivo_para_array(arquivo):
    aux = open(arquivo, 'r')
    palavras = []
    for linha in aux:
        palavras.append(linha.strip())
    aux.close()
    return palavras

def pegar_numero_aleatorio(array_de_dados):
    return randrange(0, len(array_de_dados))

def inicializa_letras_acertadas(palavra_secreta):
    return ['_' for letra in palavra_secreta]

def nova_tentativa():
    return input('Informe uma letra? : ').strip().lower()

def marca_chute_correto(palavra_secreta, chute, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if (erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if (erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if (erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if (erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if (erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if (erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def imprime_mensagem_vitoria():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_mensagem_derrota(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


imprime_mensagem_abertura()
palavra_secreta = carrega_palavra_secreta()
letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

print(letras_acertadas)
enforcou = False
acertou = False
erros = 0

while (not enforcou and not acertou):
    chute = nova_tentativa()
    if (chute in palavra_secreta):
        marca_chute_correto(palavra_secreta, chute, letras_acertadas)
    else:
        erros += 1
        desenha_forca(erros)
    enforcou = erros == 7
    acertou = '_' not in letras_acertadas
    print(letras_acertadas)

if (acertou):
    imprime_mensagem_vitoria()
else:
    imprime_mensagem_derrota(palavra_secreta)
    