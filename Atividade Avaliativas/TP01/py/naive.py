from copy import deepcopy

class naivePonte:
  
  def inverterElemento(self, element):
    temp0= element[0]
    temp1 = element[1]
    valorNew = element.copy()
    valorNew[0] = temp1
    valorNew[1] = temp0
    return valorNew
  
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
  
  def buscaProfundidade(self, item, listaSUP):
    loop = True
    podeCopiar = True
    destino = item[1]-1
    arestasInicias = listaSUP[destino].copy()
    arestasInicias = self.testarCiclodeVoltaRemovenaListComum(arestasInicias, item)
    while loop:
      if podeCopiar:
        copiaArestasdoVertice = arestasInicias
        copiaArestasdoVertice = self.testarCiclodeVoltaRemovenaListComum(copiaArestasdoVertice, item)
      mv = self.selecionandoMenorElemento(copiaArestasdoVertice)
      if item[0] == mv[1]:
        return False
      elif len(copiaArestasdoVertice)==1:
        return True
      else:
        destino = mv[1]-1       
  
  def selecionarProximoCaminho(self, inicio, listaSup):
    for item in inicio:
      isPonte = self.buscaProfundidade(item, listaSup)  
      if not isPonte:
        self.testarCiclodeVoltaRemove(listaSup, item)
        return item