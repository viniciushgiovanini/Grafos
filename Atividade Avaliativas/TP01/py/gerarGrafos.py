#imports
import random


class criarGrafos:
  
  def criarEulerianos(self,tamReq):
   cont = 0
   while cont < tamReq:
    valor = random.randint(1, tamReq+1)
    print(valor) 
    if cont == tamReq:
     return valor
    else:
     cont = cont + 1
   pass
  def criarSemiEulerianos():
    pass
  def criarNaoEulerianos(self,tamReq):
    pass   
  
