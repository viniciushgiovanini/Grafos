#imports
from gerarGrafos import criarGrafos
import time
start = time.perf_counter()


print("0 - Encerrar o Programa | 1 - Geração dos Grafos")
numeroCase = int(input("Escreva o número desejado !\n"))

vLoop = True
while(vLoop):
  if numeroCase == 0:
    vLoop = False
    print("Encerrando o Programa")
    break
  elif numeroCase == 1:
    print("a - Gerar grafo euleriano | b - gerar grafo semi euleriano | c - gerar grafo não euleriano")
    numeroCase2 = input("Insira a letra desejada: ")
    if numeroCase2 == "a":
      tamGrafo = int(input("Insira o tamanho do grafo euleriano desejado (100, 1000 ou 100.000): "))
      nomeArquivo = str(input("Insira o nome do Arquivo TXT: "))
      gEule = criarGrafos()
      class1 = gEule.criarEulerianos(tamGrafo, nomeArquivo)
    elif numeroCase2 == "b":
      pass
    elif numeroCase2 == "c":
      pass
    else:
      print("Valor inserido não existe !")    
  else:
    print("Valor inserido não existe !")
  print("0 - Encerrar o Programa | 1 - Geração dos Grafos")  
  numeroCase = int(input("Escreva o número desejado !\n"))

end = time.perf_counter()
print(end - start)