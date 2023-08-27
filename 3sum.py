class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        r = set()

        n, p, z = [], [], []
        for each in nums:
            if each == 0:
                z.append(each)
            elif each < 0:
                n.append(each)
            else:
                p.append(each)

        N, P = set(n), set(p)

        if z:
            for each_n in N:
                if -1*each_n in P:
                    r.add((each_n, 0, -1*each_n))

        if len(z) >= 3:
            r.add((0, 0, 0))

        for i in range(len(n)):
            for j in range(i+1, len(n)):
                t = -1*(n[i]+n[j])
                if t in p:
                    r.add(tuple(sorted([n[i], n[j], t])))

        for i in range(len(p)):
            for j in range(i+1, len(p)):
                t = -1*(p[i]+p[j])
                if t in n:
                    r.add(tuple(sorted([p[i], p[j], t])))
        
        return r