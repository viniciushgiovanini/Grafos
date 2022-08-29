#imports
import sys
import os.path

#setando o path
path = './database/'


#func
def criarLista(rString):
  print(rString)



#Pegando Argumento do Command Line
fileName = sys.argv[1]
dirname = os.path.dirname(path)
verticeInput = sys.argv[2]

#Testa se Tem .txt no campo do nome do arquivo
if ".txt" in fileName:
  pathConcat = dirname + '/' + fileName
else:
  pathConcat = dirname + '/' + fileName + ".txt"

with open(pathConcat) as file:
  linha = file.readlines()


#Limpa a linha e deixa pronto para utilizar os valores
for i in range(1, len(linha)):
  removeSpace = linha[i].strip()
  splits = removeSpace.split()
  criarLista(splits)

