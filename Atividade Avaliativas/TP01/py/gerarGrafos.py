#imports
import random
import os
from naive import naivePonte
import math
class criarGrafos:

  #funcoes globais 
  def isPath(self, caminho):
    resp = False
    if (os.path.exists(caminho)):
      resp = True
    return resp 
  
  def salvarMatrizEmArquivo(self, m, obj):
    for inicio in m:
     for item in inicio:
      stringMontada = str(item[0]) + " " + str(item[1])
      obj.write(stringMontada + "\n") 
  
  #------------------------------------------
    
  def verificarselecionarElemento(self, listaElementosSelecionados, valor):
    tam = len(listaElementosSelecionados)
    if tam == 0 :
      return False
    else:
      for item in listaElementosSelecionados:
       if item == valor:
         return True
    return False
  
  def selecionarElemento(self, listaRR, grau, valorOrigem):
    cont = 0
    contadorLista = 0
    listadosDoisValores = []
    marcador = False
    listaElementosSelecionados = []

    while cont < (grau-1) or marcador:
      elementoLista = listaRR[contadorLista]
      
      if elementoLista != valorOrigem and not self.verificarselecionarElemento(listaElementosSelecionados, elementoLista):
        l = []
        l.append(valorOrigem)
        l.append(elementoLista)
        listadosDoisValores.append(l)
        listaRR.remove(elementoLista)
        marcador = False
        listaElementosSelecionados.append(elementoLista)
      else:
        contadorLista = contadorLista + 1
        marcador = True
        
            
      cont = cont + 1
    
    return listadosDoisValores  
   
  def gerarMatrizdeSalvamento(self, matrizSalvamento, elementos):
  # 1 3 | 1 5
    n = naivePonte()    
    for item in elementos:
     destinoPrincipal = item[0]-1
     destinoSecundario = item[1]-1
     
     testarNone = matrizSalvamento[destinoPrincipal]
     testarNone2 = matrizSalvamento[destinoSecundario]
     if testarNone == None:
       listaEmp = []
       matrizSalvamento[destinoPrincipal] = listaEmp.copy()
       matrizSalvamento[destinoPrincipal].append(item) 
     else:
       matrizSalvamento[destinoPrincipal].append(item) 
     if testarNone2 == None:
      listaEmp = []
      matrizSalvamento[destinoSecundario] = listaEmp.copy()
      invertItem = n.inverterElemento(item)
      matrizSalvamento[destinoSecundario].append(invertItem)
     else:
       invertItem = n.inverterElemento(item)
       matrizSalvamento[destinoSecundario].append(invertItem)
    
  def criarEulerianos(self,tamReq, nomeArq):
    
    # Verificar se o arquivo existe
    strInterpolacao = 'data/' + nomeArq + '.txt'
    arquivoExiste = self.isPath(strInterpolacao)   

    if (arquivoExiste == False):
      oPP = open(strInterpolacao, 'wb+')
      oPP.close()
    else:
      open(strInterpolacao, 'w').close()

    obj = open(strInterpolacao, 'r+')
    #  grau = random.randrange(1, 11, 2)
    grau = 2
    # referente as duas linhas salvas la em cima
    # qtdLinhas = 1 + ((grau * int(tamReq)) - (((grau-(grau2))) * int(tamReq/(tamReq/10))))
    qtdLinhas = 1 + ((grau * int(tamReq)))
    obj.write(str(tamReq) + "_" + str(qtdLinhas) + "\n")
    
    listaRR = []
    listaRang= range(1, tamReq+1)
    for item in listaRang:
     listaRR.append(item)
    
    matrizSalvamento = [None] * (tamReq)

    cont = 1
    while cont < tamReq:
      if cont == tamReq:
        grau = grau -1
      
      
      for item in listaRR:
        if item == cont:
          listaRR.remove(cont)
      
      elementos = self.selecionarElemento(listaRR, grau, cont)
    
      self.gerarMatrizdeSalvamento(matrizSalvamento, elementos)     
      
      if cont == (tamReq-1):
        n = naivePonte()  
        ulitmoElemento = []
        ulitmoElemento.append(1)
        ulitmoElemento.append(cont+1)
        matrizSalvamento[0].append(ulitmoElemento)
        ulitmoElementoInvert = n.inverterElemento(ulitmoElemento)
        matrizSalvamento[tamReq-1].append(ulitmoElementoInvert)
        
        
      cont = cont + 1
    
    self.salvarMatrizEmArquivo(matrizSalvamento, obj)    
    
    obj.close()  

  #------------------------------
  # grafo Nao euleriano
  def criarNaoEulerianos(self, qtdVertice, nomeArq):
    # Verificar se o arquivo existe
    strInterpolacao = 'data/' + nomeArq + '.txt'
    arquivoExiste = self.isPath(strInterpolacao)   
        
    
    if (arquivoExiste == False):
      oPP = open(strInterpolacao, 'wb+')
      oPP.close()
    else:
      open(strInterpolacao, 'w').close()
            
    
    obj = open(strInterpolacao, 'r+')
    
    
    
    
    grau = 2
    # referente as duas linhas salvas la em cima
    # qtdLinhas = 1 + ((grau * int(tamReq)) - (((grau-(grau2))) * int(tamReq/(tamReq/10))))
    qtdLinhas = 1 + ((grau * int(qtdVertice)+3))
    obj.write(str(qtdVertice) + "_" + str(qtdLinhas) + "\n")
    
    listaRR = []
    listaRang= range(1, qtdVertice+1)
    for item in listaRang:
     listaRR.append(item)
    
    matrizSalvamento = [None] * (qtdVertice)

    cont = 1
    while cont < qtdVertice:
      if cont == qtdVertice:
        grau = grau -1
      
      
      for item in listaRR:
        if item == cont:
          listaRR.remove(cont)
      
      elementos = self.selecionarElemento(listaRR, grau, cont)
    
      self.gerarMatrizdeSalvamento(matrizSalvamento, elementos)     
      
      if cont == (qtdVertice-1):
        n = naivePonte()  
        ulitmoElemento = []
        ulitmoElemento.append(1)
        ulitmoElemento.append(cont+1)
        matrizSalvamento[0].append(ulitmoElemento)
        ulitmoElementoInvert = n.inverterElemento(ulitmoElemento)
        matrizSalvamento[qtdVertice-1].append(ulitmoElementoInvert)
      if cont == 1 or cont == 2:
        n = naivePonte()  
        ulitmoElemento = []
        ulitmoElemento.append(cont)
        elementoDest = math.floor(qtdVertice/2)
        ulitmoElemento.append(elementoDest)
        matrizSalvamento[cont-1].append(ulitmoElemento)
        ulitmoElementoInvert = n.inverterElemento(ulitmoElemento)
        matrizSalvamento[elementoDest] = [] 
        matrizSalvamento[elementoDest].append(ulitmoElementoInvert)   
        
      cont = cont + 1
    
    self.salvarMatrizEmArquivo(matrizSalvamento, obj)
    
    
    obj.close()
    
  #-------------------------------
  #grafo Semi Euleriano
  def criarSemiEulerianos(self, qtdVertice, nomeArq):
  # Verificar se o arquivo existe
    strInterpolacao = 'data/' + nomeArq + '.txt'
    arquivoExiste = self.isPath(strInterpolacao)   
        
    
    if (arquivoExiste == False):
      oPP = open(strInterpolacao, 'wb+')
      oPP.close()
    else:
      open(strInterpolacao, 'w').close()
            
    
    obj = open(strInterpolacao, 'r+')
    
    grau = 2
    # referente as duas linhas salvas la em cima
    # qtdLinhas = 1 + ((grau * int(tamReq)) - (((grau-(grau2))) * int(tamReq/(tamReq/10))))
    qtdLinhas = 1 + ((grau * int(qtdVertice))+2)
    obj.write(str(qtdVertice) + "_" + str(qtdLinhas) + "\n")
    
    listaRR = []
    listaRang= range(1, qtdVertice+1)
    for item in listaRang:
     listaRR.append(item)
    
    matrizSalvamento = [None] * (qtdVertice)

    cont = 1
    while cont < qtdVertice:
      if cont == qtdVertice:
        grau = grau -1
      
      
      for item in listaRR:
        if item == cont:
          listaRR.remove(cont)
      
      elementos = self.selecionarElemento(listaRR, grau, cont)
    
      self.gerarMatrizdeSalvamento(matrizSalvamento, elementos)     
      
      if cont == (qtdVertice-1):
        n = naivePonte()  
        ulitmoElemento = []
        ulitmoElemento.append(1)
        ulitmoElemento.append(cont+1)
        matrizSalvamento[0].append(ulitmoElemento)
        ulitmoElementoInvert = n.inverterElemento(ulitmoElemento)
        matrizSalvamento[qtdVertice-1].append(ulitmoElementoInvert)
      if cont == 1:
        n = naivePonte()  
        ulitmoElemento = []
        ulitmoElemento.append(1)
        elementoDest = math.floor(qtdVertice/2)
        ulitmoElemento.append(elementoDest)
        matrizSalvamento[0].append(ulitmoElemento)
        ulitmoElementoInvert = n.inverterElemento(ulitmoElemento)
        matrizSalvamento[elementoDest] = [] 
        matrizSalvamento[elementoDest].append(ulitmoElementoInvert) 
      cont = cont + 1
    
    self.salvarMatrizEmArquivo(matrizSalvamento, obj) 
    
    
    obj.close()   
  
