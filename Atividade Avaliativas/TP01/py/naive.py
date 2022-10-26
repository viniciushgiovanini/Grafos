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
  
  def buscaA(self, destino, listaSUP, arestaOrigem):
    # TA FUNCIONANDO, SÓ TA DANDO O ERRO POIS QUANDO ELE TESTA TODOS OS MENORES E CHEGA EM LUGAR NENHUM ELE DA PAU, TEM
    # QUE FAZER ELE VOLTAR E SELECIONAR OUTRO CAMINHO DESDE O INICIO
    l = deepcopy(listaSUP)
    arestaOrigemCOPY = arestaOrigem[0]
    lDESTINO2 = l[destino-1].copy()
    lDESTINO2 = self.testarCiclodeVoltaRemovenaListComum(l[destino-1].copy(),arestaOrigem)
    podePegarDestino = True
    listaJaPercorrigos = []
    while len(lDESTINO2)>0:
     if podePegarDestino:
        lDESTINO = l[destino-1]
     lDESTINO = self.testarCiclodeVoltaRemovenaListComum(lDESTINO,arestaOrigem)

     jaPercorrido = True
     while jaPercorrido and (len(lDESTINO)>0):
       menorElemento = self.selecionandoMenorElemento(lDESTINO)
       jaPercorrido = self.verificarSeJaFoiPercorrido(listaJaPercorrigos, menorElemento[1])
       if jaPercorrido:
         lDESTINO.remove(menorElemento)
       else:
         arestaOrigem = menorElemento
     
     
     
     if menorElemento[1] == arestaOrigemCOPY:
       return False
     elif len(lDESTINO) == 0:
      #  ENCONTOU PONTE
       lDESTINO2.remove(arestaOrigem)
       listaJaPercorrigos.remove(arestaOrigem[0])
       lDESTINO = lDESTINO2.copy()
       podePegarDestino = False
     else:
       destino = menorElemento[1]
       
       podePegarDestino = True
       listaJaPercorrigos.append(menorElemento[0])
    return True
  
  def proxElemento(self, listaINICIAL, listaSUP):
    # Tem que fazer uma busca em largura para descobrir se é ponte ou não.
    listaINICIALCOPY = listaINICIAL.copy()
    for item in listaINICIALCOPY:
      if len(listaINICIAL)!=1:
        resp = self.buscaA(item[1], listaSUP, item)
      else:
        resp = False
      if not resp:
        self.testarCiclodeVoltaRemove(listaSUP, item)
        return item
      
     
    