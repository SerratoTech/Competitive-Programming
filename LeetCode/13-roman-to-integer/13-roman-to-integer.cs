public class Solution {
    public int RomanToInt(string s) {
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
}