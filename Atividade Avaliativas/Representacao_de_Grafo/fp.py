#imports
import sys
import os.path

#setando o path
path = './database/'

#Pegando Argumento do Command Line
fileName = sys.argv[1]
dirname = os.path.dirname(path)
pathConcat = dirname + '/' + fileName + '.txt'

with open(pathConcat) as file:
  linha = file.readlines()
  

#Limpa a linha e deixa pronto para utilizar os valores
print(linha[0].strip())
