class CommonElements:

    def solve(self,a,b,c):
        i=j=k=0
        res=[]
        while i<len(a) and j<len(b) and k<len(c):
            if a[i]==b[j]==c[k]:
                if len(res)==0 or res[-1]!=a[i]:
                    res.append(a[i])
                i+=1; j+=1; k+=1
            elif a[i]<b[j]:
                i+=1
            elif b[j]<c[k]:
                j+=1
            else:
                k+=1
        return res if res else [-1]

obj = CommonElements()
print(obj.solve([1,5,10,20,40,80],
                [6,7,20,80,100],
                [3,4,15,20,30,70,80,120]))
