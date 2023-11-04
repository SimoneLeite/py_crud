import os

# Classe para interfacr do usuário do programa

class interface:
    def __int__(self):
        pass

    def logoTipo(self):
        print("====================================")
        print("=========Catálago de Filmes=========")
        print("====================================")

    def limpaTela(self):
        os.system('cls' if os.name == 'nt' else 'clear')
   # Função que permite o usuário escolher uma opção

    def selecionaOpcao(self, opcoesPermitidas = []) :
        opcaoSelecionada = input("Digite a opção desejada: ")  

        if opcaoSelecionada =="":
            return self.selecionaOpcao(opcoesPermitidas)

        try:
            opcaoSelecionada = int(opcaoSelecionada)
        except ValueError:
            print("opção inválida!") 
            self.selecionaOpcao()
            return self.selecionaOpcao(opcoesPermitidas)

        if opcaoSelecionada not in opcoesPermitidas:
            print("Opção inválida!")   
            return self.selecionaOpcao(opcoesPermitidas) 

            return opcaoSelecionada
          

       
   