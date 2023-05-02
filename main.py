from cifra import Cifra
from decifra import Decifra
from ataque import Ataque

inicio = True

while inicio:    
    operacao = input("Que operação deseja realizar?\n\n1- Cifrar\n2- Decifrar\n3- Atacar\n\n")
    
    if(operacao.isdigit()):
        operacao = int(operacao)
        if(operacao == 1):
            inicio = False
            
            cifra = Cifra()
            cifra.getArquivo()
            cifra.getChave()
            
            inicioCifra = True
            
            while inicioCifra:
                
                operacaoCifra = input("Que operação deseja realizar?\n\n1- Manter maiúsculo e minúsculo \n2- Não precisa manter\n\n")
                
                if(operacaoCifra.isdigit()):
                    operacaoCifra = int(operacaoCifra)
                    if(operacaoCifra == 1):
                        inicioCifra = False
                        cifra.cifrar()
                    elif(operacaoCifra == 2):
                        inicioCifra = False
                        cifra.cifrarCase()
                    else:
                        print("Selecione uma opção válida \n")
                else:
                        print("Selecione uma opção válida \n")
            
            cifra.save()

        elif(operacao == 2):
            inicio = False
            
            decifra = Decifra()
            decifra.getArquivo()
            decifra.getChave()
            
            inicioDecifra = True
            
            while inicioDecifra:
                
                operacaoDecifra = input("Que operação deseja realizar?\n\n1- Manter maiúsculo e minúsculo \n2- Não precisa manter\n\n")
                
                if(operacaoDecifra.isdigit()):
                    
                    operacaoDecifra = int(operacaoDecifra)
                    
                    if(operacaoDecifra == 1):
                        inicioDecifra = False
                        decifra.decifrar()
                    elif(operacaoDecifra == 2):
                        inicioDecifra = False
                        decifra.decifrarCase()
                    else:
                        print("Selecione uma opção válida \n")
                else:
                        print("Selecione uma opção válida \n")
            
            decifra.save()
        
        elif(operacao == 3):
            print("Atacar")
            inicio = False
        else:
            print("Selecione uma opção viável \n");
    else:
        print("Selecione uma opção viável \n");1