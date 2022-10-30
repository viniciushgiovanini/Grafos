# Aluno: Vinícius Henrique Giovanini
# Data: 30/10/2022


from copy import deepcopy

class naivePonte:
  
  # Funcoes de apoio do naive
  
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
  # Funcoes principais do naive
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
  # Verifica a existencia de um certo valor na lista de destinos de um vertice.
  # ---
  def verificarExistencia(self, lista, valor):
    for item in lista:
      if item[1] == valor:
        return item
    return []
  
  def verificarArestaPenultima(self, lista, valores):
    for item2 in lista:
      for item3 in valores:
        if item2[1] == item3[1]:
          return item2
    return []
  # ---
  # Essa e a funcao buscaA que testa sempre pegando o menor elemento se forma um ciclo, garantindo
  # assim se é ponte ou nao, retornando True caso exista ponte no caminho percorrido, e false se conseguir
  # realizar o ciclo.
  # ---
  def buscaA(self, destino, listaSUP, arestaOrigem):
    # TA FUNCIONANDO, SÓ TA DANDO O ERRO POIS QUANDO ELE TESTA TODOS OS MENORES E CHEGA EM LUGAR NENHUM ELE DA PAU, TEM
    # QUE FAZER ELE VOLTAR E SELECIONAR OUTRO CAMINHO DESDE O INICIO
    l = deepcopy(listaSUP)
    arestaOrigemCOPY = arestaOrigem[0]
    lDESTINOORIGINAL = l[arestaOrigem[0]-1].copy()
    lDESTINO2 = l[destino-1].copy()
    lDESTINO2 = self.testarCiclodeVoltaRemovenaListComum(l[destino-1].copy(),arestaOrigem)
    podePegarDestino = True
    listaJaPercorrigos = []
    while len(lDESTINO2)>0:
     
     isAtalho = False  
    
     if podePegarDestino:
        lDESTINO = l[destino-1]
        lDESTINO = self.testarCiclodeVoltaRemovenaListComum(lDESTINO,arestaOrigem)
      
     #  ARRUMAR ESSA FUNCAO, POIS ELA TA VERIFICANDO SÓ O O VERTICE ORIGEM, MAS EU TENHO OS VERTICE QUE CHEGAM NELA
     verificarSeTemNosOutrosVertices = self.verificarExistencia(lDESTINO, arestaOrigemCOPY)

     if len(verificarSeTemNosOutrosVertices)!=0:
        jaPercorrido = False
        menorElemento = verificarSeTemNosOutrosVertices
     else:
       verificarSetemAtalho = self.verificarArestaPenultima(lDESTINO, lDESTINOORIGINAL)
       if len(verificarSetemAtalho)!=0:
         isAtalho = True
         menorElemento = verificarSetemAtalho
       jaPercorrido = True
      
     while (jaPercorrido) and (len(lDESTINO)>0) and (not isAtalho):
       menorElemento = self.selecionandoMenorElemento(lDESTINO)
       jaPercorrido = self.verificarSeJaFoiPercorrido(listaJaPercorrigos, menorElemento[1])
       if jaPercorrido:
         lDESTINO.remove(menorElemento)
       else:
         arestaOrigem = menorElemento
     
     
     
     if (menorElemento[1] == arestaOrigemCOPY) or (isAtalho):
       return 0
     elif len(lDESTINO) == 0:
      #  ENCONTOU PONTE

        if self.verificarExistencia(lDESTINO2, arestaOrigem):
          lDESTINO2.remove(arestaOrigem)
          listaJaPercorrigos.remove(arestaOrigem[0])
          lDESTINO = lDESTINO2.copy()
          podePegarDestino = False
        else:
          loop = True
          cont = len(listaJaPercorrigos)-1
          while loop:
            elemento = listaJaPercorrigos[cont]
            inicio = l[elemento-1]
            if len(inicio)>1:
              lDESTINO2 = inicio.copy()
              menorElemento = self.selecionandoMenorElemento(lDESTINO2)
              l[elemento-1].remove(menorElemento)
              lDESTINO2.remove(menorElemento)
              lDESTINO = lDESTINO2.copy()
              podePegarDestino = False
              loop = False
              listaJaPercorrigos.remove(elemento)
            cont = cont -1
            if cont == -1:
              # Eliminar as ultimas pontes e terminar.
              return 1
        
     else:
       destino = menorElemento[1]
       
       podePegarDestino = True
       listaJaPercorrigos.append(menorElemento[0])
    return 1
  
  # ---
  # Funcao principal da classe, ela pega os vertices destino que foi passado para parametro,
  # e testar se percorrendo o menor elemento é possivel realizar o ciclo, mandando o valor testado,
  # que nao se encontrou o ciclo para a classe fleury adicionar na lista do caminho percorrido.
  # ---
  def proxElemento(self, listaINICIAL, listaSUP):
    # Tem que fazer uma busca em largura para descobrir se é ponte ou não.
    listaINICIALCOPY = listaINICIAL.copy()
    listaINICIALCOPY.sort()
    tamListaInicial = len(listaINICIAL)
    contQtdVerificados = 0
    for item in listaINICIALCOPY:
      if tamListaInicial !=1 and contQtdVerificados != (tamListaInicial-1):
        resp = self.buscaA(item[1], listaSUP, item)
      else:
        resp = 0
      if resp == 0:
        self.testarCiclodeVoltaRemove(listaSUP, item)
        return item
      contQtdVerificados = contQtdVerificados + 1
    if resp == 1:
      itemA = listaINICIALCOPY[len(listaINICIALCOPY)-1]
      return itemA
    