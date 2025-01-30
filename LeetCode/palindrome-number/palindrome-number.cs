public class Solution {
    public bool IsPalindrome(int x) {
        int num = x, reversedNum = 0;
        while (x > 0)
        {
            reversedNum = (reversedNum * 10) + (x % 10);
            x /= 10;
        }
        return num == reversedNum;
    }
}