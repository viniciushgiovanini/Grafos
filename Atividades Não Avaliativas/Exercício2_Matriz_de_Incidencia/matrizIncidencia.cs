class matrizIncidencia
{
  int[,]? mAic;


  public void criarMatrizInci(int vertice, int aresta)
  {
    mAic = new int[aresta, vertice + 1];
  }


  public void receberDados(String valor)
  {
    matrizadj ma = new matrizadj();//só para usar os métodos de limpeza que estão presente nessa classe
    int tamAresta = ma.limpar(valor);
    int tamVertice = ma.limpar2(valor);

    if (tamAresta != 0 && tamVertice != 0)
    {
      mAic[tamAresta, tamVertice] = 1;
      mAic[tamAresta, tamAresta] = -1;
    }


  }

  public void imprimirMatrizInci(int tamAresta, int tamVertice)
  {

    for (int i = 1; i < tamVertice + 1; i++)
    {
      for (int j = 1; j < tamAresta; j++)
      {
        System.Console.Write("[" + mAic[j, i] + "]");
      }
      System.Console.WriteLine();
    }

  }

}