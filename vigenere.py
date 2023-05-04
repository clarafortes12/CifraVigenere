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

    def vigenere_generico(self, cif_dec, caseMantido = True): #cif_dec - (1, 2) responsável por cifrar ou decifrar, respectivamente
        
        self.chave = self.chave.upper()
        refA = ord('A')
        refa = ord('a')
        i = 0
        
        textoResult = ""
        
        if cif_dec == 1:
            auxMult = 1
            textoRef = self.textoOriginal
        elif cif_dec == 2:
            auxMult = -1
            textoRef = self.textoCifrado
            
        if not caseMantido:
            textoRef = textoRef.upper()
        
        for letra in textoRef:
            increm = auxMult*(ord(self.chave[i%len(self.chave)]) - refA)
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
        elif cif_dec == 2:
            self.textoOriginal = textoResult