import random
import os
class criarGRD:
  def isPath(self, caminho):
    resp = False
    if (os.path.exists(caminho)):
      resp = True
    return resp 
  
  def realizarSalvemento(self, m, obj):
   for inicio in m:
    for item in inicio:
     stringMontada = str(item[0]) + " " + str(item[1])
     obj.write(stringMontada + "\n") 
  
  def salvarMatrizArquivo(self, m, qtdVertices, nomeArq, qtdLinhas):
     strInterpolacao = 'db/' + nomeArq + '.txt'
     arquivoExiste = self.isPath(strInterpolacao)   

     if (arquivoExiste == False):
       oPP = open(strInterpolacao, 'wb+')
       oPP.close()
     else:
       open(strInterpolacao, 'w').close()
     obj = open(strInterpolacao, 'r+')
     
     
     linhaum = str(int(qtdVertices)) + " " + str(int(qtdLinhas[0])) + "\n"
     obj.write(linhaum)
     self.realizarSalvemento(m, obj)
  
  def deletarElementoLista(self, lista, elemento):
    cont = 0
    anotherList = []
    for item in lista:
      if item != elemento:
        anotherList.append(item)
      cont = cont + 1
    return anotherList 
  
  def gerarMatrizPrinciRD(self, qtdVertices, qtdLinhasReturn):
    m = []
    # grau = qtdVertices
    verticesList = []
    cont = 1
    qtdLinhas = 1
    while cont <= qtdVertices:
      verticesList.append(cont)
      cont = cont + 1
    
    # Realizando multiplicação da lista para gerar os destinos
    cont = 0
    listDestinos = []
    listDestinos = verticesList.copy()
    
    
    # while cont < (grau-1):
    #   listDestinos = listDestinos + listDestinos
    #   cont = cont + 1
    random.shuffle(listDestinos)
    
    vertice = 1
    aresta = []
    destino = listDestinos.copy()
    destino = self.deletarElementoLista(destino,1)
    listAdj = []
    contDestino = 1
    while vertice <= qtdVertices:
      while contDestino < random.randint(2, 10):
        qtdLinhas = qtdLinhas + 1
        aresta.append(vertice)
        valorEscolhido = destino[0]
        aresta.append(valorEscolhido)
        destino = self.deletarElementoLista(destino,valorEscolhido)
        listAdj.append(aresta.copy())
        aresta.clear()
        contDestino = contDestino +1
      m.append(listAdj.copy())
      listAdj.clear()
      contDestino = 1
      destino = listDestinos.copy()
      vertice = vertice + 1
      destino = self.deletarElementoLista(destino,vertice)
    
    qtdLinhasReturn.append(qtdLinhas)
    return m
  
  def princiGerarGraphRand(self,  qtdVertices, nomearq):
    qtdLinhas = []
    m = []
    m = self.gerarMatrizPrinciRD(qtdVertices, qtdLinhas)
    self.salvarMatrizArquivo(m,qtdVertices, nomearq, qtdLinhas)
    
    