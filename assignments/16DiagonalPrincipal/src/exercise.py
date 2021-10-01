def valoresDiagonal(matriz):
    diagonal=[]
    for i in range(len(matriz)):
        diagonal.append(matriz[i][i])
    return diagonal    
def main():
    matrices=[]
    f=int(input(""))
    c=int(input(""))
    if f==c:
        for i in range(f):
            matrices.append([])
            for j in range(c):
                datos=int(input(""))
                matrices[i].append(datos)
        elementosDiagonal=valoresDiagonal(matrices)
        print(elementosDiagonal)
    else:
        print("La matriz no es cuadrada")
if __name__=='__main__':
    main()