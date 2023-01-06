from pastapacote.funcoes import interface
import datetime
from time import sleep

def data(num):
    while True:
        teste = input((num))
        n = teste
        if not n:
            (print(f"{interface.cor(8)}ERRO.{cor(0)}Digite algo..."))
        if len(n) == 4:
            if n.isnumeric():
                n = int(n) #o erro estava acontecendo, para transformar 'n' em 'int' é preciso atribuir a alguma variável
                break
            elif n.isalpha or n.isalnum():
                (print(f"{interface.cor(8)}Erro.{interface.cor(0)}Digite uma data válida..."))
        else:
            print(f"{interface.cor(8)}ERRO.{interface.cor(0)}Digite uma data válida...")
    return n

def leiaFloat(num):
    while True:
        try:
            teste = float(input(num))
        except ValueError:
            print(f"{interface.cor(8)}ERRO!{interface.cor(0)}Digite um número válido.")
            print(f"{interface.cor(8)}Se o erro persistir, utilize ponto ao invés de vírgula.{interface.cor(0)}")
        else:
            return teste


def verif_arq(nome):
    try:
        arquivo = open(nome, 'rt')
        arquivo.close()
    except FileNotFoundError:
        print(f"{interface.cor(8)}ERRO!{interface.cor(0)} Arquivo inexistente.")
        return False
    else:
        return True


def cria_arq(nome):
    try:
        arquivo = open(nome, "wt+")
        arquivo.close()
    except Exception as erro:
        print(f"{interface.cor(8)}ERRO!Este arquivo não pôde ser aberto.{interface.cor(0)} Verifique o que aconteceu.")
    else:
        print(f"{interface.cor(3)}O arquivo .txt {arquivo} foi criado com sucesso!{interface.cor(0)}")


def nome_pessoas(documento, n="'<desconhecido>'"):
    try:
        arquivo = open(documento, 'at')
    except Exception as erro:
        erro = "Ocorreu algum erro, o arquivo não abriu."
        print(f"{interface.cor(8)}{erro}{interface.cor(0)}")
    else:
        try:
            arquivo.write(f"Nome:{n};")
        except Exception as erro2:
            erro2 = "NÃO FOI POSSÍVEL CADASTRAR OS DADOS"
            print(f"{interface.cor(8)}{erro2}{interface.cor(0)}")
        else:
            print(f"{interface.cor(3)}Concluído.{interface.cor(0)}")
        arquivo.close()


def verdados(nome):
    try:
        arquivo = open(nome, 'rt')
    except Exception as erro3:
        erro3 = 'ERRO!\n'
        print(f'{interface.cor(8)}{erro3}Erro ao ler o arquivo.{interface.cor(0)}')
    else:
        interface.cabeçalho(msg="LISTA DOS CADASTRADOS")
        contador = 1
        for c in arquivo:
            print(f"{interface.cor(4)}{contador}){interface.cor(0)}")
            for varredura in c.split(';'):
                print(f"{interface.cor(f=3)}{varredura:>}{interface.cor(f=0)}", end=(""))
                print()
            contador += 1
    finally:
        arquivo.close()


def continuar(documento,perg="Cadastrar mais dados desta pessoa? [S] para sim e [N] para não.", valida=True):
    while True:
        mais = str(input(perg)).strip().lower()
        if mais[0] in 's':
            return valida
        elif mais[0] in 'n':
            while True:
                try:
                    arquivo = open(documento, 'at')
                except Exception as erro:
                    erro = "Ocorreu algum erro, o arquivo não abriu."
                    print(f"{interface.cor(8)}{erro}{interface.cor(0)}")
                else:
                    try:
                        arquivo.write(f"\n")
                    except Exception as erro2:
                        erro2 = "NÃO FOI POSSÍVEL IR PARA O PRÓXIMO CADASTRO"
                        print(f"{interface.cor(8)}{erro2}{interface.cor(0)}")
                    else:
                        print(f"{interface.cor(3)}Concluído.{interface.cor(0)}")
                        arquivo.close()
                        break
            valida = False
            print(f"{interface.cor(7)}Cadastro finalizado.{interface.cor(0)}")
            break
        elif mais != 'sn':
            print(f"{interface.cor(8)}ERRO{interface.cor(0)}.DIGITE UMA RESPOSTA VÁLIDA.{interface.cor(3)}[S]{interface.cor(0)} PARA SIM ou {interface.cor(3)}[N]{interface.cor(0)} PARA NÃO")


def idade(documento,dt):
    anoatual = datetime.date.today().year
    idade = anoatual - dt
    try:
        arquivo = open(documento, 'at')
    except Exception as erro:
        erro = "Ocorreu algum erro, o arquivo não abriu."
        print(f"{interface.cor(8)}{erro}{interface.cor(0)}")
    else:
        try:
            arquivo.write(f"Idade:{idade};")
        except Exception as erro2:
                erro2 = "NÃO FOI POSSÍVEL CADASTRAR OS DADOS"
                print(f"{interface.cor(8)}{erro2}{interface.cor(0)}")
        else:
            print(f"{interface.cor(3)}Concluído.{interface.cor(0)}")
            arquivo.close()


def peso(documento,p):
    while True:
        teste = input(p)
        if ',' in teste: #esse if é opcional
            teste = teste.replace(',','.')
            #print(teste)
        try:
            teste = float(teste)
        except ValueError:
            print(f'{interface.cor(8)}ALGO DEU ERRADO.{interface.cor(0)}Digite apenas números.')
        else:
            try:
                arquivo = open(documento, 'at')
            except Exception as erro:
                erro = "Ocorreu algum erro, o arquivo não abriu."
                print(f"{interface.cor(8)}{erro}{interface.cor(0)}")
            else:
                try:
                    arquivo.write(f"PESO:{teste:.1f}Kg;")
                except Exception as erro2:
                    erro2 = "NÃO FOI POSSÍVEL CADASTRAR OS DADOS"
                    print(f"{interface.cor(8)}{erro2}{interface.cor(0)}")
                else:
                    print(f"{interface.cor(3)}Concluído.{interface.cor(0)}")
                    arquivo.close()
        break
    return teste

def altura(documento,a):
    while True:
        teste = input(a)
        #if ',' in teste: #esse if é opcional
        teste = teste.replace(',','.')
            #print(teste)
        try:
            teste = float(teste)
        except ValueError:
            print(f'{interface.cor(8)}ALGO DEU ERRADO.{interface.cor(0)}Digite apenas números.')
        else:
            try:
                arquivo = open(documento, 'at')
            except Exception as erro:
                erro = "Ocorreu algum erro, o arquivo não abriu."
                print(f"{interface.cor(8)}{erro}{interface.cor(0)}")
            else:
                try:
                    arquivo.write(f"ALTURA:{teste:.2f}m;")
                except Exception as erro2:
                    erro2 = "NÃO FOI POSSÍVEL CADASTRAR OS DADOS"
                    print(f"{interface.cor(8)}{erro2}{interface.cor(0)}")
                else:
                    print(f"{interface.cor(3)}Concluído.{interface.cor(0)}")
                    arquivo.close()
        break
    return teste



def calculoIMC(documento,a=0,p=0):
    calculo = p / (a**2)
    if a == 0 or p == 0:
        print(f"{interface.cor(8)}INFORMAÇÕES INSUFICIENTES PARA CALCULAR O SEU I.M.C.{interface.cor(0)}")
    try:
        arquivo = open(documento, 'at')
    except Exception as erro:
        erro = "Ocorreu algum erro, o arquivo não abriu."
        print(f"{interface.cor(8)}{erro}{interface.cor(0)}")
    else:
        try:
            arquivo.write(f"IMC -> O índice de massa corpórea é: {calculo:.2f};")
        except Exception as erro2:
            erro2 = "NÃO FOI POSSÍVEL CADASTRAR OS DADOS"
            print(f"{interface.cor(8)}{erro2}{interface.cor(0)}")
        else:
            print(f"{interface.cor(3)}Concluído.{interface.cor(0)}")
            arquivo.close()
        return calculo


def cadastra_Convenio(documento,c=True):
    try:
        arquivo = open(documento, 'at')
    except Exception as erro:
        erro = "Ocorreu algum erro, o arquivo não abriu."
        print(f"{interface.cor(8)}{erro}{interface.cor(0)}")
    else:
        try:
            if c:
                arquivo.write(f"POSSUI CONVÊNIO MÉDICO PARTICULAR;")
            if not c:
                c = False
                arquivo.write(f"NÃO POSSUI CONVÊNIO MÉDICO PARTICULAR;")
        except Exception as erro2:
            erro2 = "NÃO FOI POSSÍVEL CADASTRAR OS DADOS"
            print(f"{interface.cor(8)}{erro2}{interface.cor(0)}")
        else:
            print(f"{interface.cor(3)}Concluído.{interface.cor(0)}")
            arquivo.close()

def sus(documento,s=True):
    try:
        arquivo = open(documento, 'at')
    except Exception as erro:
        erro = "Ocorreu algum erro, o arquivo não abriu."
        print(f"{interface.cor(8)}{erro}{interface.cor(0)}")
    else:
        try:
            if s:
                arquivo.write(f"POSSUI CADASTRO NO SISTEMA ÚNICO DE SAÚDE (SUS);")
            if not s:
                s = False
                arquivo.write(f"NÃO POSSUI CADASTRO NO SISTEMA ÚNICO DE SAÚDE (SUS);")
        except Exception as erro2:
            erro2 = "NÃO FOI POSSÍVEL CADASTRAR OS DADOS"
            print(f"{interface.cor(8)}{erro2}{interface.cor(0)}")
        else:
            print(f"{interface.cor(3)}Concluído.{interface.cor(0)}")
            arquivo.close()
        return s


def finalizar(documento):
    try:
        arquivo = open(documento, 'at')
    except Exception as erro:
        erro = "Ocorreu algum erro, o arquivo não abriu."
        print(f"{interface.cor(8)}{erro}{interface.cor(0)}")
    else:
        try:
            arquivo.write(f"\n") #aqui faz a quebra da linha para o próximo cadastrado
        except Exception as erro2:
            erro2 = "NÃO FOI POSSÍVEL IR PARA O PRÓXIMO A SER CADASTRADO OU FINALIZAR O PROCESSO."
            print(f"{interface.cor(8)}{erro2}{interface.cor(0)}")
        else:
            arquivo.close()
            print(f"{interface.cor(7)}O CADASTRO DESSA PESSOA ESTÁ COMPLETO.{interface.cor(0)}")

