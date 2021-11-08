n, b, h = map(int, input().split())
dp = [[[0 for i in range(b + 50)] for j in range(n + 1)] for i in range(h)]
if b <= n:
    dp[0][b][b] = 1
    for i in range(h - 1):
        for j in range(n + 1):
            for k in range(b + 50):
                if k > 1 and j + k - 1 <= n:
                    dp[i + 1][j + k - 1][k - 1] = (dp[i + 1][j + k - 1][k - 1] + dp[i][j][k]) % (1e9 + 7)
                if k < b + 50 and j + k + 1 <= n:
                    dp[i + 1][j + k + 1][k + 1] = (dp[i + 1][j + k + 1][k + 1] + dp[i][j][k]) % (1e9 + 7)
    print(int((sum(dp[h - 1][n])) % (1e9 + 7)))
else:
    print(0)
