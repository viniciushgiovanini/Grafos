class matrizadj
{
  int[,]? mAdj;
  public void criarMatrizAdj(int tam)
  {
    mAdj = new int[tam + 1, tam + 1];
  }
  public int limpar(String a)
  {
    a = a.Trim();
    char[] limp = a.ToCharArray();
    int aConvert = (int)Char.GetNumericValue(limp[0]);//convertendo char para int

    return aConvert;
  }

  public int limpar2(String a)
  {
    a = a.Trim();
    String[] vet = a.Split(' ');
    int aConvert = Int32.Parse(vet[vet.Length - 1]);//convertendo char para int

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