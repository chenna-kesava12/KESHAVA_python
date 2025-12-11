class Solution:
    def isMatch(self, s, p):
        m, n = len(s), len(p)

        # dp[i][j] = whether s[i:] matches p[j:]
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[m][n] = True  # empty string matches empty pattern

        # Fill DP table from bottom-right to top-left
        for i in range(m, -1, -1):
            for j in range(n - 1, -1, -1):

                first_match = (i < m) and (p[j] == s[i] or p[j] == '.')

                # If next char is '*', handle zero or more repetitions
                if j + 1 < n and p[j + 1] == '*':
                    dp[i][j] = dp[i][j + 2] or (first_match and dp[i + 1][j])
                else:
                    dp[i][j] = first_match and dp[i + 1][j + 1]

        return dp[0][0]
        
        