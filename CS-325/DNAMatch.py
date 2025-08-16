def dna_match_topdown(DNA1, DNA2):
    dp = {}

    def lcs(a, b):
        if a == len(DNA1) or b == len(DNA2):
            return 0
        if (a, b) in dp:
            return dp[a, b]
        if DNA1[a] == DNA2[b]:
            dp[a, b] = 1 + lcs(a + 1, b + 1)

        else:
            dp[a, b] = max(lcs(a + 1, b), lcs(a, b + 1))
        return dp[a, b]
    return lcs(0, 0)


def dna_match_bottomup(DNA1, DNA2):
    a = len(DNA1)
    b = len(DNA2)
    dp = [[0] * (b + 1) for _ in range(a + 1)]
    for i in range(1, a + 1):
        for j in range(1, b + 1):
            if DNA1[i - 1] == DNA2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[a][b]
