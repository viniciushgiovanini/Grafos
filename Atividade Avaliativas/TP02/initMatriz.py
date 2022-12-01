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
  # Gera a lista de elemento da matriz
  # ---
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
  
  # ---
  # Le do arquivo e gera a lista de origem e destino de cada elemento (vertice)
  # ---
  def gerandoListas(self, nomeArq):
    
    strInterpolacao = "db/" + nomeArq + '.txt'
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
        contadorLoopPrinci = contadorLoopPrinci + 1
      else:
        qtddeLinhas = self.tratarPrmeiraLinhaQTD(item)+1
        contadorpularPrimeiraLinha = contadorpularPrimeiraLinha + 1
    return listaVerticeeArestas  
  
  # ---
  # Funcao utilizada pela funcao fleury que pega o vertice manda para o naive testar se
  # ir por esse caminho.
  # ---
  def pesquisarCaminho(self, nomeArq, verticeInicial):
    listaVerticeeArestas = self.gerandoListas(nomeArq)
    # Pesquisa NAIVE
    caimhoOuTrajeto = []   
    caimhoOuTrajeto = list(self.fleury(listaVerticeeArestas, verticeInicial))
    # for item in caimhoOuTrajeto:
    #   print( str(item) + "\n")     
    self.isCaminhoOrTrajeto(caimhoOuTrajeto)
    
  
  
  