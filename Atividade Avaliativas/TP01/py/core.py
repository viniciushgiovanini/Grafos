#imports
from gerarGrafos import criarGrafos
from fleury import fleuryAlg
import time
start = 0
end = 0

print("0 - Encerrar o Programa | 1 - Geração dos Grafos | 2 - Fleury")
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
      tamGrafo = int(input("Insira o tamanho do grafo euleriano desejado (100, 1000 ou 100.000): "))
      nomeArquivo = str(input("Insira o nome do Arquivo TXT: "))
      gEule = criarGrafos()
      start = time.perf_counter()
      class1 = gEule.criarEulerianos(tamGrafo, nomeArquivo)
      end = time.perf_counter()
      print(end - start)
    elif numeroCase2 == "b":
     tamGrafo = int(input("Insira o tamanho do grafo NÃO euleriano desejado (100, 1000 ou 100.000): "))
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
    break 
  elif numeroCase == 2:
   gFleury = fleuryAlg()
   print("\n")
   entradaFL = int(input("Digite o número do grafo a ser analísado (1- Euleriano | 2- Não Euleriano | 3- Semi Euleriano: "))
   nomeArq = input("Digite o nome do arquivo a ser lido: ")
   print("\n")
   gFleury.fleuryInicial(nomeArq,entradaFL)
  else:
    print("Valor inserido não existe !")
  print("0 - Encerrar o Programa | 1 - Geração dos Grafos")  
  numeroCase = int(input("Escreva o número desejado !\n"))

