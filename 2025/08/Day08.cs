using AdventOfCode.helper;

namespace AdventOfCode._08;

public class Day08 : Day
{
    private InputHelper helper;
    private bool test;

    private List<string> lines;
    
    private static string DAY = "08";

    public Day08(bool test)
    {
        this.test = test;
        this.helper = new InputHelper();
        this.lines = helper.ReadLines(this.test, DAY);
        if (this.lines.Count == 0) {
            System.Environment.Exit(-1);
        }
        
    }

    private double distance((int, int, int) a, (int, int, int) b)
    {
        return Math.Sqrt(
                Math.Pow(a.Item1-b.Item1, 2) + 
                Math.Pow(a.Item2-b.Item2, 2) + 
                Math.Pow(a.Item3-b.Item3, 2));
    }
    public void solveStage1()
    {
        List<(int, int, int)> points = new List<(int, int, int)>();
        Dictionary<(int, int, int), HashSet<(int, int, int)>> clusters =
            new Dictionary<(int, int, int), HashSet<(int, int, int)>>();

        foreach (var line in this.lines)
        {
            var coords = line.Split(',');
            var point = (int.Parse(coords[0]), int.Parse(coords[1]), int.Parse(coords[2]));
            points.Add(point);
            HashSet<(int, int, int)> c = new HashSet<(int, int, int)>();
            c.Add(point);
            clusters[point] = c;
        }
        
        List<((int, int, int), (int, int, int), double)> connections =
            new List<((int, int, int), (int, int, int), double)>();

        for (var i = 0; i < points.Count; i++)
        {
            for (var j = i+1; j < points.Count; j++)
            {
                connections.Add((points[i], points[j], distance(points[i], points[j])));
            }
        }
        
        var sortedConnections = connections.OrderBy(t => t.Item3).ToList();
        
        for (int i = 0; i < (test ? 10 : 1000); i++)
        {
            if (i >= sortedConnections.Count)
                break;
            

            var n = sortedConnections[i];
            var p1 = n.Item1;
            var p2 = n.Item2;
            
            var c1 = clusters[p1];
            var c2 = clusters[p2];
            
            foreach (var point in c2)
            {
                c1.Add(point);
                clusters[point] = c1;
            }
        }

        var unique = clusters.Select(kvp => kvp.Value).Distinct().OrderByDescending(set => set.Count).ToList();
        Console.WriteLine($"Solution to {DAY}: {unique[0].Count * unique[1].Count * unique[2].Count}");

    }

    public void solveStage2()
    {
        List<(int, int, int)> points = new List<(int, int, int)>();
        Dictionary<(int, int, int), HashSet<(int, int, int)>> clusters =
            new Dictionary<(int, int, int), HashSet<(int, int, int)>>();

        foreach (var line in this.lines)
        {
            var coords = line.Split(',');
            var point = (int.Parse(coords[0]), int.Parse(coords[1]), int.Parse(coords[2]));
            points.Add(point);
            HashSet<(int, int, int)> c = new HashSet<(int, int, int)>();
            c.Add(point);
            clusters[point] = c;
        }
        
        List<((int, int, int), (int, int, int), double)> connections =
            new List<((int, int, int), (int, int, int), double)>();

        for (var i = 0; i < points.Count; i++)
        {
            for (var j = i+1; j < points.Count; j++)
            {
                connections.Add((points[i], points[j], distance(points[i], points[j])));
            }
        }
        
        var sortedConnections = connections.OrderBy(t => t.Item3).ToList();
        
        for (int i = 0; i < sortedConnections.Count; i++)
        {
            var n = sortedConnections[i];
            var p1 = n.Item1;
            var p2 = n.Item2;
            
            var c1 = clusters[p1];
            var c2 = clusters[p2];
            
            foreach (var point in c2)
            {
                c1.Add(point);
                clusters[point] = c1;
            }

            if (c1.Count == points.Count)
            {
                ulong x1 = (ulong)p1.Item1;
                ulong x2 = (ulong)p2.Item1;
                Console.WriteLine($"FOund: {x1 * x2}");
                break;
            }
        }
        
        Console.WriteLine($"Solution to {DAY}: Fin");
    }
}