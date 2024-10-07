def decode_message(s: str, p: str) -> bool:
    # Lengths of message and pattern
    m, p_len = len(s), len(p)
    
    # DP table where dp[i][j] is True if s[:i] matches p[:j]
    dp = [[False] * (p_len + 1) for _ in range(m + 1)]
    
    # Empty pattern matches empty message
    dp[0][0] = True
    
    # If pattern contains *, it can match an empty message
    for j in range(1, p_len + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]
    
    # Fill the dp table
    for i in range(1, m + 1):
        for j in range(1, p_len + 1):
            if p[j - 1] == s[i - 1] or p[j - 1] == '?':
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
    
    return dp[m][p_len]