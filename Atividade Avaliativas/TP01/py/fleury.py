class fleuryAlg:
  
  def tratarLinha(self, item):
    numerosTratados = []
    hasNumber1 = False
    cont = 0
    concatNumber1 = ""
    concatNumber2 = ""
    while cont < len(item):
      if item[cont] != "\n":
        if item[cont] == " ":
          hasNumber1 = True
        elif hasNumber1 == False:
          concatNumber1 = concatNumber1 + item[cont]   
        elif hasNumber1 == True and item[cont] != " ":
          concatNumber2 = concatNumber2 + item[cont]
      cont = cont + 1
    numerosTratados.append(int(concatNumber1))
    numerosTratados.append(int(concatNumber2))
    
    return numerosTratados
    
    
  def fleurynotIsEuleriano(self, listaNumber, listaGuardarVértice):
      
   if len(listaGuardarVértice) == 0:
    listaGuardarVértice.append(listaNumber[0])
   elif listaGuardarVértice[0] == listaNumber[0]:
    listaGuardarVértice.append(listaNumber[0])
   elif listaGuardarVértice[0] != listaNumber[0]:
    qtdV = len(listaGuardarVértice)
    listaGuardarVértice.clear()
    listaGuardarVértice.append(listaNumber[0])
    if qtdV % 2 != 0:
      return True
    
    
    
      

  
  def fleuryInicial(self, nomeArq, entradaFL):
    
    strInterpolacao = ''
    entradaFL = int(entradaFL)
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
    arquivinho = reader.readlines()
    contadorpularPrimeiraLinha = 0
    
    # Variaveis Grafos Não eulerianos    
    listaGuardarVértice = [] #esse lista é apra guardar os vértices para testar se é euleriano
    
    for item in arquivinho:
      if contadorpularPrimeiraLinha != 0:
        linhaTratada = self.tratarLinha(item)
        isNotEulerian =  self.fleurynotIsEuleriano(linhaTratada, listaGuardarVértice)
        
        if isNotEulerian:
          print("\nEsse grafo NÃO é euleriano\n")
          return
        
      else:
        contadorpularPrimeiraLinha = contadorpularPrimeiraLinha + 1
     
 
    
     
  
  
  