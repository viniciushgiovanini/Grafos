class Program
{
  private static int contarTam(String l)
  {
    int tam = 0;
    String[] vet = l.Split(' ');
    tam = Int32.Parse(vet[0]);

    return tam;
  }

  public static int leituraGrafo(String arqName, matrizadj ma)
  {


    try
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
    catch (IOException e)
    {
      System.Console.WriteLine("Ocorreu um erro na leitura do arquivo: " + e.Source);
      System.Console.WriteLine("Tente digitar o arquivo sem a extensão dele (arquivo.txt). Digite somente (arquivo)");
      return -1;
    }
    return 0;
  }
  public static void Main()
  {

    matrizadj ma = new matrizadj();
    bool loop = true;

    System.Console.WriteLine("0 - Encerrar o Programa | 1 - Descobrir Fluxo Máximo de um Grafo Qualquer");
    string? valorS = (Console.ReadLine());

    int valor = (valorS != null) ? Int32.Parse(valorS) : -1;

    while (loop)
    {


      switch (valor)
      {
        case 0:
          System.Console.WriteLine("Encerrando o Programa...");
          return;
        case 1:
          System.Console.WriteLine("Digite o nome do arquivo a ser lido | Digite FIM para encerrar o programa");
          string? arqName = Console.ReadLine();
          int statsRetorno = 10;
          // string? arqName = "dataTeste";

          if (arqName != null)
          {
            statsRetorno = leituraGrafo(arqName, ma);
          }

          if (statsRetorno != -1)
          {
            System.Console.WriteLine("Insira o VÉRTICE origem e destino respectivamente !");
            string? v1 = Console.ReadLine();
            string? v2 = Console.ReadLine();
          }

          break;
        default:
          System.Console.WriteLine("Valor não encontrado...");
          break;
      }

      System.Console.WriteLine("0 - Encerrar o Programa | 1 - Descobrir Fluxo Máximo de um Grafo Qualquer");
      valorS = (Console.ReadLine());
      valor = (valorS != null) ? Int32.Parse(valorS) : -1;


    }

  }
}
