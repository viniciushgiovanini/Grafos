# Aluno: Vinícius Henrique Giovanini

#imports
from initMatriz import gerarMatriz
from searchFluxoMax import buscaFluxo
from createGraph import criarG
import time
# from copy import deepcopy
start = 0
end = 0

print("0 - Encerrar o Programa | 1 - Identificar Fluxo Maximo em um Grafo Qualquer | 2 - Realizar Geração de um Grafo")
numeroCase = int(input("Escreva o número desejado !\n"))
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
   nomeArq = input("Digite o nome do arquivo a ser lido: ")
   origem = int(input("Digite o valor do vértice Origem: "))
   destino = int(input("Digite o valor do vértice Destino: "))
   start = time.perf_counter()
   Matriz = iniciarMatriz.gerandoListas(nomeArq).copy()
   if Matriz != []:
    fluxosMaximos = []
    retorno = search.searchPrincipal(Matriz, origem, destino)
    print("\n")
    end = time.perf_counter()
    print("Tempo de Execucao da Descoberta: ", end - start)
    
    frase = "\nFoi encontrado (" + str(len(retorno)) + ") caminhos neste grafo !\n" 
    print(frase)
        
    print("-----X----\n")
  elif numeroCase == 2:
    nomeGerarGraph = str(input("Digite o nome do arquivo a ser criado: "))
    qtdK = int(input("Digite o número de grafos com 4 arestas interligadas você deseja!: "))
    gGraph = criarG()
    gGraph.gerarMatrizPrinci(qtdK , nomeGerarGraph)
  else:
    print("Valor inserido não existe !")
  print("0 - Encerrar o Programa | 1 - Identificar Fluxo Maximo em um Grafo Qualquer | 2 - Realizar Geração de um Grafo")
  numeroCase = int(input("Escreva o número desejado !\n"))