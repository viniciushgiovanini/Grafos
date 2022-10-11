#imports
import random
import os

class criarGrafos:

  #funcoes globais  
  #------------------------------------------
  #funcoes do grafo Euleriano  
  
  def verificarARQGrafofEuleriano(self):
    resp = False
    caminho = 'data/grafosEulerianos.txt'
    if (os.path.exists(caminho)):
      resp = True
    return resp
  
  
  def gerarVerticesEulerianos(self, cont, qtd, obj, listaRR):
    cont2 = 0
    
    while(cont2 < qtd):
      # Salvar cont no arquivo e numero sorteado
      if len(listaRR) != 0: 
       destinoAresta = listaRR[0]
       listaRR.remove(destinoAresta)
      else:
       destinoAresta = 1
    
      marcadorLaco = False
      if destinoAresta == cont:
        marcadorLaco = True
        qtd = qtd + 1
        
       
       
      
      if not marcadorLaco:
       stringMontada = str(cont) + " " + str(destinoAresta)
       obj.write(stringMontada + "\n")  
      
      stringMontada = ""     
      cont2 = cont2 + 1
    # listaRR = []  
      
    
      



  def criarEulerianos(self,tamReq):
    
    # Verificar se o arquivo existe
    arquivoExiste = self.verificarARQGrafofEuleriano()
    
    if (arquivoExiste == False):
      oPP = open("data/grafosEulerianos.txt", 'wb+')
      oPP.close()
    else:
      open("data/grafosEulerianos.txt", 'w').close()
            
    
    obj = open("data/grafosEulerianos.txt", 'r+')
    
    
    
    cont = 1
    #  qtd = random.randrange(1, 11, 2)
    qtd = 2
    if tamReq == 1000:
     qtd = 4
    else:
     if tamReq == 1000000:
      qtd = 2
    
    # referente as duas linhas salvas la em cima
    qtdLinhas = 2 + (qtd * int(tamReq))
    obj.write(str(tamReq) + "_" + str(qtdLinhas) + "\n")
        
    listaRR = []
    listaRang = range(1, tamReq+1)
    for item in listaRang:
     listaRR.append(item)
     listaRR.insert(0,item)
    
    random.shuffle(listaRR)
    
    
    
    while cont <= tamReq:
     self.gerarVerticesEulerianos(cont, qtd, obj, listaRR)     
     cont = cont + 1
    
    
    obj.close()  
  
  # def criarSemiEulerianos():
  #   pass
  # def criarNaoEulerianos():
  #   pass   
  
