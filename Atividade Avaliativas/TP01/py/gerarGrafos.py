#imports
import random
import os

class criarGrafos:

  #funcoes globais 
  def isPath(self, caminho):
    resp = False
    if (os.path.exists(caminho)):
      resp = True
    return resp 
  #------------------------------------------
  #funcoes do grafo Euleriano  
  def gerarVerticesEulerianos(self, cont, grau, obj, listaRR):
    cont2 = 0
    contadorLaco = 1
    marcadorLaco = False
    valor1 = -1
    while(cont2 < grau):
      # Salvar cont no arquivo e numero sorteado
      if len(listaRR) != 0 and marcadorLaco == False: 
       destinoAresta = listaRR[0]
       
      else:
       destinoAresta = listaRR[contadorLaco]
       contadorLaco = contadorLaco+1
    
      
      if destinoAresta == cont or destinoAresta == valor1:
        marcadorLaco = True
        grau = grau + 1
      else:
        valor1 = destinoAresta
        contadorLaco = 1
        marcadorLaco = False
        listaRR.remove(destinoAresta)
        
        
       
       
      
      if not marcadorLaco:
       stringMontada = str(cont) + " " + str(destinoAresta)
       obj.write(stringMontada + "\n")  
      
      stringMontada = ""     
      cont2 = cont2 + 1
    # listaRR = []  
      
  def criarEulerianos(self,tamReq, nomeArq):
    
    # Verificar se o arquivo existe
    strInterpolacao = 'data/grafosEulerianos/' + nomeArq + '.txt'
    arquivoExiste = self.isPath(strInterpolacao)   
        
    
    if (arquivoExiste == False):
      oPP = open(strInterpolacao, 'wb+')
      oPP.close()
    else:
      open(strInterpolacao, 'w').close()
            
    
    obj = open(strInterpolacao, 'r+')
    
    
    
    
    #  grau = random.randrange(1, 11, 2)
    
    grau = 2
    # referente as duas linhas salvas la em cima
    # qtdLinhas = 1 + ((grau * int(tamReq)) - (((grau-(grau2))) * int(tamReq/(tamReq/10))))
    qtdLinhas = 1 + ((grau * int(tamReq)))
    obj.write(str(tamReq) + "_" + str(qtdLinhas) + "\n")
    
    listaRR = []
    listaRang= range(1, tamReq+1)
    for item in listaRang:
     listaRR.append(item)

    listaRRsemo1 = listaRR.copy()   
    listaRRsemo1.pop(0)
    concatCont = 0
    while (concatCont < grau - 1):
      if (concatCont+1) < grau-1:
        listaRR = listaRR + listaRR
      else:
        listaRR = listaRR + listaRRsemo1
      concatCont = concatCont + 1

    random.shuffle(listaRR)
    cont = 1
    while cont <= tamReq:
      if cont == tamReq:
        grau = grau -1
      
      self.gerarVerticesEulerianos(cont, grau, obj, listaRR)     
      
      if cont == tamReq:
        stringMontada = str(cont) + " " + str(1)
        obj.write(stringMontada + "\n")  
      cont = cont + 1
        
    
    obj.close()  

  #------------------------------
  # grafo Nao euleriano
  def criarNaoEulerianos(self, qtdVertice, nomeArq):
    # Verificar se o arquivo existe
    strInterpolacao = 'data/grafosNaoEulerianos/' + nomeArq + '.txt'
    arquivoExiste = self.isPath(strInterpolacao)   
        
    
    if (arquivoExiste == False):
      oPP = open(strInterpolacao, 'wb+')
      oPP.close()
    else:
      open(strInterpolacao, 'w').close()
            
    
    obj = open(strInterpolacao, 'r+')
    
    
    
    
    #  grau = random.randrange(1, 11, 2)
    grau = 4
    # grauDivisaoLinha = 1
    if qtdVertice == 1000:
     grau = 4
    #  grauDivisaoLinha = 10
    elif qtdVertice == 100000:
      grau = 2
      # grauDivisaoLinha = 1000
    
    grau2 = grau - (grau-1)
    # referente as duas linhas salvas la em cima
    qtdLinhas = 1 + ((grau * int(qtdVertice)) - ((grau-grau2) * int(qtdVertice/(qtdVertice/10))))
    obj.write(str(qtdVertice) + "_" + str(qtdLinhas) + "\n")
        
    listaRR = []
    listaRang= range(1, qtdVertice+1)
    for item in listaRang:
     listaRR.append(item)
  
    concatCont = 0
    while (concatCont < grau-1):
      listaRR = listaRR + listaRR
      concatCont = concatCont + 1
      
    random.shuffle(listaRR)
    
    
    
    cont2Chega = qtdVertice/10
    cont = 1
    cont2 = 1
    isGrau2 = False
    temp = -1
    while cont <= qtdVertice:
      
      if cont2 == cont2Chega and cont2Chega != 0:
        temp = grau
        grau = grau2
        cont2 = 0
        isGrau2 = True
      
      self.gerarVerticesEulerianos(cont, grau, obj, listaRR)     
      cont2 = cont2 + 1
      cont = cont + 1
      
      if isGrau2:
        grau = temp
        isGrau2 = False
    
    
    obj.close()
    
  #-------------------------------
  #grafo Semi Euleriano
  def criarSemiEulerianos(self, qtdVertice, nomeArq):
  # Verificar se o arquivo existe
    strInterpolacao = 'data/grafosSemiEulerianos/' + nomeArq + '.txt'
    arquivoExiste = self.isPath(strInterpolacao)   
        
    
    if (arquivoExiste == False):
      oPP = open(strInterpolacao, 'wb+')
      oPP.close()
    else:
      open(strInterpolacao, 'w').close()
            
    
    obj = open(strInterpolacao, 'r+')
    
    
    
    
    #  grau = random.randrange(1, 11, 2)
    grau = 4
    grau2 = grau - (grau-1)
    # grauDivisaoLinha = 1
    if qtdVertice == 1000:
     grau = 4
    #  grauDivisaoLinha = 10
    elif qtdVertice == 100000:
      grau = 2
      grau2 = 1
      # grauDivisaoLinha = 1000
    
    
    # referente as duas linhas salvas la em cima
    qtdLinhas = 1 + ((grau * int(qtdVertice)) - ((grau-grau2) * 2))
    obj.write(str(qtdVertice) + "_" + str(qtdLinhas) + "\n")
        
    listaRR = []
    listaRang= range(1, qtdVertice+1)
    for item in listaRang:
     listaRR.append(item)
  
    concatCont = 0
    while (concatCont < grau-1):
      listaRR = listaRR + listaRR
      concatCont = concatCont + 1
      
    random.shuffle(listaRR)
    
    
    
    cont2Chega = qtdVertice/10
    cont = 1
    cont2 = 1
    isGrau2 = False
    temp = -1
    contSemiEule = 0
    
    while cont <= qtdVertice:
      
      if cont2 == cont2Chega and cont2Chega != 0 and contSemiEule < 2:
        temp = grau
        grau = grau2
        cont2 = 0
        isGrau2 = True
        contSemiEule = contSemiEule + 1
      
      
      
      self.gerarVerticesEulerianos(cont, grau, obj, listaRR)     
      cont2 = cont2 + 1
      cont = cont + 1
      
      if isGrau2:
        grau = temp
        isGrau2 = False
    
    
    obj.close()   
  
