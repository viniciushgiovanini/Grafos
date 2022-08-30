#Implementação Predecessores
#Agora tem que fazer a mesma coisa com predecessores, aproveitar a função, quando ele limpar a linha e for adicionar o sucessor
#ele vai na posicao e adiciona o predecessor, se ja estiver um nó de predecessor ele vai ter que pecorrer o objeto ate achar
#o none e implementar ele lá

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
elementPosiLS = 0
elementPosiLP = 0


#func
def initListas(tamSuce, tamPrede):
  global myListPredecesso
  global myListSucesso
  myListSucesso = [None] * tamSuce
  myListPredecesso = [None] * tamPrede


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

# def fazerPesquisaCriarSuce(objA, newObj):
#   if objA.sucessor == None:
#     objA.sucessor = newObj
#     return
#   else:
#     fazerPesquisaCriarSuce(objA.sucessor, newObj)

#Tem que mudar esse método para aceitar predecessores
def fazerPesquisaCriar(objA, newObj):
  if objA.sucessor == None:
    objA.sucessor = newObj
    return
  else:
    fazerPesquisaCriar(objA.sucessor, newObj)

#Tem que mudar esse método para aceitar predecessores
def criarLista(rSplit):
  global elementPosiLP
  global elementPosiLS
  mudouV = mudouVertice(rSplit[0])

  if mudouV == "notInit":

    #Criando Lista de Sucessores
    raiz = myVerticeSuce()
    suce = myVerticeSuce()
    raiz.vPrinci = rSplit[0]
    
    suce.vPrinci = rSplit[1]
    suce.sucessor = None
    raiz.sucessor = suce
    myListSucesso.insert(elementPosiLS, raiz)
    elementPosiLP += 1
    
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
    myListSucesso.insert(elementPosiLS,newRaiz)
    elementPosiLS += 1

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
# fileName = sys.argv[1]
# dirname = os.path.dirname(path)
# verticeInput = sys.argv[2]


# Testa se Tem .txt no campo do nome do arquivo
# if ".txt" in fileName:
#   pathConcat = dirname + '/' + fileName
# else:
#   pathConcat = dirname + '/' + fileName + ".txt"

#.\Atividade Avaliativas\Representacao_de_Grafo\database\dataTeste.txt
# pathConcat
with open(".\Atividade Avaliativas\Representacao_de_Grafo\database\dataTeste.txt") as file:
  linha = file.readlines()


#Limpa a linha e deixa pronto para utilizar os valores
#len(linha)
travaLoop = False
for i in range(0, len(linha)-1):
  removeSpace = linha[i].strip()
  splits = removeSpace.split()
  if travaLoop == False:
    initListas(int(splits[0]), int(splits[1]))
    travaLoop = True
  else:
    criarLista(splits)
  
  
  
# print(myListPredecesso[9].vPrinci)
#Imprime Lista de Sucessores
pesquisarVerticeImprimirSucessores(str(1))