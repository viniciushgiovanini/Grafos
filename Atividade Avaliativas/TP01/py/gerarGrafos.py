#imports
import random
import os
import pathlib

class criarGrafos:

  #funcoes globais  
  def gerarArestas(self, tamReq):
   valorrr = random.randint(1, tamReq)
   return valorrr 
   
 #------------------------------------------
  #funcoes do grafo Euleriano  
  
  def verificarARQGrafofEuleriano(self):
    resp = False
    caminho = 'data/grafosEulerianos.txt'
    if (os.path.exists(caminho)):
      resp = True
    return resp
  
  
  def gerarVerticesEulerianos(self, cont, qtd, tamReq, obj):
    cont2 = 0
    listaRR = []
    while(cont2 < qtd):
      # Salvar cont no arquivo e numero sorteado
      numeroPresentenaLista = False
      
      while(numeroPresentenaLista == False):
       destinoAresta = self.gerarArestas(tamReq)
       if not destinoAresta in listaRR:
         numeroPresentenaLista = True
         listaRR.append(destinoAresta)
         
       
       
       
      stringMontada = str(cont) + " " + str(destinoAresta)
      obj.write(stringMontada + "\n")
      stringMontada = ""     
      cont2 = cont2 + 1
    listaRR = []  
      
    
      



  def criarEulerianos(self,tamReq):
    
    # Verificar se o arquivo existe
    arquivoExiste = self.verificarARQGrafofEuleriano()
    
    if (arquivoExiste == False):
      oPP = open("data/grafosEulerianos.txt", 'wb+')
      oPP.close()
      
    
    obj = open("data/grafosEulerianos.txt", 'r+')
    
    obj.write(' ' + "\n")
    obj.write(str(tamReq) + "\n")
    
    cont = 1
    #  qtd = random.randrange(1, 11, 2)
    qtd = 2
    if tamReq == 1000:
     qtd = 4
    else:
     if tamReq == 1000000:
      qtd = 20
        
      

    while cont <= tamReq:
     self.gerarVerticesEulerianos(cont, qtd, tamReq, obj)     
     cont = cont + 1
    obj.close()  
  
  # def criarSemiEulerianos():
  #   pass
  # def criarNaoEulerianos():
  #   pass   
  
