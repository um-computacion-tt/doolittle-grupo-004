import numpy as np
def doolittle(a,b):
    m,n = a.shape
    if (m !=n ):
        print("Asegurarse que el num de ecuaciones sea igual al de incognitas")
    else:
        l = np.zeros((n,n))
        u = np.zeros((n,n))
        s1 = 0
        s2 = 0
        for i in range (n):
            l[i][0] = a[i][0]
            u[i][i] = 1
        for j in range (1,n):
            u[0][j] = a[0][j] / l[0][0]
        for k in range(1,n) :
            for i in range (k,n):
                for r in range (k): s1 += l[i][r] * u[r][k]
                l[i][k] = a[i][k] - s1
                s1 = 0
            for j in range (k+1,n):
                for r in range (k): s2 += l[k][r] * u[r][j]#r columna i filas
                u[k][j] = (a[k][j] - s2) / l[k][k]
                s2 = 0
        y = np.zeros(n)
        s3 = 0
        y[0] = b[0] / l[0][0]
        for k in range(1,n):
            for r in range(k):
                s3 += l[k][r] * y[r]
            y[k] = (b[k]-s3) / l[k][k]
            s3 = 0
        x = np.zeros(n)
        s4 = 0
        x[n-1] = y[n-1]
        for k in range (n-2, -1, -1):
            for r in range (k+1,n):
                s4 += u[k][r] * x[r]
            x[k] = y[k] - s4
            s4=0
        for i in range (n):
            print ("x" + str(i+1) + "=", x[i])
        print ("x" "=", x)
if __name__ == '__main__':
    a = np.array([[2,4,2,6], [4,9,6,15], [2,6,9,18], [6,15,18,40]])
    b=np.array ([9,23,22,47])
    doolittle(a,b)


            



        
