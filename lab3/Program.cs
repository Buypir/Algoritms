using System;
using System.Collections.Generic;
using System.IO;

class Program
{
    static void Main()
    {
        string[] inputLines = File.ReadAllLines("D:\\Labs\\algo\\lab3\\lab3\\govern.in");

        Dictionary<string, List<string>> graph = new Dictionary<string, List<string>>();

        foreach (string line in inputLines)
        {
            string[] tokens = line.Split(' ');
            string document = tokens[0];
            string prerequisite = tokens[1];

            if (!graph.ContainsKey(prerequisite))
                graph[prerequisite] = new List<string>();

            graph[prerequisite].Add(document);
        }

        List<string> optimizedOrder = OptimizeOrder(graph);

        File.WriteAllLines("D:\\Labs\\algo\\lab3\\lab3\\govern.out", optimizedOrder);
    }

    static List<string> OptimizeOrder(Dictionary<string, List<string>> graph)
    {
        List<string> optimizedOrder = new List<string>();
        HashSet<string> visited = new HashSet<string>();

        foreach (string node in graph.Keys)
        {
            if (!visited.Contains(node))
                DFS(node, graph, visited, optimizedOrder);
        }

        optimizedOrder.Reverse();
        return optimizedOrder;
    }

    static void DFS(string node, Dictionary<string, List<string>> graph, HashSet<string> visited, List<string> optimizedOrder)
    {
        visited.Add(node);

        if (graph.ContainsKey(node))
        {
            foreach (string neighbor in graph[node])
            {
                if (!visited.Contains(neighbor))
                    DFS(neighbor, graph, visited, optimizedOrder);
            }
        }

        optimizedOrder.Add(node);
    }
}