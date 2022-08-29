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
  antecessor = None

#Lista variavel Global
myListSucesso = []
verticeLidoAnterior = None


#func
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

def fazerPesquisaCriarSuce(objA, newObj):
  if objA.sucessor == None:
    objA.sucessor = newObj
    return
  else:
    fazerPesquisaCriarSuce(objA.sucessor, newObj)


def criarListaSucessores(rSplit):
  
  mudouV = mudouVertice(rSplit[0])

  if mudouV == "notInit":
    raiz = myVerticeSuce()
    suce = myVerticeSuce()
    raiz.vPrinci = rSplit[0]
    
    suce.vPrinci = rSplit[1]
    suce.sucessor = None
    raiz.sucessor = suce
    myListSucesso.append(raiz)
  elif mudouV == False:
    suce = myVerticeSuce()
    suce.vPrinci = rSplit[1]        
    tamList = len(myListSucesso)
    objetoAnterior = myListSucesso[tamList-1]
    fazerPesquisaCriarSuce(objetoAnterior, suce)
  else:
    newRaiz = myVerticeSuce()
    newSuce = myVerticeSuce()
    newRaiz.vPrinci = rSplit[0]
    newSuce.vPrinci = rSplit[1]
    newRaiz.sucessor = newSuce
    myListSucesso.append(newRaiz)

def recPesquisaSuce(objimprimir, sucessores):
  if objimprimir.vPrinci != None:
    if objimprimir.sucessor != None:
      sucessores.append(objimprimir.sucessor.vPrinci)
      recPesquisaSuce(objimprimir.sucessor, sucessores)
  else:
    return
    

def pesquisarVerticeImprimirSucessores(vPesquisa):
   objimprimir = myListSucesso[int(vPesquisa)-1]
   sucessores = []
   print("Vertice Principal: " + vPesquisa)
   recPesquisaSuce(objimprimir, sucessores)
   print("Sucessores: ")
   for i in sucessores:
    print("[" + i + "]", end='')
    

#Pegando Argumento do Command Line
fileName = sys.argv[1]
dirname = os.path.dirname(path)
verticeInput = sys.argv[2]


# Testa se Tem .txt no campo do nome do arquivo
if ".txt" in fileName:
  pathConcat = dirname + '/' + fileName
else:
  pathConcat = dirname + '/' + fileName + ".txt"

#.\Atividade Avaliativas\Representacao_de_Grafo\database\dataTeste.txt
with open(pathConcat) as file:
  linha = file.readlines()


#Limpa a linha e deixa pronto para utilizar os valores
for i in range(1, len(linha)):
  removeSpace = linha[i].strip()
  splits = removeSpace.split()
  criarListaSucessores(splits)

#Imprime Lista de Sucessores
pesquisarVerticeImprimirSucessores(str(verticeInput))