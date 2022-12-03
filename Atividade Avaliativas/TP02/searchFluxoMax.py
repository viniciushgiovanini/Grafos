# Aluno: Vinícius Henrique Giovanini

from copy import deepcopy

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
  
  # PAREI AQUI DIA 03 DE MADRUGS, EU TENHO QUE FAZER AGORA ELE NÃO TESTAR O CAMINHO DE VOLTA NA VARIAVEL ARESTASDOVERTICEANALISADO
  # E QUANDO DER CERTO E ELE ACHAR UMA ARESTA PARA CONTINUAR EU TENHO QUE FAZER A MESMA COISA PARA EVITAR QUE ELE VOLTE POR
  # UM CAMINHO JA PERCORRIDO.
  
  
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
        listaSUP[arestaOrigem[0]-1].append(arestaOrigem.copy())
        caminhoVerticeRevert = caminhoVertice.copy()
        caminhoVerticeRevert.reverse()
        for item in caminhoVerticeRevert:
         if not isArestas:
          arestasDoVerticeAnalisado = listaSUP[item-1]
          if len(arestasDoVerticeAnalisado)>1:
            if not item in caminhoVertice:
             caminhoVertice.remove(item)
             caminho.pop(len(caminho)-1)
             conjuntoArestaNoDestino = listaSUP[item-1]
             isArestas = True
          else:
           elementoInvertido = self.inverterElemento(arestasDoVerticeAnalisado[0])
           listaSUP[elementoInvertido[0]-1].append(elementoInvertido)
           listaSUP[arestasDoVerticeAnalisado[0][0]-1].remove(arestasDoVerticeAnalisado[0])
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
      elementoInvertido = self.inverterElemento(arestaOrigem)
      arestaOrigem = self.selecionandoMenorElemento(conjuntoArestaNaOrigem, caminho)
      listaSUP[elementoInvertido[0]-1].append(elementoInvertido)
      
      if len(arestaOrigem)>0:
       if arestaOrigem[1] == verticeDestino:
        #  self.removerElementoPercorrido(listaSUP, arestaOrigem)
         caminho.append(arestaOrigem)
         elementoInvertido = self.inverterElemento(arestaOrigem)
         listaSUP[elementoInvertido[0]-1].append(elementoInvertido)
         self.removerElementoPercorrido(listaSUP, arestaOrigem)
         return caminho
      else:
        # Não precisou fazer backtrack pq o grafo era um ciclo mas ficou vazio
        return []  

  # ---
  # Funcao principal que vai organizar a chamada de busca até encontrar o vertice destino
  # ---
  def searchPrincipal(self, m, origem, destino):
    lVertices = m[origem-1]
    lVertices.sort()
    caminhosPercorridos = []
    while(len(lVertices)>0):
     resp = self.buscaA(m, lVertices[0], destino)
     if resp != []:
       caminhosPercorridos.append(resp.copy())
       resp.clear()
    
    print("teste")
  