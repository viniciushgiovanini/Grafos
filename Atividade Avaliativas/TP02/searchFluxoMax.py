# Aluno: Vinícius Henrique Giovanini

from copy import deepcopy

class buscaFluxo:
  
  # Funcoes de apoio da pesquisa
  
  # ---
  # Essa funcao recebe uma lista contendo varias arestas com origem e destino, e seleciona o destino
  # de menor valor.
  # ---
  def selecionandoMenorElemento(self, lista):
    resp = 10000000000000
    listaResposta = []
    for item in lista:
     if item[1] < resp:
      resp = item[1]
      listaResposta = item.copy()
    return listaResposta
  
  # ---
  # Essa duas funcoes abaixo pega o elemento que foi percorrido por exemplo 1-->2 e a primeira,
  # testarCiclodeVoltaRemove remove o elemento de volta na matriz principal no caso o 2 --> 1,
  # a funcao testarCiclodeVoltaRemovenaListComum, simplemente retorna se esse elemento existe.
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
      
  def testarCiclodeVoltaRemovenaListComum(self, lista, valor):
    valor2 = valor.copy()
    destino = valor[1]
    tmp1 = valor[0]
    valorDestino = lista
    valor2[0] = destino
    valor2[1] = tmp1
    
    for item in valorDestino:
     if item == valor2:
      lista.remove(valor2)     
    return lista
   
   
  # ---------------------------------------X-----------------------------------
  # Funcoes principais da pesquisa
  # ---
  # Verifica se o vertice ja foi percorrido.
  # ---
  def verificarSeJaFoiPercorrido(self, lista, valor):
    resp = False
    if len(lista)==0:
      return resp
    else:
     for item in lista:
      if item == valor:
        resp = True
        return resp
    return resp 
  
  
  
  # ---
  # funcao para remover elemento percorrido
  # ---
  def removerElementoPercorrido(self,listaSupreme, arestaOrigem):
    destino = arestaOrigem[0]-1
    listaSupreme[destino].remove(arestaOrigem)
  
  # ---
  # Remove elemento de volta
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
  
  # ---
  # Verifica a existencia de um certo valor na lista de destinos de um vertice.
  # ---
  def verificarExistencia(self, lista, valor):
    for item in lista:
      if item[0] == valor:
        return item
    return []
  
  # ---
  # Essa e a funcao que vai realizar a navegacao até encontrar o vértice desejado ou percorrer todos os vértices.
  # ---
  def buscaA(self, listaSUP, arestaOrigem, verticeDestino):
    loop = True
    # vertices ja percorridos
    caminhoVertice = []
    # Caminho percorido
    caminho = []
    conjuntoArestaNaOrigem = listaSUP[arestaOrigem[0]-1]
    while loop:
      destino = arestaOrigem[1]
      conjuntoArestaNoDestino = listaSUP[destino-1]
      self.removerElementoPercorrido(listaSUP, arestaOrigem)
      caminho.append(arestaOrigem)
      caminhoVertice.append(arestaOrigem[0])
      
      if len(conjuntoArestaNoDestino)==0:
        isArestas = False
        contador = 0
        # Tem que inverter o vetor aqui
        caminhoVerticeRevert = caminhoVertice.copy()
        caminhoVerticeRevert.reverse()
        for item in caminhoVerticeRevert:
         if not isArestas:
          arestasDoVerticeAnalisado = listaSUP[item-1]
          if len(arestasDoVerticeAnalisado)>0:
            caminhoVertice.remove(item)
            caminho.pop(len(caminho)-1)
            conjuntoArestaNoDestino = listaSUP[item-1]
            isArestas = True
          else:
           caminhoVerticeRevert.remove(item)
           caminhoVerticeRevert.insert(contador, -1)
           caminhoVertice.remove(item)
           caminho.pop(len(caminho)-1)
           contador = contador + 1
        if not isArestas:
          # Testou tudo desse ramo inicial, e não encontrou nada
          # Retornar -10 para testar outra ramificacao da raiz (origem)
          return -10
        
      
      
      
      self.testarCiclodeVoltaRemove(listaSUP, arestaOrigem)
      conjuntoArestaNaOrigem = conjuntoArestaNoDestino
      arestaOrigem = self.selecionandoMenorElemento(conjuntoArestaNaOrigem)
      
      
      
      
      if arestaOrigem[1] == verticeDestino:
        self.removerElementoPercorrido(listaSUP, arestaOrigem)
        caminho.append(arestaOrigem)
        return caminho
    pass
  
  # ---
  # Essa funcao vai ser responsavel por variar a base da pesquisa, entao ela vai cudar as arestas do vértice raiz
  # ---
  def proxElemento(self, listaINICIAL, M, verticeDestino):
    # Tem que fazer uma busca em largura para descobrir se é ponte ou não.
    listaINICIALCOPY = listaINICIAL.copy()
    listaINICIALCOPY.sort()
    for item in listaINICIALCOPY:
     resp = self.buscaA(M, item, verticeDestino)
     if resp != []:
       return resp
   
   
  # ---
  # Funcao principal que vai organizar a chamada de busca até encontrar o vertice destino
  # ---
  def searchPrincipal(self, m, origem, destino):
    loop = True
    lVertices = m[origem-1]
    menorElementoRaiz = self.selecionandoMenorElemento(lVertices)
    resp = self.buscaA(m, menorElementoRaiz, destino)
  