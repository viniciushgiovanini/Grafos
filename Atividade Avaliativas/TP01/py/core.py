#imports
from gerarGrafos import criarGrafos
import time
start = time.perf_counter()

gEule = criarGrafos()
class1 = gEule.criarEulerianos(100)
end = time.perf_counter()
print(end - start)
print(class1)