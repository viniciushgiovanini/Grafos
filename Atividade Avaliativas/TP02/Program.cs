class Program
{
  private static int contarTam(String l)
  {
    int tam = 0;
    String[] vet = l.Split(' ');
    tam = Int32.Parse(vet[0]);

    return tam;
  }

  public static void leituraGrafo(String arqName, matrizadj ma)
  {
    bool criouMatrizAdj = false;
    int tamanhoMatriz = 0;

    arqName = "db/" + arqName + ".txt";
    String? linha;
    using var file = new StreamReader(arqName);

    // Faz a leitura da primeira linha contendo a qtd de vértice e aresta.
    while ((linha = file.ReadLine()) != null)
    {

      // Se não existir matriz ele cria uma matriz com tamamanho da qtd de vértices.
      if (!criouMatrizAdj)
      {
        tamanhoMatriz = contarTam(linha);
        ma.criarMatrizAdj(tamanhoMatriz);
        criouMatrizAdj = true;
      }

      // faz a leitura linha por linha até o final do arquivo.
      String? linha2;
      while ((linha2 = file.ReadLine()) != null)
      {
        if (linha2 != null)
        {
          // Criação da Matriz de Adjacencia 
          // Pega a linha e coloca o número 1 na posicao da matriz
          ma.receberDados(linha2, tamanhoMatriz);
        }

      }

      // ma.imprimirMatrizAdj(tamanhoMatriz);
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
