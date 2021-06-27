def spirallyTraverse(matrix, r, c): 
        # code here 
        l=[]
        counti=countj=0
        s1=s2=s3=s4=0
        while True:
        #step1
            i=s1
            for j in range(s1,c-s1):
                l.append(matrix[i][j])
            counti+=1
            s1+=1
            #print(l)
            if counti == r:
                break
        #step2
            j=c-s2-1
            for i in range(s1,r-s1+1):
                l.append(matrix[i][j])
            countj+=1
            s2+=1
            #print(l)
            if countj == c:
                break
        #step3
            i=r-s3-1
            for j in range(c-1-s1,s1-2,-1):
                l.append(matrix[i][j])
            counti+=1
            s3+=1
            #print(l)
            if counti == r:
                break
        #step4
            j=s4
            for i in range(r-1-s1,s1-1,-1):
                l.append(matrix[i][j])
            countj+=1
            s4+=1
            #print(l)
            if countj == c:
                break
        return l