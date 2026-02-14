class MinJumps:

    def solve(self, arr):
        n=len(arr)
        if arr[0]==0:
            return -1

        maxReach=arr[0]
        step=arr[0]
        jump=1

        for i in range(1,n):
            if i==n-1:
                return jump

            if i+arr[i]>maxReach:
                maxReach=i+arr[i]

            step-=1

            if step==0:
                jump+=1
                if i>=maxReach:
                    return -1
                step=maxReach-i
        return -1

obj = MinJumps()
print(obj.solve([1,3,5,8,9,2,6,7,6,8,9]))
