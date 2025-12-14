using AdventOfCode.helper;

namespace AdventOfCode._09;

public class Day09 : Day
{
    private InputHelper helper;
    private bool test;

    private List<string> lines;
    
    private static string DAY = "09";

    public Day09(bool test)
    {
        this.test = test;
        this.helper = new InputHelper();
        this.lines = helper.ReadLines(this.test, DAY);
        if (this.lines.Count == 0) {
            System.Environment.Exit(-1);
        }
        
    }
    public void solveStage1()
    {
        List<(int, int)> redTiles = new List<(int, int)>();

        foreach (var line in this.lines)
        {
            var coords = line.Split(',');
            var tile = (int.Parse(coords[0]), int.Parse(coords[1]));
            redTiles.Add(tile);
        }

        ulong area = 0;
        
        for (var i = 0; i < redTiles.Count; i++)
        {
            for (var j = i+1; j < redTiles.Count; j++)
            {
                ulong xDiff = (ulong)Math.Abs(redTiles[i].Item1 - redTiles[j].Item1) + 1;
                ulong yDiff = (ulong)Math.Abs(redTiles[i].Item2 - redTiles[j].Item2) + 1;

                var a = xDiff * yDiff;
                area = Math.Max(area, a);
            }
        }
        Console.WriteLine($"Solution stage 1: {area}");
    }

    private bool checkRange(Dictionary<int, HashSet<(int, int)>> edges, (int,int) range, double h)
    {
        
        var checker = edges.Keys.Where(k => k > range.Item1 && k < range.Item2).ToHashSet();
        if (checker.Count == 0)
            return false;
        return edges.Where(kvp => checker.Contains(kvp.Key)).Any(kvp =>
        {
            return kvp.Value.Any(edgeRange => h > edgeRange.Item1 && h < edgeRange.Item2);
        });
    }

    public void solveStage2()
    {
        List<(int, int)> redTiles = new List<(int, int)>();
        Dictionary<int, HashSet<(int, int)>> horizontalEdges = new Dictionary<int, HashSet<(int, int)>>();
        Dictionary<int, HashSet<(int, int)>> verticalEdges = new Dictionary<int, HashSet<(int, int)>>();
        
        foreach (var line in this.lines)
        {
            var coords = line.Split(',');
            var tile = (x: int.Parse(coords[0]), y:int.Parse(coords[1]));
            redTiles.Add(tile);
        }
        
        for (var i = 0; i < redTiles.Count; i++)
        {
            var tile1 =  redTiles[i];
            var tile2 =  redTiles[(i+1) % redTiles.Count];

            HashSet<(int, int)> s;
            (int, int) range;
            if (tile1.Item1 == tile2.Item1) // vertical
            {
                s = new HashSet<(int, int)>();
                if(verticalEdges.ContainsKey(tile1.Item1))
                    s = verticalEdges[tile1.Item1];
                range = (Math.Min(tile1.Item2, tile2.Item2), Math.Max(tile1.Item2, tile2.Item2));
                s.Add(range);
                verticalEdges[tile1.Item1] = s;
            }
            else
            {
                s = new HashSet<(int, int)>();
                if(horizontalEdges.ContainsKey(tile1.Item2))
                    s = horizontalEdges[tile1.Item2];
                range = (Math.Min(tile1.Item1, tile2.Item1), Math.Max(tile1.Item1, tile2.Item1));
                s.Add(range);
                horizontalEdges[tile1.Item2] = s;
            }
        }


        ulong area = 0;
        
        for (var i = 0; i < redTiles.Count; i++)
        {
            for (var j = i+1; j < redTiles.Count; j++)
            {
                var point1 = redTiles[i];
                var point2 = redTiles[j];

                if (point1.Item1 == point2.Item1 || point1.Item2 == point2.Item2)
                    continue;
                
                ulong xDiff = (ulong)Math.Abs(redTiles[i].Item1 - redTiles[j].Item1) + 1;
                ulong yDiff = (ulong)Math.Abs(redTiles[i].Item2 - redTiles[j].Item2) + 1;

                var a = xDiff * yDiff;
                if(a < area)
                    continue;

                var point3 = (point1.Item1, point2.Item2);
                var point4 = (point2.Item1, point1.Item2);

                (int, int) leftTop;
                (int, int) leftBottom;
                (int, int) rightTop;
                (int, int) rightBottom;

                if (point1.Item1 > point2.Item1) // p1 and p3 are right
                {
                    leftTop = point2.Item2 > point4.Item2 ? point2 : point4;
                    leftBottom = point2.Item2 > point4.Item2 ? point4 : point2;
                    rightTop = point1.Item2 > point3.Item2 ? point1 : point3;
                    rightBottom = point1.Item2 > point3.Item2 ? point3 : point1;
                }
                else
                {
                    rightTop = point2.Item2 > point4.Item2 ? point2 : point4;
                    rightBottom = point2.Item2 > point4.Item2 ? point4 : point2;
                    leftTop = point1.Item2 > point3.Item2 ? point1 : point3;
                    leftBottom = point1.Item2 > point3.Item2 ? point3 : point1;
                }

                var horizontalRange = (leftBottom.Item1, rightBottom.Item1);
                var verticalRange = (leftBottom.Item2, leftTop.Item2);

                var checkHorizontaly1 = leftTop.Item2 - 0.5;
                var checkHorizontaly2 = leftBottom.Item2 + 0.5;

                var checkVerticalx1 = leftTop.Item1 + 0.5;
                var checkVerticalx2 = rightTop.Item1 - 0.5;
                var c1 = checkRange(verticalEdges, horizontalRange, checkHorizontaly1);
                if(c1)
                    continue;
                var c2 = checkRange(verticalEdges, horizontalRange, checkHorizontaly2);
                if(c2)
                    continue;
                var c3 = checkRange(horizontalEdges, verticalRange, checkVerticalx1);
                if(c3)
                    continue;
                var c4 = checkRange(horizontalEdges, verticalRange, checkVerticalx2);
                if(c4)
                    continue;
                //Console.WriteLine($"Checked {point1}-{point2}: {checkHorizontaly1} {horizontalRange}");
                //Console.WriteLine($"Returned {c1 && c2 && c3 && c4}");
                area = a;
            }
        }
        Console.WriteLine($"Solution stage 2: {area}");

    }
}