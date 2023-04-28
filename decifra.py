class Decifra:
    def __init__(self):#, file):
        #self.arquivo = file
        self.senha = "senhaBoa"
        self.textoOriginal = "lifae RE qrusbuee"
        self.textoCifrado = ""
    
    def getArquivo():
        print("pega arquivo cifrado")
        print("pega arquivo chave")

    def decifrar(self):
        print("fazer o decifra do texto")
        #Colocar texto em textoOriginal
        self.textoCifrado = ""
        textoRef = self.textoOriginal.upper()
        self.senha = self.senha.upper()
        refA = ord('A')
        i = 0
        for letra in textoRef:
            increm = ord(self.senha[i%len(self.senha)]) - refA
            if (ord(letra) >= ord('A')) and (ord(letra) <= ord('Z')):
                cod = ((ord(letra) - refA) - increm) % 26
                cod += refA
            else:
                cod = ord(letra)
            self.textoCifrado += chr(cod)
            i += 1
            
    def decifrarCase(self):
        #Colocar texto em textoOriginal
        self.textoCifrado = ""
        self.senha = self.senha.upper()
        refA = ord('A')
        refa = ord('a')
        i = 0
        for letra in self.textoOriginal:
            increm = ord(self.senha[i%len(self.senha)]) - refA
            if (ord(letra) >= ord('A')) and (ord(letra) <= ord('Z')):
                cod = ((ord(letra) - refA) - increm) % 26
                cod += refA
            elif (ord(letra) >= ord('a')) and (ord(letra) <= ord('z')):
                cod = ((ord(letra) - refa) - increm) % 26
                cod += refa
            else:
                cod = ord(letra)
            self.textoCifrado += chr(cod)
            i += 1
    
    def save(self):
        print("salvar o arquivo original")
        
        
obj = Decifra()

obj.decifrar()
print(obj.textoCifrado)
obj.decifrarCase()
print(obj.textoCifrado)