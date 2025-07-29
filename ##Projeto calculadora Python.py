##Projeto calculadora Python

import os

def exibir_nome_calculadora():
    print("BEM VINDO A CALCULADORA DO FIFI")

def exibir_opcoes():
    print("""
ESCOLHA QUAL OPERAÇÃO QUER FAZER
1. Soma
2. Subtração          
3. Multiplicação
4. Divisão
5. Historico de calculos
6. Sair
""")
    
def finalizar_app():
    os.system("cls")
    print("Finalizando os calculos")

def opcao_invalida():
   print('Opção inválida, digite apenas numeros!\n')
   input('Digite uma tecla para voltar ao menu principal')
   main()

def funcao_voltar_menu():
    input("Digite uma tecla para voltar ao menu:")
    main()

def soma(a, b):
     return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return a / b

    funcao_voltar_menu()
##Criando o dicionario das funções
funcoes = {
    1: soma,
    2: subtracao,
    3: multiplicacao,
    4: divisao
}
def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma das opções: '))
        if opcao_escolhida in funcoes:
            funcoes[opcao_escolhida]()
        elif opcao_escolhida == 6: 
            finalizar_app
        else:
            opcao_invalida()       
    except:
        opcao_invalida()

def main():
    os.system("cls")
    exibir_nome_calculadora()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()