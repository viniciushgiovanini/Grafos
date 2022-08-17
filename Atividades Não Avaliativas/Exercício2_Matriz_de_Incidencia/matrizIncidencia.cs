class matrizIncidencia
{

  private String[] pegarElementoVertice(String v, int tam)
  {

    String[] ar = new String[tam];
    char[] letra = v.ToCharArray();
    int cont = 0;
    for (int i = 0; i < v.Length; i++)
    {
      if (letra[i] != '{' || letra[i] != ',')
      {
        ar[cont] = letra[i].ToString();
        cont++;
      }
    }


    return ar;
  }

  public void matrizIncidenciaND(String a, bool type, String v)
  {
    //{{a,b},{a,c},{b,a},{b,c},{b,d},{c,a},{c,b},{c,d},{d,b},{d,c},{d,e},{e,b},{e,d}} MI - Grafo Não Direcionado
    //{a,b,c,d,e}
    Program pc = new Program();
    int tamArestas = pc.contadorArestas(a);
    int tamVertices = pc.contadorVertices(v);
    String[,] inci = new String[tamArestas + 1, tamVertices + 1];
    String[] vetorVertice = new String[tamVertices];
    vetorVertice = pegarElementoVertice(v, tamVertices);
    for (int i = 0; i < tamVertices; i++)
    {
      inci[i, 7] = vetorVertice[i];
    }

  }
}