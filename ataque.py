class Ataque:
    freq_ingles = [8.167, 1.492, 2.782, 4.253, 12.702, 2.228, 2.015, 6.094, 6.966, 0.153, 0.772, 4.025, 2.406, 6.749, 7.507, 1.929, 0.095, 5.987, 6.327, 9.056, 2.758, 0.978, 2.360, 0.150, 1.974, 0.074]
    freq_portugues = [14.63, 1.04, 3.88, 4.99, 12.57, 1.02, 1.30, 1.28, 6.18, 0.40, 0.02, 2.78, 4.74, 5.05, 10.73, 2.52, 1.20, 6.53, 7.81, 4.34, 4.63, 1.67, 0.01, 0.21, 0.01, 0.47] 

    def __init__(self):
        self.nomeArquivo = ""
        self.chave = ""
        self.textoOriginal = ""
        self.textoCifrado = ""
        self.textoAjustado = ""
        self.frequencia = {"Bloco":"", "Repeticoes": 0, "mmcDistancia": 0}
    
    def getArquivo(self):
        arquivo = input("Insira o caminho completo do arquivo .txt que deseja atacar: ")
        
        nome_arquivo = arquivo[0:-4]
        cont_barra = 0
        for i in range(len(arquivo)):
            if(arquivo[i]=='/' or arquivo[i]=="\\"):
                cont_barra = i

        nome_arquivo = nome_arquivo[cont_barra+1:]
        
        self.nomeArquivo = nome_arquivo
        file_leitura = open(arquivo, 'r', encoding='UTF8')
        
        file_leitura.seek(0,0)
        text = ""
        
        linha = file_leitura.readline()
        while not linha == '':
            text += linha 
            linha = file_leitura.readline()
        
        self.textoCifrado = text
        
        file_leitura.close()
    
    def ajustaTexto(self):
        texto = ""
        textoRef = self.textoCifrado.upper()
        
        for letra in textoRef:
            if (ord(letra) >= ord('A')) and (ord(letra) <= ord('Z')):
                texto += letra
        
        self.textoAjustado = texto
    
    def getFrequence(self):
        Repeticoes = {}
        
        if self.textoAjustado != "":
            for j in range(2,5):
                for i in range(len(self.textoAjustado)- j + 1):
                    bloco = self.textoAjustado[i:i+j]
                    
                    if bloco in Repeticoes:
                        
                        Repeticoes[bloco] += 1
                    else:
                        Repeticoes[bloco] = 1
                        
        inv = {v: k for k, v in Repeticoes.items()}
        x = inv[max(inv)]
        
        self.frequencia["Bloco"] = x
        self.frequencia["Repeticoes"] = Repeticoes[x]
    
    def mdc(self, x, y, dic):
        while y:
            x, y = y, x % y
        
        if(x != 1):
            if x in dic:
                dic[x] += 1
            else:
                dic[x] = 1
    
    def findDistances(self):
        distance = []
        cont = 0
        
        for i in range(len(self.textoAjustado)):
            bloco = self.textoAjustado[i:i+len(self.frequencia["Bloco"])]
            
            if(self.frequencia["Bloco"] == bloco):
                distance.append(cont-1)
                cont = 0
            else:
                cont += 1
        mdcDic = {}
        
        for j in range(1, len(distance)):
            for i in range(j+1, len(distance)):
                self.mdc(distance[j], distance[i], mdcDic)
        
        #Mostrar Distancias
        #Mostrar MDC
        #Mostrar Selecionada tirando o 2
        #Pedir Escolha
        
        self.frequencia["mmcDistancia"] = max(mdcDic, key=mdcDic.get)
    
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

obj = Ataque()
obj.getArquivo();
obj.ajustaTexto();
obj.getFrequence();
obj.findDistances();
print(obj.frequencia)