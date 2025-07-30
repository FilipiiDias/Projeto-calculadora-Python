##Projeto calculadora Python

import os

def exibir_nome_calculadora():
    print("🇧 🇪 🇲  🇻 🇮 🇳 🇩 🇴  🇦  🇨 🇦 🇱 🇨 🇺 🇱 🇦 🇩 🇴 🇷 🇦  🇩 🇴  🇫 🇮 🇫 🇮 !!")

def exibir_opcoes():
    print("""
ESCOLHA QUAL OPERAÇÃO QUER FAZER
1. Soma
2. Subtração          
3. Multiplicação
4. Divisão
5. Historico de calculos
""")
    
def finalizar_app():
    limpar_terminal()
    print("Finalizando os calculos")

def limpar_terminal():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def opcao_invalida():
   print('Opção inválida, digite apenas numeros!\n')
   input('Digite uma tecla para voltar ao menu principal')
   main()

def funcao_voltar_menu():
    input("Digite uma tecla para voltar ao menu:")
    main()

def soma():
    try:
        a,b = list(map(int, input("Digite dois números separados por espaço: ").split()))
        resultado = a + b
        print(f"{resultado}")
        funcao_voltar_menu()
    except:
        opcao_invalida()

def subtracao():
    try:
        a,b = list(map(int, input("Digite dois números separados por espaço: ").split()))
        resultado = a - b
        print(f"{resultado}")
        funcao_voltar_menu()
    except:
        opcao_invalida()

def multiplicacao():
    try:
        a,b = list(map(int, input("Digite dois números separados por espaço: ").split()))
        resultado = a * b
        print(f"{resultado}")
        funcao_voltar_menu()
    except:
        opcao_invalida()

def divisao():
    try:
        a,b = list(map(int, input("Digite dois números separados por espaço: ").split()))
        resultado = a / b
        print(f"{resultado}")
        funcao_voltar_menu()
    except:
        opcao_invalida()

def escolher_opcao():
    try:
        opcao_escolhida = int(input("Escolha uma das opções: "))
        if opcao_escolhida == 1:
            limpar_terminal()
            soma()
        elif opcao_escolhida == 2: 
            subtracao()
        elif opcao_escolhida == 3: 
            multiplicacao()
        elif opcao_escolhida == 4: 
            divisao()
        elif opcao_escolhida == 5: 
            subtracao()
        else:
            opcao_invalida()       
    except:
        opcao_invalida()

def main():
    limpar_terminal()
    exibir_nome_calculadora()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()