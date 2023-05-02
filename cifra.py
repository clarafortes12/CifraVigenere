class Cifra:
    def __init__(self):
        self.nomeArquivo = ""
        self.chave = ""
        self.textoOriginal = ""
        self.textoCifrado = ""
    
    def getArquivo(self):
        arquivo = input("Insira o caminho completo do arquivo .txt que deseja cifrar: ")
        
        nome_arquivo = arquivo[0:-4]
        cont_barra = 0
        for i in range(len(arquivo)):
            if(arquivo[i]=='/' or arquivo[i]=="\\"):
                cont_barra = i

        nome_arquivo = nome_arquivo[cont_barra+1:]
        
        self.nomeArquivo = nome_arquivo
        file_leitura = open(arquivo, 'r')
        
        file_leitura.seek(0,0)
        text = ""
        
        linha = file_leitura.readline()
        while not linha == '':
            text += linha 
            linha = file_leitura.readline()
        
        self.textoOriginal = text
        
        file_leitura.close()
    
    def getChave(self):
        arquivo = input("Insira o caminho completo do arquivo .txt que contém a senha OU Insira a senha: ")
        
        if(arquivo.find(".txt") == -1):
            self.chave = arquivo
        else:
            file_leitura = open(arquivo, 'r')
            file_leitura.seek(0,0)    
            
            self.chave = file_leitura.readline()
            
            file_leitura.close()
    
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
    
    def save(self):
        if(self.nomeArquivo.find("Original") == -1):
            arquivo = self.nomeArquivo
        else:
            arquivo = self.nomeArquivo.split("Original")[0]
        
        file_crifrado = open(arquivo+'Cifrado.txt', 'w')
        file_crifrado.write(self.textoCifrado)
        file_crifrado.close()