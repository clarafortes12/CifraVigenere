class Vigenere:
    def __init__(self):
        self.nomeArquivo = ""
        self.chave = ""
        self.textoOriginal = ""
        self.textoCifrado = ""

    def getChave(self):
        while(True):
            arquivo = input("Insira o caminho completo do arquivo .txt que contém a senha OU Insira a senha: ")
            
            if(arquivo.find(".txt") == -1):
                self.chave = arquivo
            else:
                file_leitura = open(arquivo, 'r')
                file_leitura.seek(0,0)    
                
                self.chave = file_leitura.readline()
                
                file_leitura.close()
            
            if(self.chave.find(" ") == -1 and self.chave.isalpha()):
                break
            else:
                print("\nInsira uma senha sem espaço de contendo apenas letras \n")
            
    def cifrar(self):
        self.textoCifrado = ""
        textoRef = self.textoOriginal.upper()
        self.chave = self.chave.upper()
        refA = ord('A')
        i = 0
        for letra in textoRef:
            increm = ord(self.chave[i%len(self.chave)]) - refA
            if (ord(letra) >= ord('A')) and (ord(letra) <= ord('Z')):
                cod = ((ord(letra) - refA) + increm) % 26
                cod += refA
            else:
                cod = ord(letra)
            self.textoCifrado += chr(cod)
            i += 1
            
    def cifrarCase(self):
        self.textoCifrado = ""
        self.chave = self.chave.upper()
        refA = ord('A')
        refa = ord('a')
        i = 0
        for letra in self.textoOriginal:
            increm = ord(self.chave[i%len(self.chave)]) - refA
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
    
    def decifrar(self):
        print("fazer o decifra do texto")
        self.textoOriginal = ""
        textoRef = self.textoCifrado.upper()
        self.chave = self.chave.upper()
        refA = ord('A')
        i = 0
        for letra in textoRef:
            increm = ord(self.chave[i%len(self.senha)]) - refA
            if (ord(letra) >= ord('A')) and (ord(letra) <= ord('Z')):
                cod = ((ord(letra) - refA) - increm) % 26
                cod += refA
            else:
                cod = ord(letra)
            self.textoCifrado += chr(cod)
            i += 1
            
    def decifrarCase(self):
        self.textoOriginal = ""
        self.chave = self.chave.upper()
        refA = ord('A')
        refa = ord('a')
        i = 0
        for letra in self.textoCifrado:
            increm = ord(self.chave[i%len(self.chave)]) - refA
            if (ord(letra) >= ord('A')) and (ord(letra) <= ord('Z')):
                cod = ((ord(letra) - refA) - increm) % 26
                cod += refA
            elif (ord(letra) >= ord('a')) and (ord(letra) <= ord('z')):
                cod = ((ord(letra) - refa) - increm) % 26
                cod += refa
            else:
                cod = ord(letra)
            self.textoOriginal += chr(cod)
            i += 1
    
    def vigenere_generico(self, cif_dec, caseMantido = True): #cif_dec - (1, -1) responsável por cifrar ou decifrar, respectivamente
        self.textoOriginal = ""
        self.chave = self.chave.upper()
        refA = ord('A')
        refa = ord('a')
        i = 0
        
        textoResult = ""
        
        if cif_dec == 1:
            textoRef = self.textoOriginal
        elif cif_dec == -1:
            textoRef = self.textoCifrado
            
        if not caseMantido:
            textoRef = textoRef.upper()
        
        for letra in self.textoRef:
            increm = cif_dec*(ord(self.chave[i%len(self.chave)]) - refA)
            if (ord(letra) >= ord('A')) and (ord(letra) <= ord('Z')):
                cod = ((ord(letra) - refA) + increm) % 26
                cod += refA
                i += 1
            elif (ord(letra) >= ord('a')) and (ord(letra) <= ord('z')):
                cod = ((ord(letra) - refa) + increm) % 26
                cod += refa
                i += 1
            else:
                cod = ord(letra)
                
            textoResult += chr(cod)
            
        if cif_dec == 1:
            self.textoCifrado = textoResult
        elif cif_dec == -1:
            self.textoOriginal = textoResult