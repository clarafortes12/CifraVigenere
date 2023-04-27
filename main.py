from chaves import Chaves 
from cifra import Cifra
from decifra import Decifra
from ataque import Ataque

operacao = int(input("Que operação deseja realizar?\n\n1- Cifrar\n2- Decifrar\n3- Atacar\n\n"))

if(operacao == 1):
    print("Cifrar")
elif(operacao == 2):
    print("Decifrar")
elif(operacao == 3):
    print("Atacar")
else:
    print("Selecione uma opção viável");

