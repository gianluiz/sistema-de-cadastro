from pastapacote.funcoes import principais
from time import sleep
color = ('\033[m', #a cor 0ZERO será 'sem cor'
     '\033[1;4;31m', #cor 1 - vermelho
     '\033[32m', ##cor 2 - verde
     '\033[1;33m', ##cor 3 - amarelo
     '\033[7;30;44m', ##cor 4 - fundo preto letra azul (invertido)
     '\033[0;30;45m', ##cor 5 - roxo
     '\033[0;40m', #cor 6 -  branco
     '\033[30;44m',#cor 7 - fundo azul letra preta
     '\033[30;41m' #cor 8 - fundo vermelho letra preta
         )


def linha(tam=10,linhas=False):
    tamanho = 0
    if linhas == False:
        tamanho = tam
        return tamanho
    elif linhas == True:
        tamanho = '-' * tam
        return tamanho


def leiaInt(num):
    while True:
        try:
            teste = int(input(num))
        except Exception as error: #ou except (ValueError, TypeError)
            print(f'{cor(8)}ERRO!Digite um dado válido.{cor(0)} Erro do tipo {error.__class__}')
            continue
        #except KeyboardInterrupt:
        #    print('\033[0;32mO usuário interrompeu o programa\033[m')
        #    return 0
        else:
            return teste


def cor(f=0):
    escolhe = color[f]
    return escolhe


def cabeçalho(msg=""):
    quant = (len(msg)+6) * '-'
    print(linha(tam=quant))
    print(f"{cor(7)}{msg.center((len(msg)+6))}{cor(0)}")


def menu(lista):
    contador = 1
    print(f"{cor(4)}{'QUAL É A SUA OPÇÃO NO MENU?'.center(50):^53}{cor(0)}")
    for c in lista:
        print(f"\n{cor(7)}{contador}){c:^51}{cor(0)}")
        contador += 1
    numero_do_menu = leiaInt(f"Digite a sua opção - {cor(3)}[1]{cor(0)} - {cor(3)}[2]{cor(0)} - {cor(3)}[3]{cor(0)}\n->")
    return numero_do_menu


def rein():
    palavra = "RETORNANDO AO MENU..."
    for c in palavra:
        print(f'{c}',end=(""))
        sleep(0.05)
    print()


def linhadiv(documento):
    try:
        arquivo = open(documento, 'at')
    except Exception as erro:
        erro = "Ocorreu algum erro, o arquivo não abriu."
        print(f"{cor(8)}{erro}{cor(0)}")
    else:
        try:
            arquivo.write("\n=-=-=-=-=-=-\n")
        except Exception as erro2:
            erro2 = "NÃO FOI POSSÍVEL CADASTRAR OS DADOS"
            print(f"{cor(8)}{erro2}{cor(0)}")
        else:
            print("Concluído.")
            arquivo.close()

