public class Solution {
    private void print(string text)
    {
        Console.WriteLine(text);
    }

    /**
    * Convert a Roman numeral to an Integer value (OPTIMAL SOLUTION).
    * @param s: a string
    * @return: an integer
    */    
    public int RomanToIntV1(string s) {
        int val = 0;

        for (int i = 0; i < s.Length; ++i)
        {
            char current = s[i];
            char next = i + 1 < s.Length ? s[i + 1] : '\0';

            if (current == 'C')
            {
                if (next == 'M')
                {
                    val += 900;
                    ++i;
                }
                else if (next == 'D')
                {
                    val += 400;
                    ++i;
                }
                else
                {
                    val += 100;
                }
            }
            else if (current == 'X')
            {
                if (next == 'C')
                {
                    val += 90;
                    ++i;
                }
                else if (next == 'L')
                {
                    val += 40;
                    ++i;
                }
                else
                {
                    val += 10;
                }
            }
            else if (current == 'I')
            {
                if (next == 'X')
                {
                    val += 9;
                    ++i;
                }
                else if (next == 'V')
                {
                    val += 4;
                    ++i;
                }
                else
                {
                    val += 1;
                }
            }
            else if (current == 'M')
            {
                val += 1000;
            }
            else if (current == 'D')
            {
                val += 500;
            }
            else if (current == 'L')
            {
                val += 50;
            }
            else if (current == 'V')
            {
                val += 5;
            }
        }

        return val;
    }

    public Dictionary<string, int> romanMap = new Dictionary<string, int>
    {
        { "I", 1 },
        { "IV", 4 },
        { "V", 5 },
        { "IX", 9 },
        { "X", 10 },
        { "XL", 40 },
        { "L", 50 },
        { "XC", 90 },
        { "C", 100 },
        { "CD", 400 },
        { "D", 500 },
        { "CM", 900 },
        { "M", 1000 }
    };

    public bool isSubtractive(char c)
    {
        return c == 'I' || c == 'X' || c == 'C';
    }

    public int RomanToIntV2(string s) {
        int result = 0;

        for (int i = 0; i < s.Length; ++i)
        {
            char currentSymbol = s[i];
            char nextSymbol = i + 1 < s.Length ? s[i + 1] : '\0';

            if (isSubtractive(currentSymbol))
            {
                string romanSymbol = currentSymbol.ToString() + nextSymbol.ToString();

                if (romanMap.ContainsKey(romanSymbol))
                {
                    result += romanMap[romanSymbol];
                    ++i;
                }
                else
                {
                    result += romanMap[currentSymbol.ToString()];
                }
            } else 
            {
                result += romanMap[currentSymbol.ToString()];
            }
        }

        return result;
    }


    public static void Main(string[] args)
    {
        Solution solution = new Solution();

        string input = "MCMXCIV";
        int expectedOutput = 1994;
        int output = solution.RomanToIntV1(input);
        string result = output == expectedOutput ? "Passed" : "Failed";

        Console.WriteLine($"Input: {input}");
        Console.WriteLine($"Output: {output}");
        Console.WriteLine($"Expected Output: {expectedOutput}");
        Console.WriteLine($"Result: {GetResult(result)}");
    }

    private static string GetResult(string result)
    {
        if (result.ToUpper() == "PASSED")
        {
            return $"\u001b[32m{result}\u001b[0m"; // Green color
        }
        else
        {
            return $"\u001b[31m{result}\u001b[0m"; // Red color
        }
    }
}
