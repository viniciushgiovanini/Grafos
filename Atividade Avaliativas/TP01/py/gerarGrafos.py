#imports
import random
class criarGrafos:
    
  #funcoes do grafo Euleriano
  def gerarValoresEulerianos(self, tamReq):
   valorrr = random.randint(1, tamReq+1)
   return valorrr
  
  
  
  def criarEulerianos(self,tamReq):
    cont = 0
    while cont < tamReq:
     valor = criarGrafos.gerarValoresEulerianos(self, tamReq) 
     if cont == tamReq:
      return valor
     else:
      cont = cont + 1
  
  # def criarSemiEulerianos():
  #   pass
  # def criarNaoEulerianos():
  #   pass   
  
