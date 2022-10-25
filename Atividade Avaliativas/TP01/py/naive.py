class naivePonte:
  
  def inverterElemento(self, element):
    temp0= element[0]
    temp1 = element[1]
    valorNew = element.copy()
    valorNew[0] = temp1
    valorNew[1] = temp0
    return valorNew
  
  def descobrirPonteFlury(self, valor, listaSup):
    # Ta quase funcionando, só que para descobrir que é ponte eu tenho que navegar ate 
    # o caminho verificar se tem o caminho de volta e verificar se o tamanho da lista é 0
    # Até agora eu consigo ir na lista e verificar se é 0 mas não consigo se tiver um caminho maior.
    
    
    isPonte = False
    valorInvert = self.inverterElemento(valor)
    destino = valor[1]
    tamLista = (len(listaSup[destino-1]))
    if  (tamLista == 0) or (tamLista)==1:
      isPonte = True
    elif tamLista> 1:
      temInvert = False
      tamReal = (len(listaSup[destino-1]))
      for item in listaSup[destino-1]:
        if item == valorInvert:
          temInvert = True
      if temInvert:
        tamReal = tamReal -1
      
      if tamReal == 0:
        isPonte = True
        
         
    return isPonte
  
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
     isPonte = self.descobrirPonteFlury(menorValor, listaSup)
     if isPonte == False:
       self.testarCiclodeVoltaRemove(listaSup, menorValor)
       loop = False
     else:
       inicio2.pop(0)
    return menorValor 
    
    
   