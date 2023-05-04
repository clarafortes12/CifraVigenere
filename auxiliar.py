class Auxiliar:    
    def __init__(self):
        self.nomeArquivo = ""
        self.textoArquivo = ""
    
    def getArquivo(self, tipo):
        if(tipo == 1 ):
            #Cifra
            text_input = "Insira o caminho completo do arquivo .txt que deseja cifrar: "
        elif(tipo == 2):
            #Decifra
            text_input = "Insira o caminho completo do arquivo .txt que deseja decifrar: "
        elif(tipo == 3):
            #Ataque
            text_input = "Insira o caminho completo do arquivo .txt que deseja atacar: "
        
        arquivo = input(text_input)
        
        nome_arquivo = arquivo[0:-4]
        cont_barra = 0
        for i in range(len(arquivo)):
            if(arquivo[i]=='/' or arquivo[i]=="\\"):
                cont_barra = i

        nome_arquivo = nome_arquivo[cont_barra+1:]
        
        self.nomeArquivo = nome_arquivo
        file_leitura = open(arquivo, 'r', encoding='UTF8')
        
        file_leitura.seek(0,0)
        text_aux = ""
        
        linha = file_leitura.readline()
        while not linha == '':
            text_aux += linha 
            linha = file_leitura.readline()
        
        self.textoArquivo = text_aux
        
        file_leitura.close()
        
    def saveArquivo(self, tipo, nomeArquivo, texto):
        if(tipo == 1 ):
            #Cifra
            text_arquivo = "Original"
            nome_salvo = "Cifrado"
        elif(tipo == 2):
            #Decifra
            text_arquivo = "Cifrado"
            nome_salvo = "Original"
        elif(tipo == 3):
            #Ataque
            text_arquivo = "Cifrado"
            nome_salvo = "Chave"
        
        if(nomeArquivo.find(text_arquivo) == -1):
            arquivo = nomeArquivo
        else:
            arquivo = nomeArquivo.split(text_arquivo)[0]
        
        file_crifrado = open(arquivo+nome_salvo+'.txt', 'w')
        file_crifrado.write(texto)
        file_crifrado.close()
        
    