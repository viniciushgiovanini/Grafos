# Aluno: Vinícius Henrique Giovanini
# Data: 30/10/2022
# Arquivo principal para rodar o TP01 de Grafos

#imports
from gerarGrafos import criarGrafos
from fleury import fleuryAlg
import time
start = 0
end = 0

print("0 - Encerrar o Programa | 1 - Geração dos Grafos | 2 - identificacao de Grafos | 3 - Realizar Caminho")
numeroCase = int(input("Escreva o número desejado !\n"))

vLoop = True
while(vLoop):
  if numeroCase == 0:
    vLoop = False
    print("Encerrando o Programa")
    break
  elif numeroCase == 1:
    print("a - Gerar grafo euleriano | b - gerar grafo não euleriano | c - gerar grafo semi euleriano")
    numeroCase2 = input("Insira a letra desejada: ")
    if numeroCase2 == "a":
      tamGrafo = int(input("Insira o tamanho do grafo euleriano desejado (100, 1000, 10000 ou 100.000): "))
      nomeArquivo = str(input("Insira o nome do Arquivo TXT: "))
      gEule = criarGrafos()
      start = time.perf_counter()
      class1 = gEule.criarEulerianos(tamGrafo, nomeArquivo)
      end = time.perf_counter()
      print(end - start)
    elif numeroCase2 == "b":
     tamGrafo = int(input("Insira o tamanho do grafo NÃO euleriano desejado (100, 1000, 10000 ou 100.000): "))
     nomeArquivo = str(input("Insira o nome do Arquivo TXT: "))
     #  chamar funcao grafo semi euleriano
     gEule = criarGrafos()
     start = time.perf_counter()
     class1 = gEule.criarNaoEulerianos(tamGrafo, nomeArquivo)
     end = time.perf_counter()
     print(end - start)
    elif numeroCase2 == "c":
     tamGrafo = int(input("Insira o tamanho do grafo SEMI euleriano desejado (100, 1000, 10000 ou 100.000): "))
     nomeArquivo = str(input("Insira o nome do Arquivo TXT: "))
     gEule = criarGrafos()
     start = time.perf_counter()
     class1 = gEule.criarSemiEulerianos(tamGrafo, nomeArquivo) 
     end = time.perf_counter()
     print(end - start)
    
      
    else:
      print("Valor inserido não existe !")   
  elif numeroCase == 2:
   gFleury = fleuryAlg()
   print("\n")
   nomeArq = input("Digite o nome do arquivo a ser lido: ")
   print("\n")
   start = time.perf_counter()
   gFleury.tipeGraph(nomeArq)
   end = time.perf_counter()
   print("Tempo de Execucao da Descoberta: ", end - start)
   print("-----X----\n")
  elif numeroCase == 3:
    gFleury = fleuryAlg()
    print("\n")
    nomeArq = input("Digite o nome do arquivo a ser lido: ")
    verticeInicial = input("Digite o vertice inicial da busca: ")
    start = time.perf_counter()
    gFleury.pesquisarCaminho(nomeArq, int(verticeInicial))
    end = time.perf_counter()
    print("-----X----\n")
    print("Tempo de Execucao da Busca: ", end - start)
    print("\n\n")
  else:
    print("Valor inserido não existe !")
  print("0 - Encerrar o Programa | 1 - Geração dos Grafos | 2 - identificacao de Grafos | 3 - Realizar Caminho")  
  numeroCase = int(input("Escreva o número desejado !\n"))

