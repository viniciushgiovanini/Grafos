from copy import deepcopy

class naivePonte:
  
  # Funcoes de apoio do naive
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
  
  # ---------------------------------------X-----------------------------------
  # Funcoes principais do naive
  
  def buscaLargura(self, item, listaSUP):
    # Tem que fazer uma busca em largura para descobrir se é ponte ou não.
    pass
          
  def selecionarProximoCaminho(self, inicio, listaSup):
    # Essa funcao tem que testar todos os caminhos
    inicio2 = inicio.copy()
    for item in inicio2:
      isPonte = self.buscaLargura(item, listaSup)  
      if not isPonte:
        self.testarCiclodeVoltaRemove(listaSup, item)
        return item
      if isPonte:
        # Caso exista ponte continua o loop com outro valor/item
        pass