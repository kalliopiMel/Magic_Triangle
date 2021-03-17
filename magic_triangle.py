# this is an exercise from math-olympiads found on linkedIn
# Magic Triangle 5
# https://www.learn-with-math-games.com/triangle-puzzles.html

arithmoi=[1,2,3,4,5,6,7,8,9]



lista=[]
for i in arithmoi:
    arithmoi.remove(i)
    for j in arithmoi:
        if i+j>14: break
        arithmoi.remove(j)
        for k in arithmoi:
           if i + j + k > 16: break
           arithmoi.remove(k)
           for l in arithmoi:
               if i+j+k+l==17:
                   lista.append([i, j, k, l])
               elif i+j+k+l > 17: break
           arithmoi.append(k)
           arithmoi.sort()
        arithmoi.append(j)
        arithmoi.sort()
    arithmoi.append(i)
    arithmoi.sort()


lista2=[]
for x in lista:
    index_x=lista.index(x)
    lista.remove(x)
    for y in lista:
        if x[3]==y[0] and (not any(i in y for i in x[0:3])):
            lista2.append([x,y])

    lista.insert(index_x,x)



lista3=[]
for x in lista2:
    for y in lista:
        bool = (not any(i in x[0][1:4] for i in y)) and (not any(i in x[1][1:3] for i in y))
        if x[0][0]==y[3] and x[1][3]==y[0] and bool:
            lista3.append([x[0],x[1],y])




lista4=[]
for x in lista3:
    x1=x[0][0]
    x2=x[1][0]
    x3=x[2][0]
    if [x1,x2,x3] not in lista4:
        if lista4!=[]:
            for z in range(0,len(lista4)):
                if not all(i in [x1,x2,x3] for i in lista4[z]):
                    lista4.append([x1,x2,x3])
        else: lista4.append([x1,x2,x3])





print("the 3 numbers that fill in the 3 nodes of triangle's corners are:",lista4[0][0],",",lista4[0][1],",",lista4[0][2])

"""""
print("lista",len(lista))
print("lista2",len(lista2))
print("lista3",len(lista3))
print("prin eixa 9 72 504 3024 216, enw twra",a,b,g,d,dd)
print(e,f,ff)"""
