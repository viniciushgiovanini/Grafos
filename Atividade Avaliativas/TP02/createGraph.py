
class criarG:
  
  def gerarMatrizPrinci(self, qtddeK):
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