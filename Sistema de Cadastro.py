from pastapacote.funcoes import interface
from pastapacote.funcoes import principais
from time import sleep
arquivo_texto = "CADASTRO_COMPLETO.txt"
if not principais.verif_arq(arquivo_texto):
    principais.cria_arq(arquivo_texto)
interface.cabeçalho("SISTEMA DE CADASTRO COMPLETO DE PESSOAS FÍSICAS")
interface.cabeçalho(f"{'>>> MENU <<<':^47}")
print(interface.linha(53,linhas=True))
while True:
    usuario = interface.menu(['CADASTRAR PESSOAS','VER TODOS OS CADASTROS','SAIR DO SISTEMA'])
    if usuario == 1:
        while True:
            interface.cabeçalho("__Opção->__1__")
            while True:
                nome = input("NOME COMPLETO:").strip()
                if nome.replace(' ','').isalpha():
                    break
                else:
                    print(f"{interface.cor(8)}ERRO!{interface.cor(0)}ESSE É O ÚNICO DADO OBRIGATÓRIO!DIGITE UM NOME VÁLIDO...")
            principais.nome_pessoas(arquivo_texto,nome)
            if not principais.continuar(documento=arquivo_texto):
                break
            ano_nascimento = principais.data("ANO DO NASCIMENTO:")
            principais.idade(arquivo_texto,ano_nascimento)
            if not principais.continuar(documento=arquivo_texto):
                break
            altura = principais.altura(arquivo_texto,"ALTURA (METROS):")
            peso = principais.peso(arquivo_texto, "PESO (Kg):")
            while True:
                imc = input('DESEJA SABER QUAL É SEU I.M.C.?\nCLIQUE EM [S] para incluir o I.M.C., ou [N] para não incluir o I.M.C.:\n').strip().lower()
                if imc in "s":
                    calimc = principais.calculoIMC(arquivo_texto, altura, peso)
                    print(f"O seu I.M.C. é {calimc:.2f}, e também foi registrado com sucesso.")
                    break
                elif imc in "n":
                    break
                else:
                    print(f"{interface.cor(8)}Resposta inválida.{interface.cor(0)}")
            if not principais.continuar(documento=arquivo_texto):
                break
            while True:
                convenio = input(f"Possui convênio médico?[S] para sim, e [N] para não.").strip().lower()
                if convenio in "s":
                    convenio = True
                    principais.cadastra_Convenio(arquivo_texto,convenio)
                    break
                elif convenio in 'n':
                    convenio = False
                    principais.cadastra_Convenio(arquivo_texto,convenio)
                    break
                else:
                    print(f"{interface.cor(8)}ERRO.{interface.cor(0)}Resposta Inválida.Digite [S] para sim, e [N] para não.")
            if not principais.continuar(documento=arquivo_texto):
                break
            while True:
                sus = input(f"Possui CADASTRO no SUS - SISTEMA ÚNICO DE SAÚDE?[S] para sim, e [N] para não.").strip().lower()
                if sus in "s":
                    convenio = True
                    principais.sus(arquivo_texto,convenio)
                    principais.finalizar(arquivo_texto)
                    break
                elif sus in 'n':
                    convenio = False
                    principais.sus(arquivo_texto,convenio)
                    principais.finalizar(arquivo_texto)
                    break
                else:
                    print(f"{interface.cor(8)}ERRO.{interface.cor(0)}Resposta Inválida.Digite [S] para sim, e [N] para não.")
                print(f"{interface.cor(7)}Cadastro finalizado.{interface.cor(0)}")
            break
        interface.rein()

    elif usuario == 2:
        interface.cabeçalho("__Opção->__2__")
        principais.verdados(arquivo_texto)
        interface.rein()
    elif usuario == 3:
        interface.cabeçalho("__Opção->__3__")
        sleep(0.7)
        interface.cabeçalho("SAINDO DO SISTEMA.")
        sleep(0.7)
        interface.cabeçalho("TCHAU!")
        break
    else:
        sleep(0.2)
        print(f"{interface.cor(8)}Você digitiu uma opção inválida.Tente Novamente!{interface.cor(0)}")
        interface.rein()
