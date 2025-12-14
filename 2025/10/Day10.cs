using System.ComponentModel.Design;
using System.Numerics;
using System.Reflection.Metadata;
using System.Text.RegularExpressions;
using AdventOfCode.helper;
using Google.OrTools.LinearSolver;

namespace AdventOfCode._10;

public class Day10 : Day
{
    
    private InputHelper helper;
    private bool test;

    private List<string> lines;
    
    private static string DAY = "10";

    public Day10(bool test)
    {
        this.test = test;
        this.helper = new InputHelper();
        this.lines = helper.ReadLines(this.test, DAY);
        if (this.lines.Count == 0) {
            System.Environment.Exit(-1);
        }
        
    }

    private ulong checkButtons(int endState, List<int> buttons)
    {
        Queue<(int, ulong)> queue = new Queue<(int, ulong)>();
        
        queue.Enqueue((0, 0));

        while (true)
        {
            var state= queue.Dequeue();
            if(state.Item1 == endState)
                return state.Item2;

            var machineState = state.Item1;
            foreach (var button in buttons)
            {
                int newState = machineState ^ button;
                queue.Enqueue((newState, state.Item2+1));
            }
        }
    }
    
    private ulong checkButtons(List<int> endState, List<List<int>> buttons)
    {
        Queue<(List<int>, ulong)> queue = new Queue<(List<int>, ulong)>();
        
        queue.Enqueue((endState.Select(j => 0).ToList(), 0));
        var visited = new HashSet<string>();

        while (true)
        {
            var state= queue.Dequeue();
            var stateString = String.Join(",", state.Item1);
            if(visited.Contains(stateString))
                continue;
            
            visited.Add(stateString); 
            
            bool cont = false;
            bool finished = true;
            for (var i = 0; i < state.Item1.Count; i++)
            {
                if (state.Item1[i] == endState[i])
                {
                    continue;
                }else
                {
                    finished = false;
                }

                if (state.Item1[i] > endState[i])
                {
                    cont = true;
                    break;
                }
            }
            if(cont) continue;
            if(finished) return state.Item2;

            var machineState = state.Item1;
            foreach (var button in buttons)
            {
                List<int> newState = new List<int>(machineState);
                foreach (var i in button)
                {
                    newState[i] += 1;
                }
                queue.Enqueue((newState, state.Item2+1));
            }
        }
    }

    
    public void solveStage1()
    {
        ulong sum = 0;
        foreach (var line in this.lines)
        {
            var match = Regex.Match(line, @"(\[.+\]) (\(.+\)) (\{.*\})");
            var machineGroup = match.Groups[1];
            var buttonGroup = match.Groups[2];
            
            var machinesString = machineGroup.Value.Substring(1, machineGroup.Value.Length - 2);
            int machinesInt = 0;
            for (var i = 0; i < machinesString.Length; i++)
            {
                if(machinesString[i] == '.')
                    continue;
                machinesInt |= (1 << i);
            }
            
            var buttonMatches = Regex.Matches(buttonGroup.Value, @"\([\d+,?]+\)");
            List<int> buttons = new List<int>();
            foreach (Match buttonMatch in buttonMatches)
            {
                int button = 0;
                var s = buttonMatch.Value.Substring(1, buttonMatch.Value.Length - 2).Split(",");
                for (var i = 0; i < s.Length; i++)
                {
                    button |= (1 << int.Parse(s[i]));
                }
                //Console.WriteLine($"{buttonMatch.Value} => {button}");
                buttons.Add(button);
            }
            
            var presses = checkButtons(machinesInt,  buttons);
            Console.WriteLine($"{line} -> {presses}");
            sum += presses;
        }
        Console.WriteLine($"Solved stage 1: {sum}");
    }

    public void solveStage2()
    {
        ulong sum = 0;
        foreach (var line in this.lines)
        {
            var match = Regex.Match(line, @"(\[.+\]) (\(.+\)) (\{.*\})");
            var joltageGroup = match.Groups[3];
            var buttonGroup = match.Groups[2];
            
            var joltageString = joltageGroup.Value.Substring(1, joltageGroup.Value.Length - 2).Split(",");
            List<int> joltageLevels = new List<int>();
            foreach (var se in joltageString)
            {
                joltageLevels.Add(int.Parse(se));
            }
            
            var buttonMatches = Regex.Matches(buttonGroup.Value, @"\([\d+,?]+\)");
            List<List<int>> buttons = new List<List<int>>();
            foreach (Match buttonMatch in buttonMatches)
            {
                List<int> button = new List<int>();
                var s = buttonMatch.Value.Substring(1, buttonMatch.Value.Length - 2).Split(",");
                for (var i = 0; i < s.Length; i++)
                {
                    button.Add(int.Parse(s[i]));
                }
                buttons.Add(button);
            }
            
            var solver = Google.OrTools.LinearSolver.Solver.CreateSolver("CBC");
            List<Variable> vars = new List<Variable>();
            for (int i = 0; i < buttons.Count; i++)
            {
                vars.Add(solver.MakeIntVar(0.0, double.PositiveInfinity, $"x{i}"));
            }

            for (int i = 0; i < joltageLevels.Count; ++i)
            {
                LinearExpr expr = new LinearExpr();
                for (int buttonIndex = 0; buttonIndex < buttons.Count; ++buttonIndex)
                {
                    if (buttons[buttonIndex].All(x => x != i))
                        continue;
                    expr += vars[buttonIndex];
                }

                solver.Add(expr == joltageLevels[i]);
            }
            
            Objective objective = solver.Objective();
            foreach (var v in vars)
            {
                objective.SetCoefficient(v, 1);
            }
            objective.SetMinimization();
            
            Google.OrTools.LinearSolver.Solver.ResultStatus resultStatus = solver.Solve();

            if (resultStatus == Google.OrTools.LinearSolver.Solver.ResultStatus.OPTIMAL)
            {
                sum += (ulong)objective.Value();
            }
            else
            {
                Console.WriteLine("No solution found.");
            }
        }
        Console.WriteLine($"Solved stage 2: {sum}");
    }
}

