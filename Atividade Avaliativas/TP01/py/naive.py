class naivePonte:
  def descobrirPonteFlury(self, lista):
    isGrauzero = False
    if len(lista)==1:
      isGrauzero = True
    return isGrauzero
  
  def selecionandoMenorElemento(self, lista):
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
  
  def pegarProxElementoGrauM(self, lista, listaSUP):
    # Ele não está apagando o elemento de grau menor da lista.
    maiorQtdGrau = 0
    qtdElementosLista = len(lista)
    resp = []
    for item in lista:
      destino = item[1]
      qtdGrauDestino = len(listaSUP[destino-1])
      if (qtdGrauDestino >= maiorQtdGrau) and not(self.descobrirPonteFlury(listaSUP[item[1]-1])):
        if qtdGrauDestino > maiorQtdGrau:
          resp = []
          resp.append(item) 
        else:
         resp.append(item)
        maiorQtdGrau = qtdGrauDestino
    if len(resp) == qtdElementosLista:
      resp = self.selecionandoMenorElemento(lista)
    else:
      resp = self.selecionandoMenorElemento(resp)
    return resp 
         
  
    
  
  def selecionarProximoCaminho(self, inicio, listaSup):
    # naive = naivePonte()
    inicio2 = inicio.copy()
    # isPonte = True
    menorValor = list(self.pegarProxElementoGrauM(inicio2, listaSup))
    self.testarCiclodeVolta(listaSup, menorValor)
    # while isPonte:
      # menorValor = list(self.pegarProxElementoGrauM(inicio2, listaSup))
      # pegarValornaListona = listaSup[menorValor[1]-1]
      # isPonte = naive.descobrirPonteFlury(pegarValornaListona)
      # self.testarCiclodeVolta(listaSup, menorValor)
      # if isPonte:
      #   inicio2.remove(menorValor)
           
    return menorValor