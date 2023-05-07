from collections import Counter

class Ataque:
    freq_ingles = [8.167, 1.492, 2.782, 4.253, 12.702, 2.228, 2.015, 6.094, 6.966, 0.153, 0.772, 4.025, 2.406, 6.749, 7.507, 1.929, 0.095, 5.987, 6.327, 9.056, 2.758, 0.978, 2.360, 0.150, 1.974, 0.074]
    freq_portugues = [14.63, 1.04, 3.88, 4.99, 12.57, 1.02, 1.30, 1.28, 6.18, 0.40, 0.02, 2.78, 4.74, 5.05, 10.73, 2.52, 1.20, 6.53, 7.81, 4.34, 4.63, 1.67, 0.01, 0.21, 0.01, 0.47] 

    def __init__(self):
        self.nomeArquivo = ""
        self.chave = ""
        self.textoOriginal = ""
        self.textoCifrado = ""
        self.textoAjustado = ""
        self.frequencia = {"Bloco":"", "Repeticoes": 0}
        self.numLetras = 0
    
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
                for i in range(len(self.textoAjustado) - j + 1):
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
                distance.append(cont+1)
                cont = 0
            else:
                cont += 1
        mdcDic = {}
        
        for j in range(1, len(distance)):
            for i in range(j+1, len(distance)):
                self.mdc(distance[j], distance[i], mdcDic)
        
        mdcComum = max(mdcDic, key=mdcDic.get)
        
        print("\n\nAs distancias encontradas para " + "'" +self.frequencia["Bloco"] + "' são: " + str(distance))
        print("Os MDCs entre as distâncias e suas respectivas frequências são: " + str(mdcDic))
        print("\n\nO tamanho da palavra sujerida é: "+ str(mdcComum))
        
        while (True):
            operacao = input("Qual tamanho deseja usar (maior ou igual a 2)? \n\n 0 - Se quiser manter sujestão \n")
            
            if (operacao.isdigit() and int(operacao) == 0):
                self.numLetras = mdcComum
                break;
            
            elif (operacao.isdigit() and int(operacao) >= 2):  
                self.numLetras = int(operacao);
                break;
            
            else:
                print("Insira um valor válido")
    
    def itera(self, iterando):
        i = -1
        iterando[i] += 1
        while i > -(self.numLetras):
            if iterando[i] == 3:
                iterando[i] = 0
                iterando[i-1] += 1
            i -= 1
        if iterando[i] == 3:
            return None
        return iterando
    
    def gerarSenhas(self, letrasPossiveis):

        iterando = []
        senhas = []
        
        for i in range(self.numLetras):
            iterando.append(0)
        
        while iterando != None:
            i = 0
            palavra = ""
            #print(letrasPossiveis)
            while i < self.numLetras:
                palavra += chr(letrasPossiveis[i][iterando[i]])
                i += 1
            iterando = self.itera(iterando)
            senhas.append(palavra)   
        return senhas
                    
    
    def findChave(self):
        #print("descobrir a chave - Salvar com a de salvar do chaves.py")
        textoSep = []
        i = 0
        
        lingua = input("O texto original está em que língua? (p)Português ou (i)Inglês \n")
        
        if lingua == 'p' or lingua == 'P':
            ingles = False
            portugues = True
        if lingua == 'i' or lingua == 'I':
            ingles = True
            portugues = False
        

        for j in range(self.numLetras):
            textoSep.append("")

        for i in range(len(self.textoAjustado)):
            textoSep[i%self.numLetras] += self.textoAjustado[i] #Separa texto em listas de caracteres q cada letra da chave codificou
          
        #contagemChar = []
        letrasFreq = []
        maisFreq = []
        
        for i in range(self.numLetras):
            #contagemChar.append(Counter(textoSep[i]))
            letrasFreq.append(list(dict(Counter(textoSep[i]).most_common(2)).keys())) #Pega as 3 letras mais comuns de cada lista separada
            
        if ingles: #Pega letras mais frequentes do inglês
            maisFreq.append(self.freq_ingles.index(sorted(self.freq_ingles)[-1]) + ord('A'))
            maisFreq.append(self.freq_ingles.index(sorted(self.freq_ingles)[-2]) + ord('A'))
           # maisFreq.append(self.freq_ingles.index(sorted(self.freq_ingles)[-3]) + ord('A'))
            
        if portugues: #Pega letras mais frequentes do português
            maisFreq.append(self.freq_portugues.index(sorted(self.freq_portugues)[-1]) + ord('A'))
            maisFreq.append(self.freq_portugues.index(sorted(self.freq_portugues)[-2]) + ord('A'))
           # maisFreq.append(self.freq_portugues.index(sorted(self.freq_portugues)[-3]) + ord('A'))
        
        letrasPossiveis = []
                
        
        for letter in range(self.numLetras):
            letrasPossiveis.append([])
            for i in range(2):
                for j in range(2):
                    if i == 1 and j == 1:
                        break
                    aux = (ord(letrasFreq[letter][i]) - maisFreq[j])%26
                    letrasPossiveis[letter].append(ord('A') + aux)
                    #print("Letra " + str(letter) + " pode ser: " + chr(ord('A') + aux))
                    
        
        possiveisSenhas = self.gerarSenhas(letrasPossiveis)
        
        self.escolheSenha(possiveisSenhas)
    
    def escolheSenha(self, possiveisSenhas):
        i = 6
        words = []
        while len(words) == 0:
            i -= 1
            words = [word for word in self.textoCifrado.split() if len(word) == i]
        index = self.textoCifrado.index(words[0])
        #print(words[0])
        #print(self.textoAjustado)
        indexSenha = self.textoAjustado.index(words[0].upper())
        index2 = index + 1
        while index2 - index < self.numLetras or self.textoCifrado[index2] != " ":
            index2 += 1
        trechoTeste = self.textoCifrado[index:index2]
        
        i = 0
        certo = '0'
        while certo == '0' and i < len(possiveisSenhas):
            print("Algum dessas alternativas faz sentido?", end = "\n\n")
            print("0 - Nenhuma")
            verificacao = []
            j = 1
            for i in range (i, i + 10):
                if i < len(possiveisSenhas):
                    verificacao.append(self.decifra(trechoTeste, possiveisSenhas[i], indexSenha))
                    print(str(j) + " - " + verificacao[j-1])
                    j += 1
                    
            certo = input()
        
        if certo == '0' or i > len(possiveisSenhas):
            print("Chave não encontrada")
        
        else:
            print("Sua chave é: " + possiveisSenhas[i-(10-int(certo))])
                
            
    
    def decifra(self, trecho, chave, i):
        refA = ord('A')
        trecho = trecho.upper()
        
        textoResult = ""
        
        for letra in trecho:
            increm = (ord(chave[i%len(chave)]) - refA)
            if (ord(letra) >= ord('A')) and (ord(letra) <= ord('Z')):
                cod = ((ord(letra) - refA) - increm) % 26
                cod += refA
                i += 1
            else:
                cod = ord(letra)
                
            textoResult += chr(cod)
            
        return textoResult
    
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

#obj = Ataque()
#obj.ajustaTexto()
#obj.getFrequence()
#obj.findDistances()
#obj.findChave()