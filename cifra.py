class Cifra:
    def __init__(self):#, file):
        #self.arquivo = file
        self.senha = "senhaBoa"
        self.textoOriginal = "teste DE mensagem" #uftuf ef nfotbhfn
        self.textoCifrado = ""
    
    def getArquivo(self):
        print("pega arquivo")
    
    def newChave(self):
        print("criar a chave e salvar com a de salvar do chaves.py")
    
    def cifrar(self):
        print("fazer a cifra do teste")
        #Colocar texto em textoOriginal
        self.textoCifrado = ""
        textoRef = self.textoOriginal.upper()
        self.senha = self.senha.upper()
        refA = ord('A')
        i = 0
        for letra in textoRef:
            increm = ord(self.senha[i%len(self.senha)]) - refA
            if (ord(letra) >= ord('A')) and (ord(letra) <= ord('Z')):
                cod = ((ord(letra) - refA) + increm) % 26
                cod += refA
            else:
                cod = ord(letra)
            self.textoCifrado += chr(cod)
            i += 1
            
    def cifrarCase(self):
        #Colocar texto em textoOriginal
        self.textoCifrado = ""
        self.senha = self.senha.upper()
        refA = ord('A')
        refa = ord('a')
        i = 0
        for letra in self.textoOriginal:
            increm = ord(self.senha[i%len(self.senha)]) - refA
            if (ord(letra) >= ord('A')) and (ord(letra) <= ord('Z')):
                cod = ((ord(letra) - refA) + increm) % 26
                cod += refA
            elif (ord(letra) >= ord('a')) and (ord(letra) <= ord('z')):
                cod = ((ord(letra) - refa) + increm) % 26
                cod += refa
            else:
                cod = ord(letra)
            self.textoCifrado += chr(cod)
            i += 1
    
    def save(self):
        print("salvar o arquivo Cifrado")
        
    
obj = Cifra()

obj.cifrar()
print(obj.textoCifrado)
obj.cifrarCase()
print(obj.textoCifrado)