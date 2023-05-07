#   SEGURANÇA COMPUTACIONAL
#   TRABALHO 1
#   MARIA CLARA OLIVEIRA FORTES -       19/0017503
#   THIAGO CARDOSO PINHEIRO DIAS PAIS - 16/0146372
#

from auxiliar import Auxiliar
from vigenere import Vigenere
from ataque import Ataque

inicio = True

while inicio:    
    operacao = input("Que operação deseja realizar?\n\n1- Cifrar\n2- Decifrar\n3- Atacar\n\n")
    
    if(operacao.isdigit()):
        operacao = int(operacao)
        if(operacao == 1):
            inicio = False
            
            auxiliar = Auxiliar()
            cifra = Vigenere()
            
            auxiliar.getArquivo(operacao)
            cifra.nomeArquivo = auxiliar.nomeArquivo
            cifra.textoOriginal = auxiliar.textoArquivo
            
            cifra.getChave()

            inicioCifra = True
            
            while inicioCifra:
                
                operacaoCifra = input("Que operação deseja realizar?\n\n1- Manter maiúsculo e minúsculo \n2- Não precisa manter\n\n")
                
                if(operacaoCifra.isdigit()):
                    operacaoCifra = int(operacaoCifra)
                    if(operacaoCifra == 1):
                        inicioCifra = False
                        cifra.vigenere_generico(operacao, False)
                    elif(operacaoCifra == 2):
                        inicioCifra = False
                        cifra.vigenere_generico(operacao)
                    
                    else:
                        print("Selecione uma opção válida \n")
                else:
                        print("Selecione uma opção válida \n")
            
            auxiliar.textoArquivo = cifra.textoCifrado
            auxiliar.saveArquivo(operacao, auxiliar.nomeArquivo, auxiliar.textoArquivo)
        elif(operacao == 2):
            inicio = False
            
            auxiliar = Auxiliar()
            decifra = Vigenere()
            
            auxiliar.getArquivo(operacao)
            decifra.nomeArquivo = auxiliar.nomeArquivo
            decifra.textoCifrado = auxiliar.textoArquivo
            
            decifra.getChave()

            inicioCifra = True
            
            while inicioCifra:
                
                operacaoCifra = input("Que operação deseja realizar?\n\n1- Manter maiúsculo e minúsculo \n2- Não precisa manter\n\n")
                
                if(operacaoCifra.isdigit()):
                    operacaoCifra = int(operacaoCifra)
                    if(operacaoCifra == 1):
                        inicioCifra = False
                        decifra.vigenere_generico(operacao, False)
                    elif(operacaoCifra == 2):
                        inicioCifra = False
                        decifra.vigenere_generico(operacao)
                    
                    else:
                        print("Selecione uma opção válida \n")
                else:
                        print("Selecione uma opção válida \n")
            
            auxiliar.textoArquivo = decifra.textoOriginal
            auxiliar.saveArquivo(operacao, auxiliar.nomeArquivo, auxiliar.textoArquivo)
        
        elif(operacao == 3):
            inicio = False
            
            auxiliar = Auxiliar()
            ataque = Ataque()
            
            auxiliar.getArquivo(operacao)
            ataque.nomeArquivo = auxiliar.nomeArquivo
            ataque.textoCifrado = auxiliar.textoArquivo
            
            ataque.ajustaTexto()
            ataque.getFrequence()
            ataque.findDistances()
            ataque.findChave()
        else:
            print("Selecione uma opção viável \n");
    else:
        print("Selecione uma opção viável \n");1