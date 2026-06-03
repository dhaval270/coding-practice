class Solution(object):
    def earliestFinishTime(self, lst, ldu, wst, wdu):
        """
        :type landStartTime: List[int]
        :type landDuration: List[int]
        :type waterStartTime: List[int]
        :type waterDuration: List[int]
        :rtype: int
        """
        ans = float("inf")
        mln = float("inf")
        mnw = float("inf")

        for i in range(len(lst)):
            mln = min(mln, lst[i] + ldu[i])

        for i in range(len(wst)):
            ans = min(ans, max(mln, wst[i]) + wdu[i])

        for i in range(len(wst)):
            mnw = min(mnw, wst[i] + wdu[i])

        for i in range(len(lst)):
            ans = min(ans, max(mnw, lst[i]) + ldu[i])

        return ans