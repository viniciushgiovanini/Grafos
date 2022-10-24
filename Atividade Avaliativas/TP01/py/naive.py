class naivePonte:
  def descobrirPonteFlury(self, lista):
    isGrauzero = False
    if len(lista)==1:
      isGrauzero = True
    return isGrauzero
  
  def selecionandoMenorElemento(self, lista):
    # Tem que pegar o vértice com maior numero de arestas e se for igual faz isso aqui
    resp = 10000000000000
    listaResposta = []
    for item in lista:
     if item[1] < resp:
      resp = item[1]
      listaResposta = item.copy()
    return listaResposta
  
 
  def testarCiclodeVolta(self, listaSup, valor):
    valor2 = valor.copy()
    destino = valor[1]
    tmp1 = valor[0]
    valorDestino = listaSup[destino-1]
    valor2[0] = destino
    valor2[1] = tmp1
    
    for item in valorDestino:
     if item == valor2:
      listaSup[destino-1].remove(valor2)      
  
  def selecionarProximoCaminho(self, inicio, listaSup):
    naive = naivePonte()
    inicio2 = inicio.copy()
    isPonte = True
    
    while isPonte:
      menorValor = list(self.selecionandoMenorElemento(inicio2))
      pegarValornaListona = listaSup[menorValor[1]-1]
      isPonte = naive.descobrirPonteFlury(pegarValornaListona)
      self.testarCiclodeVolta(listaSup, menorValor)
      if isPonte:
        inicio2.remove(menorValor)
           
    return menorValor