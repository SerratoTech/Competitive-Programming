public class Solution {
    public bool IsValid(string s) {
        Stack<char> stack = new Stack<char>();

        for (int i = 0; i < s.Length; ++i)
        {
            char c = s[i];

            if (c == '(' || c == '[' || c == '{')
            {
                stack.Push(c);
            }
            else
            {
                if (stack.Count == 0)
                {
                    return false;
                }

                char top = stack.Pop();
                
                if (c == ')' && top != '(' ||
                    c == ']' && top != '[' ||
                    c == '}' && top != '{')
                {
                    return false;
                }
            }
        }

        return stack.Count == 0;
    }

    public static void Main(string[] args)
    {
        Solution solution = new Solution();

        string input = Console.ReadLine();
        bool result = solution.IsValid(input);
        Console.WriteLine(AssertResult(result, "Passed", "Failed"));
    }

    private static string AssertResult(bool assertion, string passed, string failed)
    {
        if (assertion)
        {
            return $"\u001b[32m{passed}\u001b[0m"; // Green color
        }
        else
        {
            return $"\u001b[31m{failed}\u001b[0m"; // Red color
        }
    }
}