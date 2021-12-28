
import random                   #Importa a biblioteca random
import os                       #importa a biblioteca com funções referenes ao OS
import platform
if platform.system() == 'Linux':      # Detecta qual sistema operacional esta sendo usado
    clear = lambda: os.system('clear')# para poder implentar a função de limpar a tela
else:
    clear = lambda: os.system('cls')
clear()
#Lista contendo o modelo do handman
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

           +---+
           |   |
               |
               |
               |
               |
           =========''', '''

           +---+
           |   |
           O   |
               |
               |
               |
           =========''', '''

           +---+
           |   |
           O   |
           |   |
               |
               |
           =========''', '''

           +---+
           |   |
           O   |
          /|   |
               |
               |
           =========''', '''

           +---+
           |   |
           O   |
          /|\  |
               |
               |
           =========''', '''

           +---+
           |   |
           O   |
          /|\  |
          /    |
               |
           =========''', '''

           +---+
           |   |
           O   |
          /|\  |
          / \  |
               |
           =========''']
#Função que gera palavras aleatoras apartir do arquivo palavra
def rand_word():
    with open("palavras.txt", "rt") as f:
        bank = f.readlines()
    return bank[random.randint(0, len(bank))].strip()

#Classe handman
class handman:
      def __init__(self,word):                      #contrutor

          self.word = word
          self.list_IN =list(self.word)             #transforma a palavra aleatoria gerada em uma lista
          self.list_OUT = self.list_IN.copy()       #Faz uma copia de list_IN
          self.count = 0                            #contador

      def hide_word(self):                          #Esconde a palavra

          for n, i in enumerate(self.list_OUT):
              self.list_OUT[n] = '_'                #Transforma cada caracter da palavra em '_'
          return print(*self.list_OUT,sep=' ')      #Imprime a lista sem os simbolos [ ] e ,

      def guess(self, letter):                      #Adivinha qual é a palavra

          self.letter = letter                      #Entrada do caracter digitado
          while self.list_OUT != self.list_IN:
              for n, i in enumerate(self.list_OUT): #Varre a lista list.OUT
                if self.list_IN[n] == self.letter:  #Compara se a lista  list_IN possui o caracter digitado
                   self.list_OUT[n] = self.letter   #Se tiver, list_OUT recebe o valor digitado
              return self.list_OUT


      def hangman_won(self):                        #Checa se o jogador venceu

          if self.list_IN.count(self.letter)>0:     #Conta quantas caracateres tem na lista iguais ao valor digitado
             return True                            #Se tiver algum '>0', retorna verdadeiro
          else:                                     #Senão devolve falso e incrementa o contador
             self.count +=1
             if self.count >= 6:                    #Se for maior ou igual a 6(Numero de tentativas)retorna False
                return False
             else:
                return True


      def print_game_status(self):                   #Chama a lista board imprime na tela conforme se comete erros
          return board[self.count]

      def hangman_over(self):                        #Checa se o jogo acabou
          if self.list_OUT != self.list_IN :         #Ele acaba quando as duas listas se tornal iguais
              return True
          else:
              return False

def main():                                          #Executa o programa
    clear()                                          #Limpa a tela
    word = handman(rand_word())                      #Objeto word recebe a classe handman com o valor da palavra aleatoria
    print(word.print_game_status())                  #Chama o metodo para imprimir na tela o desenho da forca
    word.hide_word()                                 #Esconde a palavra digitada

    x=0
    wordIN = input("Digita ai bb: ")                 #Armazena na variavel wordIN o caracter digitado
    b= word.guess(wordIN)
    clear()
    while x==0:                                      #loop para rodar o programa enquanto não houver vencedor ou derrotado

        if word.hangman_over():                      #Verifica se o jogo acabou
            pass
        else:
            print(*b, sep=' ')
            print('Parabéns você ganhou')
            break
        if word.hangman_won():                       #Verifica se o jogador venceu
            print(word.print_game_status())
            print(*b,sep=' ')
            wordIN = input("Digita ai bb: ")
            b = word.guess(wordIN)
            clear()
        else:
            print(word.print_game_status())
            print(*b,'\nVocê perdeu a palavra era: ',word.word, sep=' ')
            break

# Executa o programa
if __name__ == "__main__":
	main()
