import os
class criarG:
  
  # ---
  # isPath recebe o caminho do arquivo e testa se ele existe ou nao retornando True or False.
  # ---
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
     
     qtdLinhas =  (qtdVertices*3) + ((qtdVertices/4)-1)
     
     linhaum = str(int(qtdVertices)) + " " + str(int(qtdLinhas)+1) + "\n"
     obj.write(linhaum)
     self.realizarSalvemento(m, obj)
   
  def gerarMatrizPrinci(self, qtddeK, nomeArq):
    m = []
    verticesAdj = []
    contador = 0
    listaVertices = []
    contGerar = 1
    vet = []
    while contGerar <= qtddeK*4:
      vet.append(contGerar)
      if (contGerar%4)==0:
        listaVertices.append(vet.copy())
        vet.clear()
      contGerar = contGerar + 1
        
        
        
    
    while contador < qtddeK:
      
      if contador > 0:
       tam = len(m)
       arestaConexao = []
       arestaConexao.append(len(m))
       arestaConexao.append(item+1)
       m[tam-1].append(arestaConexao.copy())       
             
      for item in listaVertices[contador]:
      
        
       verticesAdj.clear()
       arestaOrigem = []
       listaDestino = listaVertices[contador].copy()
       listaDestino.remove(item)
       cont=0
       while(cont<3):
        arestaOrigem.append(item)
        arestaOrigem.append(listaDestino[0])
        verticesAdj.append(arestaOrigem.copy())
        listaDestino.pop(0)
        arestaOrigem.clear()
        cont = cont +1
       m.append(verticesAdj.copy())
        
 
      contador = contador + 1   
       
    if len(m)>0:
      self.salvarMatrizArquivo(m, qtddeK*4, nomeArq)