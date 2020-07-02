def huffmandict(sym, prob, N=2, variance='min'):
    symbols = dict(zip(sym, prob))
    codewords={i:'' for i in sym}
    groups=[[i] for i in sorted(symbols, key=symbols.get, reverse=True)]
    n=len(groups)
    if variance=='min':
        while n>=N:
            for i in range(N):
                for j in groups[n-i-1]:
                    codewords[j]=str(i)+codewords[j]
            for i in range(N-1):
                groups[n-2]+=groups.pop()
                n-=1
            n1=n-2
            weight=lambda x:sum([symbols[i] for i in groups[x]])
            while weight(n1)<=weight(n1+1) and n1>=0:
                t=groups[n1]
                groups[n1]=groups[n1+1]
                groups[n1+1]=t
                n1-=1
        while n>=2:
            for i in range(n):
                for j in groups[n-i-1]:
                    codewords[j]=str(i)+codewords[j]
            for i in range(n-1):
                groups[n-2]+=groups.pop()
                n-=1
            n1=n-2
            weight=lambda x:sum([symbols[i] for i in groups[x]])
            while weight(n1)<=weight(n1+1) and n1>=0:
                t=groups[n1]
                groups[n1]=groups[n1+1]
                groups[n1+1]=t
                n1-=1
    else:
        while n>=N:
            for i in range(N):
                for j in groups[n-i-1]:
                    codewords[j]=str(i)+codewords[j]
            for i in range(N-1):
                groups[n-2]+=groups.pop()
                n-=1
            n1=n-2
            weight=lambda x:sum([symbols[i] for i in groups[x]])
            while weight(n1)<weight(n1+1) and n1>=0:
                t=groups[n1]
                groups[n1]=groups[n1+1]
                groups[n1+1]=t
                n1-=1
        while n>=2:
            for i in range(n):
                for j in groups[n-i-1]:
                    codewords[j]=str(i)+codewords[j]
            for i in range(n-1):
                groups[n-2]+=groups.pop()
                n-=1
            n1=n-2
            weight=lambda x:sum([symbols[i] for i in groups[x]])
            while weight(n1)<weight(n1+1) and n1>=0:
                t=groups[n1]
                groups[n1]=groups[n1+1]
                groups[n1+1]=t
                n1-=1
    avglen=0
    for i in symbols:
        avglen+=symbols[i]*len(codewords[i])
    return codewords, avglen
