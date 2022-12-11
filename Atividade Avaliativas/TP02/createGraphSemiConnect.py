import os

class criarGAC:
  
  # Essa funcao tem como objetivo criar um grafo que o seu primeiro vértice
  # conecta com todo mundo, mas o segundo conecta em todo mundo menos o primeiro
  # dessa forma o último não vai conectar com ninguem, só receber arestas de todos.
  
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
  
  def salvarMatrizArquivo(self, m, qtdVertices, nomeArq):
    strInterpolacao = 'db/' + nomeArq + '.txt'
    arquivoExiste = self.isPath(strInterpolacao)   

    if (arquivoExiste == False):
      oPP = open(strInterpolacao, 'wb+')
      oPP.close()
    else:
      open(strInterpolacao, 'w').close()
    obj = open(strInterpolacao, 'r+')
    
    number = qtdVertices -1
    valorSub = 0
    contC = qtdVertices - 1
    while contC > 0:
      valorSub = valorSub + number  
      number = number -1
      contC = contC - 1
     
    linhaum = str(int(qtdVertices)) + " " + str(int((valorSub)+1)) + "\n"
    obj.write(linhaum)
    self.realizarSalvemento(m, obj)
  
  def gerarMatrizGAC(self,m, qtdVertices):
   cont = 1
   aresta = []
   Adj = []
   listaDestino = []
   while cont <= qtdVertices:
     listaDestino.append(cont)
     cont = cont + 1
   
   cont = 1
   while cont <= qtdVertices:
     for item in listaDestino:
      if cont != item:
        aresta.append(cont)
        aresta.append(item)
        Adj.append(aresta.copy())
        aresta.clear()
     m.append(Adj.copy())
     listaDestino.remove(cont)
     Adj.clear()
     cont = cont + 1
   return m
  
  def gerarMatrizPrinciGAC(self, qtdVertices, nomeArq):
    m = []
    m = self.gerarMatrizGAC(m, qtdVertices)
    self.salvarMatrizArquivo(m, qtdVertices, nomeArq)
    
  