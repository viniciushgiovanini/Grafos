//2 - Implementar programa que leia dados de um grafo qualquer (do terminal ou de um arquivo) e represente o grafo
//Por meio de matriz de incidência
//Por meio de matriz de adjacência

class Program
{
  private static bool selectionSort(int[] ver, int busca)
  {
    bool verticeExistente = false;

    for (int i = 0; i < ver.Length; i++)
    {
      if (ver[i] == busca)
      {
        verticeExistente = true;
      }
    }
    return verticeExistente;
  }
  private static int qtdElementosArray(int[] a)
  {
    int contador = 0;

    foreach (var i in a)
    {
      if (i != 0)
      {
        contador++;
      }
    }
    return contador;
  }
  private static int contarTam()
  {


    using var file = new StreamReader("./graph.txt");//poderia usar RAF pra otimizar aqui
    matrizadj Adj = new matrizadj();
    String? LinhaTam;
    bool podeContar = false;
    int[] vertice = new int[100];
    int contadorVertice = 0;

    while ((LinhaTam = file.ReadLine()) != "fim")
    {
      if (LinhaTam != null)
      {
        if (LinhaTam.Contains("n  m"))
        {
          podeContar = true;
          LinhaTam = file.ReadLine();
        }
        else if (LinhaTam.Equals("fim"))
        {
          podeContar = false;
        }


        if (podeContar && LinhaTam != null)
        {

          int valorVertice = Adj.limpar(LinhaTam);

          if (!(selectionSort(vertice, valorVertice)))
          {
            vertice[contadorVertice] = valorVertice;
            contadorVertice++;
          }


        }
      }
    }

    int tam = qtdElementosArray(vertice);
    file.Close();
    return tam;
  }

  private static int contarTamArestas()
  {
    using var file = new StreamReader("./graph.txt");
    String? LinhaTam;
    int contador = 0;
    while ((LinhaTam = file.ReadLine()) != "fim")
    {
      if (LinhaTam != null && LinhaTam != "n  m" && LinhaTam != "Inci")
      {
        contador++;
      }
    }
    return contador;
  }

  public static void Main()
  {

    using var file = new StreamReader("./graph.txt");
    String? linha;
    bool criouMatrizAdj = false;
    bool criouMatrizInci = false;
    int tamanhoMatriz = 0;
    //class
    matrizadj ma = new matrizadj();
    matrizIncidencia mi = new matrizIncidencia();

    while ((linha = file.ReadLine()) != null)
    {

      if (linha == "Adj")
      {
        if (!criouMatrizAdj)
        {
          tamanhoMatriz = contarTam();
          ma.criarMatrizAdj(tamanhoMatriz);
          criouMatrizAdj = true;
        }

        String? linha2;
        while ((linha2 = file.ReadLine()) != "fim")
        {
          if (linha2 != null && (!linha2.Equals("n  m")))
          {
            ma.receberDados(linha2, tamanhoMatriz);
          }

        }

        ma.imprimirMatrizAdj(tamanhoMatriz);
      }
      else if (linha == "Inci")
      {
        int qtdArestas = 0;
        int qtdVertices = 0;
        if (!criouMatrizInci)
        {
          qtdArestas = contarTamArestas();
          qtdVertices = contarTam();
          mi.criarMatrizInci(qtdVertices, qtdArestas);
          criouMatrizInci = true;
        }

        String? linha2;
        while ((linha2 = file.ReadLine()) != "fim")
        {
          if (linha2 != null && (!linha2.Equals("n  m")))
          {
            mi.receberDados(linha2);
          }

        }

        mi.imprimirMatrizInci(qtdArestas, qtdVertices);
      }

    }

    file.Close();


  }
}

