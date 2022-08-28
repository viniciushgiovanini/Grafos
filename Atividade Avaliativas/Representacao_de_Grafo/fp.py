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
  

print(linha)