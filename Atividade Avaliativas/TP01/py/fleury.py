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
  
  def realizandoFleury(self, listaNumber, listaGuardarVértice, listaSUPREME, listaListaNumber, ultimoElemento):
   if len(listaGuardarVértice) == 0:
    listaGuardarVértice.append(listaNumber[0])
    listaListaNumber.append(list(listaNumber).copy())
   elif (listaGuardarVértice[0] == listaNumber[0]) and not ultimoElemento:
    listaGuardarVértice.append(listaNumber[0])
    listaListaNumber.append(list(listaNumber).copy())
   elif (listaGuardarVértice[0] != listaNumber[0]) and not ultimoElemento:
    listaSUPREME.append(listaListaNumber.copy())
    listaListaNumber.clear()   
    qtdV = len(listaGuardarVértice)
    listaGuardarVértice.clear()
    listaGuardarVértice.append(listaNumber[0])
    listaListaNumber.append(list(listaNumber).copy())
    if qtdV % 2 != 0:
      return True
   elif ultimoElemento:
     listaGuardarVértice.append(listaNumber[0])
     listaListaNumber.append(list(listaNumber).copy())
     listaSUPREME.append(listaListaNumber.copy())
     listaListaNumber.clear()  
  
  def selecionandoMenorElemento(self, lista):
    resp = 10000000000000
    listaResposta = []
    for item in lista:
     if item[1] < resp:
      resp = item[1]
      listaResposta = item.copy()
    return listaResposta
  
  def analisandoFleury(self, listaSUPREME, qtdLinhas):
    # Precisa colocar o naive aqui para identificar pontes.
    cont = 0
    destino = 0
    caminhoLista = []
    while cont < qtdLinhas-1:
      inicio = listaSUPREME[destino]
      posicaoLista = listaSUPREME.index(inicio)
      menorValorEntreOsVertices = list(self.selecionandoMenorElemento(inicio))
      caminhoLista.append(menorValorEntreOsVertices.copy())
      listaSUPREME[posicaoLista].remove(menorValorEntreOsVertices)    
      destino = menorValorEntreOsVertices[1] - 1            
      cont = cont + 1
    return caminhoLista
      

  
  def fleuryInicial(self, nomeArq, entradaFL):
    
    strInterpolacao = ''
    entradaFL = int(entradaFL)
    if entradaFL == 1:
       strInterpolacao = 'data/grafosEulerianos/' + nomeArq + '.txt'
    elif entradaFL == 2:
       strInterpolacao = 'data/grafosNaoEulerianos/' + nomeArq + '.txt'
    elif entradaFL == 3:
       strInterpolacao = 'data/grafosSemiEulerianos/' + nomeArq + '.txt'
    else:
      print("Grafo não encontrado")
      return
    
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
        isNotEulerian =  self.realizandoFleury(linhaTratada, listaGuardarVértice, listaVerticeeArestas, listaListaNumber, flagcontadorLoopPrinciUltimoElement)
        if contadorLoopPrinci == qtddeLinhas -3:
          flagcontadorLoopPrinciUltimoElement = True
        contadorLoopPrinci = contadorLoopPrinci + 1
        if isNotEulerian:
          print("\nEsse grafo NÃO é euleriano\n")
          return
      else:
        qtddeLinhas = self.tratarPrmeiraLinhaQTD(item)
        contadorpularPrimeiraLinha = contadorpularPrimeiraLinha + 1
    caimhoOuTrajeto = []    
    caimhoOuTrajeto = list(self.analisandoFleury(listaVerticeeArestas, qtddeLinhas))
    for item in caimhoOuTrajeto:
      print( str(item) + "\n")
     
    
     
  
  
  