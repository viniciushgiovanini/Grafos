class matrizadj
{
  int[,]? mAdj;
  public void criarMatrizAdj(int tam)
  {
    mAdj = new int[tam + 1, tam + 1];
    //comentario era pra dicionar cabecalho para matriz
    // int contador = 0;
    // for (int i = 0; i < tam + 1; i++)
    // {
    //   mAdj[0, i] = contador++;
    // }

    // contador = 0;

    // for (int j = 0; j < tam + 1; j++)
    // {
    //   mAdj[j, tam + 1] = contador++;
    // }
  }
  public int limpar(String a)
  {

    char[] limp = a.ToCharArray();
    int aConvert = (int)Char.GetNumericValue(limp[0]);//convertendo char para int

    return aConvert;
  }

  public int limpar2(String a)
  {

    char[] limp = a.ToCharArray();
    int aConvert = (int)Char.GetNumericValue(limp[3]);//convertendo char para int

    return aConvert;
  }

  public void receberDados(String a, int tam)
  {

    Program t = new Program();
    int vLinha = limpar(a);
    int vColuna = limpar2(a);

    if (vLinha != 0 && vColuna != 0)
    {
      mAdj[vLinha, vColuna] = 1;
    }

  }

  public void imprimirMatrizAdj(int tam)
  {

    for (int i = 0; i < tam + 1; i++)
    {
      for (int j = 0; j < tam + 1; j++)
      {
        System.Console.Write("[" + mAdj[i, j] + "]");
      }
      System.Console.WriteLine();
    }

  }

}