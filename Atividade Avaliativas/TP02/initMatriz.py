# Aluno: Vinícius Henrique Giovanini

class gerarMatriz:
  
  # ---
  # Pega a linha e tranforma em uma lista contendo o primeiro e o segundo numero,
  # referente a origem e o destino
  # ---
  def tratarLinha(self, item):
    item = item.lstrip()
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
   
  # ---
  # Pega a primeira linha referente a quantidade de elementos e linha, e retorna a
  # quantidade de linhas.
  # --- 
  def tratarPrmeiraLinhaQTD(self, item):
    cont = 0
    marcador = False
    qtdNumero = ""
    while cont < len(item):
      if item[cont] == " " or marcador:
        if marcador and item[cont] != "\n":
         qtdNumero = qtdNumero + item[cont]
        marcador = True
      cont = cont + 1
    return int(qtdNumero)
  
  # ---
  # Pegar a quantidade de vertices que tem no grafo
  # ---
  def tratarPrmeiraLinhaQTDVertices(self, item):
    cont = 0
    marcador = True
    qtdNumero = ""
    while cont < len(item) and marcador:
       if item[cont] == ' ':
         marcador = False
       else:
        qtdNumero = qtdNumero + item[cont]
       cont = cont + 1
    return int(qtdNumero)
  
  # ---
  # Gera a lista de elemento da matriz
  # ---
  def realizandoGeracaoLista(self, listaNumber, listaGuardarVértice, listaSUPREME, listaListaNumber):
   if len(listaGuardarVértice) == 0:
    listaGuardarVértice.append(listaNumber[0])
    listaListaNumber.append(list(listaNumber).copy())
   elif (listaGuardarVértice[0] == listaNumber[0]):
    listaGuardarVértice.append(listaNumber[0])
    listaListaNumber.append(list(listaNumber).copy())
   elif (listaGuardarVértice[0] != listaNumber[0]):
    posicaoAdd = listaListaNumber[0][0]-1
    listaSUPREME.pop(posicaoAdd)
    listaSUPREME.insert(posicaoAdd,listaListaNumber.copy())
    listaListaNumber.clear()   
    listaGuardarVértice.clear()
    listaGuardarVértice.append(listaNumber[0])
    listaListaNumber.append(list(listaNumber).copy())
  
  # ---
  # Le do arquivo e gera a lista de origem e destino de cada elemento (vertice)
  # ---
  def gerandoListas(self, nomeArq):
    
    strInterpolacao = "db/" + nomeArq + '.txt'
    reader = open(strInterpolacao, "r")  
    arquivinho = reader.readlines()
    contadorpularPrimeiraLinha = 0
    
    listaGuardarVértice = [] 
    listaListaNumber = []

    listaVerticeeArestas = []
    contadorLoopPrinci = 0
    
    for item in arquivinho:
      
      if contadorpularPrimeiraLinha != 0:
        linhaTratada = self.tratarLinha(item)
             
        # Estou fazendo o flag com a quantidade de linha, melhor fazer com o ultimo elemento.
        
        # Testar se o grafo é Euleriano  
        self.realizandoGeracaoLista(linhaTratada, listaGuardarVértice, listaVerticeeArestas, listaListaNumber)
        contadorLoopPrinci = contadorLoopPrinci + 1
      else:
        qtddeVertices = self.tratarPrmeiraLinhaQTDVertices(item)
        listaVerticeeArestas = [[]]*qtddeVertices
      contadorpularPrimeiraLinha = contadorpularPrimeiraLinha + 1
    
    if item != []:
      posicaoAdd = listaListaNumber[0][0]-1
      listaVerticeeArestas.pop(posicaoAdd)
      listaVerticeeArestas.insert(posicaoAdd,listaListaNumber.copy())
    return listaVerticeeArestas  