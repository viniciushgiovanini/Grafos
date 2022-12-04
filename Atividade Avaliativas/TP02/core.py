# Aluno: Vinícius Henrique Giovanini

#imports
from initMatriz import gerarMatriz
from searchFluxoMax import buscaFluxo
import time
# from copy import deepcopy
start = 0
end = 0

print("0 - Encerrar o Programa | 1 - Identificar Fluxo Maximo em um Grafo Qualquer")
# numeroCase = int(input("Escreva o número desejado !\n"))
numeroCase = 1
Matriz = []
vLoop = True
while(vLoop):
  if numeroCase == 0:
    vLoop = False
    print("Encerrando o Programa")
    break
  elif numeroCase == 1:
   iniciarMatriz = gerarMatriz()
   search = buscaFluxo()
   print("\n")
  #  nomeArq = input("Digite o nome do arquivo a ser lido: ")
   Matriz = iniciarMatriz.gerandoListas("euleriano10MIL").copy()
  #  origem = int(input("Digite o valor do vértice Origem."))
  #  destino = int(input("Digite o valor do vértice Destino"))
   fluxosMaximos = []
   search.searchPrincipal(Matriz, 1, 8)
  #  print("\n")
  #  start = time.perf_counter()
  #  iniciarMatriz.tipeGraph(nomeArq)
  #  end = time.perf_counter()
  #  print("Tempo de Execucao da Descoberta: ", end - start)
  #  print("-----X----\n")
  else:
    print("Valor inserido não existe !")
  print("0 - Encerrar o Programa | 1 - Identificar Fluxo Maximo em um Grafo Qualquer")
  numeroCase = int(input("Escreva o número desejado !\n"))