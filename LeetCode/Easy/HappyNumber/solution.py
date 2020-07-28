class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        for i in range(10000):
            sum = 0
            while(n):
                d = n % 10
                n //= 10
                sum += d * d
            if sum == 1:
                return True
            else:
                n = sum
        return False
