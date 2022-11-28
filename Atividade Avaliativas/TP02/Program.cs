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
  private static int contarTam(String l)
  {
    int tam = 0;
    String[] vet = l.Split(' ');
    tam = Int32.Parse(vet[0]);



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
  public static void leituraGrafo(String arqName, matrizadj ma)
  {
    bool criouMatrizAdj = false;
    int tamanhoMatriz = 0;

    arqName = "db/" + arqName + ".txt";
    String? linha;
    using var file = new StreamReader(arqName);

    while ((linha = file.ReadLine()) != null)
    {


      if (!criouMatrizAdj)
      {
        tamanhoMatriz = contarTam(linha);
        ma.criarMatrizAdj(tamanhoMatriz);
        criouMatrizAdj = true;
      }

      String? linha2;
      while ((linha2 = file.ReadLine()) != null)
      {
        if (linha2 != null)
        {
          ma.receberDados(linha2, tamanhoMatriz);
        }

      }

      ma.imprimirMatrizAdj(tamanhoMatriz);
    }

  }
  public static void Main()
  {

    matrizadj ma = new matrizadj();
    bool loop = true;

    while (loop)
    {


      System.Console.WriteLine("Digite o nome do arquivo a ser lido | Digite FIM para encerrar o programa");
      string? arqName = Console.ReadLine();
      // string? arqName = "dataTeste";

      if (arqName != null && arqName != "fim" && arqName != "FIM" && arqName != "Fim")
      {
        leituraGrafo(arqName, ma);
      }



      if (arqName != "fim" && arqName != "FIM" && arqName != "Fim")
      {
        System.Console.WriteLine("Insira o VÉRTICE origem e destino respectivamente !");
        string? v1 = Console.ReadLine();
        string? v2 = Console.ReadLine();
      }


      if (arqName == "fim" && arqName == "FIM" && arqName == "Fim")
      {
        loop = false;
        System.Console.WriteLine("Encerrando o programa...");
        return;
      }

    }

  }
}
