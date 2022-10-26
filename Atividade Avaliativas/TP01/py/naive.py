from copy import deepcopy


class naivePonte:
  
  def inverterElemento(self, element):
    temp0= element[0]
    temp1 = element[1]
    valorNew = element.copy()
    valorNew[0] = temp1
    valorNew[1] = temp0
    return valorNew
  
  def buscaProf(self, valor,l,  listaSup):
   loop = True
   lLimpo = l
   b = deepcopy(listaSup)
   while loop:
    newValor = self.selecionandoMenorElemento(lLimpo) 
    l = b[newValor[1]-1] 
    if len(l)>1:
      lLimpo = self.testarCiclodeVoltaRemovenaListComum(l, newValor)
      if newValor[1] == valor[0]:
        return False
      else:
        b[newValor[0]-1].remove(newValor)
    else:
      return True    
      
  def descobrirPonteFlury(self, valor, listaSup):
    # Esse método é responsável por selecionar as arestas do vertice escolhido e mandar para busca em largura tentar
    # chegar nele mesmo, caso caonsiga não precisa testar com os outros
    isPonte = False
    deslocalmentoInicial = listaSup[valor[1]-1]    
    l = self.testarCiclodeVoltaRemovenaListComum(deslocalmentoInicial, valor)
    tamL = len(l)
    cont = 0
    loop = True
    while loop:
      resp = self.buscaProf(valor, l, listaSup)
      if resp == False:
        return False
      elif cont == tamL: 
        return True
      else:
        l.remove(self.selecionandoMenorElemento(deslocalmentoInicial))
        cont = cont + 1
    
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