//2 - Implementar programa que leia dados de um grafo qualquer (do terminal ou de um arquivo) e represente o grafo
//Por meio de matriz de incidência
//Por meio de matriz de adjacência

class Program
{
  public static bool eDirecionada(String a)
  {
    char[] letra = a.ToCharArray();
    Boolean resp = true;
    if (letra[1] == '{')
    {
      resp = false;
    }
    else if (letra[1] == '(')
    {
      resp = true;
    }

    return resp;
  }

  public int contadorArestas(String a)
  {

    int contador = 0;
    char[] letra = a.ToCharArray();
    for (int i = 0; i < a.Length; i++)
    {
      if (letra[i] == '{' || letra[i] == '(')
      {
        contador++;
      }
    }

    if (contador != 0)
    {
      contador -= 2;
    }

    return contador;
  }

  public int contadorVertices(String v)
  {

    char[] letra = v.ToCharArray();
    int contador = 0;
    for (int i = 0; i < v.Length; i++)
    {
      if (letra[i] != '{')
      {
        contador++;
      }
    }

    return contador;

  }

  public static void Main()
  {

    System.Console.WriteLine("Insira o Grafo !");
    System.Console.WriteLine("Insira os Vértices do Grafo Exemplo = {1,2,3,4}");
    String? v = Convert.ToString(Console.ReadLine());
    System.Console.WriteLine("Inira as Arestas/Relação do Grafo = (Represente como {{1,2}} - Não Direcionado ou {(1,2)} Grafo Direcionado ! ");
    String? graph = Convert.ToString(Console.ReadLine());

    if (graph != null)
    {
      bool direcioada = eDirecionada(graph);
    }



  }
}