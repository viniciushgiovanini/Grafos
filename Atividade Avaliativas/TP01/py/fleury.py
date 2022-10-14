from contextlib import nullcontext


class fleuryAlg:
  def fleuryInicial(self, nomeArq, entradaFL):
    
    strInterpolacao = ''
    entradaFL = entradaFL.lower()
    if entradaFL == 1:
       strInterpolacao = 'data/grafosEulerianos/' + nomeArq + '.txt'
    elif entradaFL == 2:
       strInterpolacao = 'data/grafosNaoEulerianos/' + nomeArq + '.txt'
    elif entradaFL == 3:
       strInterpolacao = 'data/grafosSemiEulerianos/' + nomeArq + '.txt'
    else:
      print("Grafo não encontrado")
      return
    
    reader = open(strInterpolacao, "r")  
    
    while reader!=nullcontext:
      print(reader.read)
    