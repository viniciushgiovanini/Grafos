#imports
import sys
import os.path

#setando o path
path = './database/'

#Criando a Class
class myVerticeSuce:
  sucessor = None
  vPrinci = None

class myVerticePrede:
  VPrinci = None
  predecessor = None

#Lista variavel Global
myListSucesso = []
myListPredecesso = []
verticeLidoAnterior = None
elementPosiLP = 0
gEntrada = 0
gSaida = 0


#func
def initListas(tamPrede):
  global myListPredecesso 
  myListPredecesso = [None] * (tamPrede-1)

def mudouVertice(rSplit):
  global verticeLidoAnterior
  
  
  if verticeLidoAnterior == None:
    mudou = "notInit"   
    verticeLidoAnterior = rSplit
    return mudou
  elif verticeLidoAnterior == rSplit:
    mudou = False  
    verticeLidoAnterior = rSplit  
    return mudou
  else:
    mudou = True    
    verticeLidoAnterior = rSplit
    return mudou

def predecessorExistente(value):
   resp = False
   valorDaLista = myListPredecesso[value-1]
   if valorDaLista != None:
     resp = True       
   return resp 

def sucessorExistente(value):
  resp = False
  valorDaLista = myListSucesso[value-1]
  if valorDaLista != None:
    resp = True       
  return resp 

def fazerPesquisaCriar(objA, newObj):
  if objA.sucessor == None:
    objA.sucessor = newObj
    return
  else:
    fazerPesquisaCriar(objA.sucessor, newObj)

def fazerPesquisaCriarPred(objA, newObj):
  if objA.predecessor == None:
    objA.predecessor = newObj
    return
  else:
    fazerPesquisaCriarPred(objA.predecessor, newObj)

def criarLista(rSplit):
  global elementPosiLP 
  mudouV = mudouVertice(rSplit[0])

  if mudouV == "notInit":

    #Criando Lista de Sucessores
    raiz = myVerticeSuce()
    suce = myVerticeSuce()
    raiz.vPrinci = rSplit[0]
    
    suce.vPrinci = rSplit[1]
    suce.sucessor = None
    raiz.sucessor = suce
    myListSucesso.append(raiz)    
    
    #Criando Lista de Predecessores
    raizPrede = myVerticePrede()
    prede = myVerticePrede()
    raizPrede.VPrinci = rSplit[1]
    prede.VPrinci = rSplit[0]
    raizPrede.predecessor = prede
    
    #Alocando a lista de predessor na posição desejada da lista
    posi = rSplit[1]
    myListPredecesso.insert(int(posi)-1, raizPrede)   
    
      
  elif mudouV == False:
    suce = myVerticeSuce()
    suce.vPrinci = rSplit[1]        
    tamList = len(myListSucesso)
    objetoAnterior = myListSucesso[tamList-1]
    fazerPesquisaCriar(objetoAnterior, suce)    
  else:
    newRaiz = myVerticeSuce()
    newSuce = myVerticeSuce()
    newRaiz.vPrinci = rSplit[0]
    newSuce.vPrinci = rSplit[1]
    newRaiz.sucessor = newSuce
    myListSucesso.append(newRaiz)
  #Implementar na Lista de Predecessores
  if mudouV != 	"notInit":
      predExist = predecessorExistente(int(rSplit[1]))
      if predExist:
       pred = myVerticePrede()
       pred.VPrinci = rSplit[0]
       fazerPesquisaCriarPred(myListPredecesso[(int(rSplit[1])-1)], pred)
      else:
       newRaiz = myVerticePrede()
       pred = myVerticePrede()
       pred.VPrinci = rSplit[0]
       newRaiz.VPrinci = rSplit[1]
       newRaiz.predecessor = pred
       myListPredecesso[(int(rSplit[1])-1)] = newRaiz

def recPesquisaSuce(objimprimir, sucessores):
  if objimprimir.vPrinci != None:
    if objimprimir.sucessor != None:
      sucessores.append(objimprimir.sucessor.vPrinci)
      recPesquisaSuce(objimprimir.sucessor, sucessores)
  else:
    return
    

def pesquisarVerticeImprimirSucessores(vPesquisa):
   global gEntrada
   objimprimir = myListSucesso[int(vPesquisa)-1]
   sucessores = []
   existSuce = sucessorExistente(int(vPesquisa))
   if existSuce:
     print("Vertice Principal: " + vPesquisa)
     recPesquisaSuce(objimprimir, sucessores)
     print("Sucessores: ")
     for i in sucessores:
      print("[" + i + "]", end='')
     print("")
   else:
      print("Vertice não Existente (Sucessores)")
   gEntrada = len(sucessores)
   

def recPesquisaPred(objimprimir, predecessores):
  if objimprimir.VPrinci != None:
    if objimprimir.predecessor != None:
      predecessores.append(objimprimir.predecessor.VPrinci)
      recPesquisaPred(objimprimir.predecessor, predecessores)
  else:
    return

def pesquisarVerticeImprimirPred(vPesquisa):
   global gSaida
   objimprimir = myListPredecesso[int(vPesquisa)-1]
   Predecessores = []
   existPred = predecessorExistente(int(vPesquisa))
   if existPred:
     recPesquisaPred(objimprimir, Predecessores)
     print("Predecessores: ")
     for i in Predecessores:
      print("[" + i + "]", end='')
     print("")
   else:
      print("Vértice não Existente (Predecessores)")
   gSaida = len(Predecessores) 
   

#Pegando Argumento do Command Line
fileName = sys.argv[1]
dirname = os.path.dirname(path)
verticeInput = sys.argv[2]


# Testa se Tem .txt no campo do nome do arquivo
if ".txt" in fileName:
  pathConcat = dirname + '/' + fileName
else:
  pathConcat = dirname + '/' + fileName + ".txt"

#Leitura do path
with open(pathConcat) as file:
  linha = file.readlines()


print("Processando...")

#Limpa a linha e deixa pronto para utilizar os valores
travaLoop = False
for i in range(0, len(linha)-1):
  removeSpace = linha[i].strip()
  splits = removeSpace.split()
  if travaLoop == False:
    initListas(int(splits[1]))
    travaLoop = True
  else:
    criarLista(splits)

#Imprime Lista de Sucessores Predecessores e Grau de Entrada e Saida
pesquisarVerticeImprimirSucessores(verticeInput)
print("--X--")
pesquisarVerticeImprimirPred(verticeInput)
print("--X--")
print("Grau de Entrada: " + str(gEntrada))
print("Grau de Saida: " + str(gSaida))