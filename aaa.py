class Solution:
    def cuttingRope(self, n: int) -> int:
        if n == 1 or n == 2: return 1
        if n == 3: return 2

        d = dict()
        d[2] = 2
        d[3] = 3
        d[4] = 4
        i = j = 2
        while (i + j <= n):
            if d[i + 1] * d[j] > d[i] * d[j + 1]:
                i = i + 1
            else:
                j = j + 1
            d[i + j] = (int)(d[i]%(1e9+7) * d[j]%(1e9+7))%(1e9+7)
        return int(d[n])
s = Solution()
print(s.cuttingRope(1000))