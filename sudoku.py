import sys
def s(row, col, value):
    result = (((row-1)*81) + ((col-1)*9) + value)
    return(result)
    
def main():
    filename = sys.stdin
    file = open(filename,"r")
    row = 1
    knownValues = []
    for line in file:
        lst = line.split()
        for colidx in range(len(lst)):
            if lst[colidx] != 'x':
                knownValues.append(s(row, colidx +1, int(lst[colidx])))
        row += 1

    print("p cnf ",729,8829+len(knownValues))
    for x in knownValues:
        print(x, 0)
    
    for x in range(1,10):
        for y in range (1,10):
            val = ''
            for z in range (1,10):
                val = val + ' ' + str(s(x,y,z))
            print(val + ' 0')
            
    for y in range(1,10):
        for z in range(1,10):
            for x in range(1,9):
                for i in range(x+1, 10):
                    print(-1*s(x,y,z), -1*s(i,y,z), 0)
    
    for x in range(1,10):
        for z in range(1,10):
            for y in range(1,9):
                for i in range(y+1, 10):
                    print(-1*s(x,y,z), -1*s(x,i,z), 0)
    
    for z in range(1,10):
        for i in range(0,3):
            for j in range(0,3):
                for x in range(1,4):
                    for y in range(1,4):
                        for k in range(y+1,4):
                            print(-1*s(3*i+x,3*j+y,z), -1*s(3*i+x, 3*j+k,z), 0)
                            
    for z in range(1,10):
        for i in range(0,3):
            for j in range(0,3):
                for x in range(1,4):
                    for y in range(1,4):
                        for k in range(x+1,4):
                            for l in range(1,4):
                                print(-1*s(3*i+x,3*j+y,z), -1*s(3*i+k, 3*j+l,z), 0)    

if __name__ == '__main__':
    main()