class Solution:
    def grayCode(self, n: int) -> List[int]:
        # formula for gray code i ^ i//2
        result = []
        for i in range(1<<n):
            result.append(i^i>>1)
        return result