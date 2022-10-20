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
    
    
  def fleurynotIsEuleriano(self, listaNumber, listaGuardarVértice, listaSUPREME, listaListaNumber):
    
    
   
    
   if len(listaGuardarVértice) == 0:
    listaGuardarVértice.append(listaNumber[0])
    listaListaNumber.append(list(listaNumber).copy())
   elif listaGuardarVértice[0] == listaNumber[0]:
    listaGuardarVértice.append(listaNumber[0])
    listaListaNumber.append(list(listaNumber).copy())
   elif listaGuardarVértice[0] != listaNumber[0]:
    listaSUPREME.append(listaListaNumber.copy())
    listaListaNumber.clear()   
    qtdV = len(listaGuardarVértice)
    listaGuardarVértice.clear()
    listaGuardarVértice.append(listaNumber[0])
    listaListaNumber.append(list(listaNumber).copy())
    if qtdV % 2 != 0:
      return True
  #  print(listaSUPREME)
    
  
  def fleuryPrinci(self, listaSUPREME):
    tamList = len(listaSUPREME)
    cont = 0
    destino = 0
    caminhoLista = []
    while cont < tamList:
      inicio = listaSUPREME[destino]
      caminhoLista.append(list(inicio[0]).copy())
      destino = inicio[1]            
      cont = cont + 1
    
      

  
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
    # Fim variaveis grafos não eulerianos
    listaVerticeeArestas = []
    for item in arquivinho:
      
      if contadorpularPrimeiraLinha != 0:
        linhaTratada = self.tratarLinha(item)
               
        
        
        # Testar se o grafo é Euleriano  
        isNotEulerian =  self.fleurynotIsEuleriano(linhaTratada, listaGuardarVértice, listaVerticeeArestas, listaListaNumber)
        if isNotEulerian:
          print("\nEsse grafo NÃO é euleriano\n")
          return
      else:
        contadorpularPrimeiraLinha = contadorpularPrimeiraLinha + 1
    self.fleuryPrinci(listaVerticeeArestas)   
 
    
     
  
  
  