class Ataque:
    def __init__(self):
        self.nomeArquivo = ""
        self.chave = ""
        self.textoOriginal = ""
        self.textoCifrado = ""
    
    def getArquivo(self):
        arquivo = input("Insira o caminho completo do arquivo .txt que deseja atacar: ")
        
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
        
        self.textoCifrado = text
        
        file_leitura.close()
    
    def findChave(self):
        print("descobrir a chave - Salvar com a de salvar do chaves.py");
    
    def saveChave(self):
        if(self.nomeArquivo.find("Cifrado") == -1):
            arquivo = self.nomeArquivo
        else:
            arquivo = self.nomeArquivo.split("Cifrado")[0]
        
        file_crifrado = open(arquivo+'Chave.txt', 'w')
        file_crifrado.write(self.chave)
        file_crifrado.close()
    
    def saveDecifra(self):
        if(self.nomeArquivo.find("Cifrado") == -1):
            arquivo = self.nomeArquivo
        else:
            arquivo = self.nomeArquivo.split("Cifrado")[0]
        
        file_crifrado = open(arquivo+'Original.txt', 'w')
        file_crifrado.write(self.textoOriginal)
        file_crifrado.close()