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
  
  def testarCiclodeVoltaResp(self, listaSup, valor):
    valor2 = valor.copy()
    destino = valor[1]
    tmp1 = valor[0]
    valorDestino = listaSup[destino-1]
    valor2[0] = destino
    valor2[1] = tmp1
    resp = False
    for item in valorDestino:
     if item == valor2:
      resp = True
    return resp
 
  def selecionarProximoCaminho(self, inicio, listaSup):
    inicio2 = inicio.copy()
    isPonte = False
    loop = True
    while loop:
     menorValor = list(self.selecionandoMenorElemento(inicio2))
     destino = menorValor[1]
     isPonte = self.descobrirPonteFlury(listaSup[destino-1])
     if isPonte == False:
       self.testarCiclodeVoltaRemove(listaSup, menorValor)
       loop = False
     else:
       inicio2.pop(0)
    return menorValor 
    
    
   