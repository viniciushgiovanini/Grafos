import os

class criarGAC:
  
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
     
     
    linhaum = str(int(qtdVertices)) + " " + str(int((qtdVertices * (qtdVertices-1))+1)) + "\n"
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
     Adj.clear()
     cont = cont + 1
   return m
  
  def gerarMatrizPrinciGAC(self, qtdVertices, nomeArq):
    m = []
    m = self.gerarMatrizGAC(m, qtdVertices)
    self.salvarMatrizArquivo(m, qtdVertices, nomeArq)
    print("A")
  