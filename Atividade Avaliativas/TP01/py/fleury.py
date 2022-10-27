from naive import naivePonte

class fleuryAlg:
  
  def tratarLinha(self, item):
    numerosTratados = []
    hasNumber1 = False
    cont = 0
    concatNumber1 = ""
    concatNumber2 = ""
    while cont < len(item):
      if item[cont] != "\n":
        if item[cont] == " ":
          hasNumber1 = True
        elif hasNumber1 == False:
          concatNumber1 = concatNumber1 + item[cont]   
        elif hasNumber1 == True and item[cont] != " ":
          concatNumber2 = concatNumber2 + item[cont]
      cont = cont + 1
    numerosTratados.append(int(concatNumber1))
    numerosTratados.append(int(concatNumber2))
    
    return numerosTratados
    
  def tratarPrmeiraLinhaQTD(self, item):
    cont = 0
    marcador = False
    qtdNumero = ""
    while cont < len(item):
      if item[cont] == "_" or marcador:
        if marcador and item[cont] != "\n":
         qtdNumero = qtdNumero + item[cont]
        marcador = True
      cont = cont + 1
    return int(qtdNumero)
  
  def realizandoGeracaoLista(self, listaNumber, listaGuardarVértice, listaSUPREME, listaListaNumber, ultimoElemento):
   if len(listaGuardarVértice) == 0:
    listaGuardarVértice.append(listaNumber[0])
    listaListaNumber.append(list(listaNumber).copy())
   elif (listaGuardarVértice[0] == listaNumber[0]) and not ultimoElemento:
    listaGuardarVértice.append(listaNumber[0])
    listaListaNumber.append(list(listaNumber).copy())
   elif (listaGuardarVértice[0] != listaNumber[0]) and not ultimoElemento:
    listaSUPREME.append(listaListaNumber.copy())
    listaListaNumber.clear()   
    listaGuardarVértice.clear()
    listaGuardarVértice.append(listaNumber[0])
    listaListaNumber.append(list(listaNumber).copy())
   elif ultimoElemento:
     listaGuardarVértice.append(listaNumber[0])
     listaListaNumber.append(list(listaNumber).copy())
     listaSUPREME.append(listaListaNumber.copy())
     listaListaNumber.clear()  
  
  
  def gerandoListas(self, nomeArq):
    
    strInterpolacao = "data/" + nomeArq + '.txt'
    reader = open(strInterpolacao, "r")  
    arquivinho = reader.readlines()
    contadorpularPrimeiraLinha = 0
    
    # Variaveis Grafos Não eulerianos    
    listaGuardarVértice = [] #esse lista é apra guardar os vértices para testar se é euleriano
    listaListaNumber = []
    #qtd_Linha
    qtddeLinhas = 1
    # Fim variaveis grafos não eulerianos
    listaVerticeeArestas = []
    contadorLoopPrinci = 0
    flagcontadorLoopPrinciUltimoElement = False
    for item in arquivinho:
      
      if contadorpularPrimeiraLinha != 0:
        linhaTratada = self.tratarLinha(item)
             
        # Estou fazendo o flag com a quantidade de linha, melhor fazer com o ultimo elemento.
        
        # Testar se o grafo é Euleriano  
        self.realizandoGeracaoLista(linhaTratada, listaGuardarVértice, listaVerticeeArestas, listaListaNumber, flagcontadorLoopPrinciUltimoElement)
        if contadorLoopPrinci == qtddeLinhas -3:
          flagcontadorLoopPrinciUltimoElement = True
          pass
        contadorLoopPrinci = contadorLoopPrinci + 1
        # if isNotEulerian:
        #   print("\nEsse grafo NÃO é euleriano\n")
        #   return
      else:
        qtddeLinhas = self.tratarPrmeiraLinhaQTD(item)
        contadorpularPrimeiraLinha = contadorpularPrimeiraLinha + 1
    return listaVerticeeArestas  
  
  def tipeGraph(self, nomeArq):
   listaVerticeeAresta = self.gerandoListas(nomeArq)
   contadorDeGrauImpar = 0
   for item in listaVerticeeAresta:
     if len(item)%2==1:
       contadorDeGrauImpar = contadorDeGrauImpar + 1
   if contadorDeGrauImpar == 0:
     print("-----X----")
     print("Esse Grafo é Euleriano")
     print("-----X----\n")
   elif contadorDeGrauImpar == 2:
     print("-----X----")
     print("Esse Grafo é Semi Euleriano")
     print("-----X----\n")
   elif contadorDeGrauImpar > 2:
     print("-----X----")
     print("Esse Grafo não é Euleriano")
     print("-----X----\n")
  
  def verificarTamLista(self, l):
    resp = False
    if len(l) == 0:
      resp = True
    return resp
    
  def fleury(self, listaSUPREME, verticeInicial):
    # Precisa colocar o naive aqui para identificar pontes.
    destino = verticeInicial-1
    caminhoLista = []
    naive = naivePonte()
    tamLista = len(listaSUPREME)-1
    # while cont < qtdLinhas-1:
    while tamLista > 0:
       inicio = listaSUPREME[destino]
      #  posicaoLista = listaSUPREME.index(inicio)
       menorValorEntreOsVertices = list(naive.proxElemento(inicio, listaSUPREME))
       caminhoLista.append(menorValorEntreOsVertices.copy())
       listaSUPREME[destino].remove(menorValorEntreOsVertices)    
       listaFicouVazia = self.verificarTamLista(listaSUPREME[destino])
       destino = menorValorEntreOsVertices[1] - 1            
       if listaFicouVazia:
         tamLista = tamLista -1 
               
    return caminhoLista  
    
  def pesquisarCaminho(self, nomeArq):
    listaVerticeeArestas = self.gerandoListas(nomeArq)
    # Pesquisa NAIVE
    caimhoOuTrajeto = []   
    caimhoOuTrajeto = list(self.fleury(listaVerticeeArestas))
    for item in caimhoOuTrajeto:
      print( str(item) + "\n")     
    
    
  
  
  