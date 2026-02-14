class MergeSortedArrays:

    def nextGap(self, g):
        if g<=1:
            return 0
        return (g//2)+(g%2)

    def solve(self, a, b):
        n=len(a); m=len(b)
        gap=self.nextGap(n+m)

        while gap>0:
            i=0
            while i+gap < n:
                if a[i] > a[i+gap]:
                    a[i],a[i+gap]=a[i+gap],a[i]
                i+=1

            j = gap-n if gap>n else 0
            i = 0 if gap<=n else gap-n

            while i<n and j<m:
                if a[i] > b[j]:
                    a[i],b[j]=b[j],a[i]
                i+=1; j+=1

            if j<m:
                j=0
                while j+gap<m:
                    if b[j] > b[j+gap]:
                        b[j],b[j+gap]=b[j+gap],b[j]
                    j+=1
            gap=self.nextGap(gap)

        return a,b

obj = MergeSortedArrays()
print(obj.solve([2,4,7,10],[2,3]))
