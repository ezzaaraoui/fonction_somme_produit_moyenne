def somme(t):
        s=sum(t)
        return s
   



def produit(t):
    p=1
    for i in range(0,10):
        p=p*t[i]
    return p

def moyenne(t):
    m=somme(t)/3
        
    return m

def pos_neg(t):
    
    s1=""
    for i in range(0,10):
        if t[i]>0:
            s1=s1+" "+str(t[i])
    print(f"les elemnts positif est : {s1}")
    print(type(s1))


    s2=""
    for i in range(0,10):
        if t[i]<0:
            s2=s2+str(t[i])
    print(f"les elemnts negatif est : {s2}")


t=[]
for i in range(0,10):
    t.append(float(input(f"donner element de la case {i+1} : ")))

# print(somme(t))   
# # print(produit(t))
# # print(moyenne)
pos_neg(t)