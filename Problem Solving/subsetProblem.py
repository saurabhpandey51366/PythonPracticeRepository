class Solution:
    def help(self, n, arr, t, dp):
        if dp[n][t] != -1:
            return dp[n][t]
        if t == 0:
            return True
        if n == 0:
            return t == arr[n]
        nottake = self.help(n - 1, arr, t, dp)
        take = False
        if arr[n] <= t:
            take = self.help(n - 1, arr, t - arr[n], dp)

        dp[n][t] = take or nottake

        return dp[n][t]

    def isSubsetSum(self, N, arr, sum):
        dp = [[-1 for i in range(sum + 1)] for j in range(N)]

        return self.help(N - 1, arr, sum, dp)