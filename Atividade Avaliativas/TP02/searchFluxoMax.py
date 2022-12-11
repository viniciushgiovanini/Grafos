# Aluno: Vinícius Henrique Giovanini

# from copy import deepcopy

class buscaFluxo:
  # ---
  # Essa funcao pega uma aresta e inverte o destino com a origem.add()
  # ---
  def inverterElemento(self, element):
    temp0= element[0]
    temp1 = element[1]
    valorNew = element.copy()
    valorNew[0] = temp1
    valorNew[1] = temp0
    return valorNew
  
  # Funcoes de apoio da pesquisa
  
  # ---
  # Essa funcao recebe uma lista contendo varias arestas com origem e destino, e seleciona o destino
  # de menor valor.
  # ---
  def selecionandoMenorElemento(self, lista, caminho):
    resp = 10000000000000
    listaResposta = []
    for item in lista:
     itemInvert = self.inverterElemento(item)
     if itemInvert not in caminho:
      if item[1] < resp:
       resp = item[1]
       listaResposta = item.copy()
    return listaResposta
  
  # ---
  # Essa duas funcoes abaixo pega o elemento que foi percorrido por exemplo 1-->2 e a primeira,
  # testarCiclodeVoltaRemove remove o elemento de volta na matriz principal no caso o 2 --> 1,
  # a funcao testarCiclodeVoltaRemovenaListComum, simplemente retorna se esse elemento existe.
  # ---
  def testarCiclodeVoltaRemove(self, listaSup, valor):
    valor2 = valor.copy()
    destino = valor[1]
    tmp1 = valor[0]
    valorDestino = listaSup[destino-1]
    valor2[0] = destino
    valor2[1] = tmp1
    
    for item in valorDestino:
     if item == valor2:
      listaSup[destino-1].remove(valor2)  
      
   
  # ---------------------------------------X-----------------------------------
  # Funcoes principais da pesquisa

  # ---
  # Pega a qtd dos vertices adjacentes ignorando o caminho que veio
  # ---
  def qtdVerticesAdjSemPercorrido(self, listaVertices, valorIda):
    qtd = len(listaVertices)
    for item in listaVertices:
      itemInvert = self.inverterElemento(item)
      if item in valorIda:
       qtd = qtd -1  
      if itemInvert in valorIda:
       qtd = qtd -1
    return qtd
  
  
   # ---
  # Pega a qtd dos vertices adjacentes ignorando o caminho que veio
  # ---
  def selecionarMenorElementoNaoPercorrido(self, listaVertices, valorIda):
    qtd = []
    for item in listaVertices:
      itemInvert = self.inverterElemento(item)
      if item not in valorIda:
       if itemInvert not in valorIda:
        qtd.append(item)
    return qtd
  
  # ---
  # Essa funcao inverterCaminhoPercorrido inverte toda a lista de vertices adjacentes.add()
  # ---
  def inverterCaminhoPercorrido(self, m, caminho):
    origem = 0
    destino = 0
    lADj1 = []
    lADj2 = []
    for item in caminho:
     origem = item[0]-1
     destino = item[1]-1
     arestaInvertida  = self.inverterElemento(item).copy()
     lADj1 = m[origem].copy()
     lADj1.remove(item)
     m[origem].clear()
     m[origem] = lADj1.copy()
     lADj1.clear()
     
     lADj2 = m[destino].copy()
     lADj2.append(arestaInvertida)
     m[destino].clear()
     m[destino] = lADj2.copy()
     lADj2.clear()
  
  
  # ---
  # Funcao para testar se algum vertice adjacente é o vertice desejado para evitar que escolha um ramo mais longo para percorrer
  # sendo que tem o caminho mais curto.add()
  # ---
  def analisarVerticesAdj(self, listaVerticesAdj, verticeDestino):
    resp = []
    for item in listaVerticesAdj:
     if item[1] == verticeDestino:
       resp = item.copy()
       return resp
    return resp
  
  # ---
  # Funcao para a busca pririzar ir para vertices não visitados do que voltar para vertices que ja foram visitados.add()
  # ---
  def selecionarVerticeNaoVisitado(self, listaVertice, caminhoVertice):
    listaArestasPossiveis = []
    cm2 =caminhoVertice.copy()
    for v1 in listaVertice:
      if v1[1] not in cm2:
         listaArestasPossiveis.append(v1)
         cm2.append(v1[1])
    return listaArestasPossiveis
     
  
  # ---
  # Essa e a funcao que vai realizar a navegacao até encontrar o vértice desejado ou percorrer todos os vértices.
  # ---
  
  def buscaA(self, listaSUP, arestaOrigem, verticeDestino):
    loop = True
    caminhoVertice = []
    caminho = []
    caminhoTotalBT = []
    # caminhoDebug = []
    conjuntoArestaNaOrigem = listaSUP[arestaOrigem[0]-1]
    while loop:
      destino = arestaOrigem[1]
      conjuntoArestaNoDestino = listaSUP[destino-1]
      caminho.append(arestaOrigem.copy())
      caminhoTotalBT.append(arestaOrigem.copy())
      
      
      # caminhoDebug.append(arestaOrigem.copy()) #linha de depuracoa
      # if len(caminhoDebug)==300:
      #   caminhoDebug = []
      
      caminhoVertice.append(arestaOrigem[0])
      backTrack = False
      valorT = self.qtdVerticesAdjSemPercorrido(conjuntoArestaNoDestino, caminhoTotalBT)
      if valorT == 0:
        isArestas = False
        contador = 0
        caminhoVerticeRevert = caminhoVertice.copy()
        caminhoVerticeRevert.reverse()
        for item in caminhoVerticeRevert:
         if not isArestas:
          arestasDoVerticeAnalisado = listaSUP[item-1]
          qtdADJnPercorrido = self.qtdVerticesAdjSemPercorrido(arestasDoVerticeAnalisado, caminhoTotalBT)
          if qtdADJnPercorrido>0:
             caminhoVertice.remove(item)
             verticesNpercorridos = self.selecionarMenorElementoNaoPercorrido(arestasDoVerticeAnalisado, caminhoTotalBT)
             caminho.pop(len(caminho)-1)
             conjuntoArestaNoDestino = listaSUP[item-1]
             isArestas = True
             backTrack = True
             arestaOrigem = self.selecionandoMenorElemento(verticesNpercorridos, caminho)
          else:
           caminhoVerticeRevert.remove(item)
           caminhoVerticeRevert.insert(contador, -1)
           caminhoVertice.remove(item)
           caminho.pop(len(caminho)-1)
           contador = contador + 1
        if not isArestas:
          # Testou tudo desse ramo inicial, e não encontrou nada
          # Retornar -10 para testar outra ramificacao da raiz (origem)
          return []
      
      
      
      self.testarCiclodeVoltaRemove(listaSUP, arestaOrigem)
      conjuntoArestaNaOrigem = conjuntoArestaNoDestino
      # Testar se vertices ajc tem caminho para o vertice desejado, se tiver pula o back track, e seleciona esta aresta
      isVerticeAdj = self.analisarVerticesAdj(conjuntoArestaNoDestino,verticeDestino)
      if not backTrack and isVerticeAdj == []:
       if len(conjuntoArestaNaOrigem)>1:
         verticesNVisitados = []
         verticesNVisitados = self.selecionarVerticeNaoVisitado(conjuntoArestaNaOrigem, caminhoVertice)
         if verticesNVisitados != []:
           conjuntoNPercorridos = self.selecionarMenorElementoNaoPercorrido(verticesNVisitados, caminhoTotalBT)
           arestaOrigem = self.selecionandoMenorElemento(conjuntoNPercorridos, caminho)
         else: 
          conjuntoNPercorridos = self.selecionarMenorElementoNaoPercorrido(conjuntoArestaNaOrigem, caminhoTotalBT)
          arestaOrigem = self.selecionandoMenorElemento(conjuntoNPercorridos, caminho)
       else:
         conjuntoNPercorridos = self.selecionarMenorElementoNaoPercorrido(conjuntoArestaNaOrigem, caminhoTotalBT)
         arestaOrigem = self.selecionandoMenorElemento(conjuntoNPercorridos, caminho)
      
      
      if len(arestaOrigem)>0 or isVerticeAdj != []:
       if arestaOrigem[1] == verticeDestino or isVerticeAdj != []:
         if isVerticeAdj != []:
           caminho.append(isVerticeAdj)
         else:
           caminho.append(arestaOrigem)
        #  funcao para inverter arestas no caminho percorido
         self.inverterCaminhoPercorrido(listaSUP, caminho)
         return caminho
      else:
        # Não precisou fazer backtrack pq o grafo era um ciclo mas ficou vazio
        return []  

  # ---
  # Funcao principal que vai organizar a chamada de busca até encontrar o vertice destino
  # Aqui irá testar até que não exista mais aresta saindo da origem, ou não tiver mais encontrando o resultado
  # Quando ele sair de um ramo e não encontrar o resultado ele pula para o outro ramo/vertice adjacente.
  # ---
  def searchPrincipal(self, m, origem, destino):
    lVertices = m[origem-1].copy()
    lVertices.sort()
    pAdj = []    
    resp = []
    caminhosPercorridos = []
    cont = 0
    while(len(lVertices) > 0 and cont < len(lVertices)):
     pAdj = self.analisarVerticesAdj(lVertices, destino)
     if pAdj == []:
      resp = self.buscaA(m, lVertices[cont], destino)
     if resp != [] or pAdj != []:
       if resp != [] and pAdj == []:
        lVertices.remove(resp[0])
        caminhosPercorridos.append(resp.copy())
        resp.clear()
       if resp == [] and pAdj != []:
         l = []
         l.append(pAdj.copy())
         lVertices.remove(l[0])
         self.inverterCaminhoPercorrido(m, l)
         caminhosPercorridos.append(l.copy())
         l.clear()
         pAdj.clear()
     else:
       cont = cont + 1
    
    return caminhosPercorridos
  