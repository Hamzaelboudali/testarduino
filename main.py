
chaine=str(input())
print(chaine)

n=len(chaine)
s=0
a=str(input("entrez un caractere :"))
for i in range(0,n):
    if chaine[i] == a:
        s+=1

print(s)

for i in range(0,n):
    if chaine[i] == a:
        Z=chaine.replace(a,"")
        break
print(Z)



'''chaine=str(input())

chaine=chaine.lower()
print(chaine)

chaine=chaine.upper()
print(chaine)

x=chaine.replace(" ","-")
print(x)

n=len(chaine)
p=n/2
p=int(p)
v=int(0)
for i in range(0,p):
    for j in reversed(range(p,n)):
        if x[i] ==x[n-j]:
            v = int(v)+1
if v == p :
    a="palindrome"
else:
    a="non palindrome"
print(a)
'''










##chaine=str(input())

'''chaine=str("hello world")

chaine=chaine.upper()

print(chaine)

x=chaine.replace("HELLO","SALUT")
print(x)
'''



'''def ajouter_etudiant():

  b=int(input("entrez le nombre d'etudiant"))
  M=0
  BULTTIN = open("BULTTIN.TXT", "w")
  print(f" le nbre etudiant {b} :", end=" ")
  for i in range(1,b+1):
    nom=str(input("nom  :"))
    prenom=str(input("prenom :"))
    note_fr=int(input("note francais :"))
    note_ag= int(input("note anglais :"))
    note_if= int(input("note informatique :"))
    BULTTIN.write(f"\n nom   :{nom}  prenom : {prenom} note francais  :{note_fr} note anglais :{note_ag} note informatique : {note_if}")
    M=float(note_fr+note_ag+note_if)/3
    if M>=16:
        mention="tres bien"
    elif M>=14:
        mention="bien"
    elif M>=12:
        mention="assez bien"
    elif M>=10:
        mention="passable"
    elif M<10:
        mention="faible"
    BULTTIN.write(f"\n la moyene {M:.2f} est le mention {mention}")

 ## AFFICHAGE
  with open("BULTTIN.TXT","r") as BULTTIN:
    contenu=BULTTIN.read()
    print(contenu)
  BULTTIN.close()


def afficher_etudiant():
    with open("BULTTIN.TXT", "r") as BULTTIN:
        contenu = BULTTIN.read()
        print(contenu)
def quiter():
   exit()
##programme 
print("MENU")
print("1-ajouter un etudiant :")
print("2-afficher les etudiants :")
print("3-quitter :")
c=int(input("Entrez votre choix :"))

if c==1:
    ajouter_etudiant()
if c==2:
    afficher_etudiant()
if c==3:
    quiter()


'''














'''age = int(input("Entrez l'âge du conducteur :"))

permis_depuis = int(input("Entrez le nbre d'années depuis le permis :"))

accidents = int(input("Entrez le nombre d'accidents :"))

if age < 25 and permis_depuis < 2:
    if accidents == 0:
        tarif = "Tarif Rouge"
    else:
        tarif = "Refusé"
elif (age < 25 and permis_depuis >= 2) or (age >= 25 and permis_depuis < 2):
    if accidents == 0:
        tarif = "Tarif Orange"
    elif accidents == 1:
        tarif = "Tarif Rouge"
    else:
        tarif = "Refusé"
else:  # age >= 25 et permis_depuis >= 2
    if accidents == 0:
        tarif = "Tarif Vert"
    elif accidents == 1:
        tarif = "Tarif Orange"
    elif accidents == 2:
        tarif = "Tarif Rouge"
    else:
        tarif = "Refusé"


print(f"Tarif d'assurance : {tarif}")



'''





'''# Vérifier si le conducteur est accepté
if tarif != "Refusé":
    duree_assurance = int(input("Entrez depuis combien de temps le conducteur est assuré chez la compagnie (en années) : "))
    if duree_assurance > 1:
        recompense = "Proposer un contrat de la couleur immédiatement la plus avantageuse"
    else:
        recompense = "Aucune récompense pour la fidélité"
else:
    recompense = "Le conducteur a été refusé, aucune récompense pour la fidélité"
    
##print(f"Récompense pour la fidélité : {recompense}")
'''
# Demander à l'utilisateur de saisir l'âge du conducteur
# Demander à l'utilisateur de saisir depuis combien de temps le conducteur est titulaire du permis
# Demander à l'utilisateur de saisir le nombre d'accidents pour lesquels le conducteur a été responsable
# Déterminer le tarif d'assurance en fonction des critères
# Afficher le tarif d'assurance et la récompense pour la fidélité








'''positif=[]
def positifs():
 print("Entrez le nombre d enties")
 w = int(input())
 for x in range(0,w):
    print(f"entrez la valeur de liste {x} : ",  end="")
    N=int(input())
    if N>=0:
     positif.append(N)

    listepositif = open("listepositif.TXT", "w")
    listepositif.write(f"{positif}")
    listepositif.close()

 with open("listepositif.TXT", "r") as listepositif:
  contenu = listepositif.read()
  print(contenu)



 for x in range(len(positif)):
    print(positif[x], end=" ")



positifs()

'''


'''## EX1 --FCT/
a=[]
b=[]
def remplisage(a):
##remplissage
 for x in range(0,4):
    print(f"entrez la valeur de liste {x} : ",  end="")
    N=int(input())
    a.append(N)


 for v in range(0,2):
    print(f"entrez la valeur de liste {v} : ",  end="")
    N=int(input())
    b.append(N)

def affichage(a):
##affichage
 print(f"\n-------------------------tableau 1----\n")
 for x in range(len(a)):
    print(a[x], end=" ")

 print(f"\n-------------------------tableau 2----\n")
 for v in range(len(b)):
    print(b[v],end=" ")


 print(f"\n-------------------------tableau 3----\n")
 z=[]
 for x in range(len(a)):
        o = a[x]
        z.append(o)
 for v in range(len(b)):
        o = b[v]
        z.append(o)

 for v in range(len(z)):
    print(z[v],end=" ")


remplisage(a)
remplisage(b)
affichage(a)

'''




'''a=[]
## remplissage
def remplissage(a):
 for x in range(0,10):
    print(f"entrez la valeur de liste {x} : ",  end="")
    N=int(input())
    a.append(N)

## affichage
def affichage(a):
 for x in range(0,10):
    print(a[x],end=" ")

##somme
def somme(a):
 s = int(0)
 for x in range(0, 10):
     s = s +a[x]
 return s

remplissage(a)
affichage(a)
print(f"la somme {somme(a)}")

'''













'''def factorial(a):
    p=int(1)
    for i in range(1,a+1):
        p=int(i)*int(p)
    return p
a=int(input("entrez un nombre"))
print(factorial(a))
'''




'''b=int(input())

FAMILLE = open("FAMILLE.TXT", "a")
print(f" le nbre d'enregistrement {b} :", end=" ")
for i in range(1,b+1):
    nom_de_famille=str(input("nom de famille :"))
    prenom_du_pere=str(input("prenom du pere :"))
    prenom_du_mere = str(input("prenom du mere :"))
    nombre_d_enfants=int(input("nombre d'enfants :"))
    FAMILLE.write(f"\n nom de famille  :{nom_de_famille}  prenom du pere : {prenom_du_pere} prenom du mere  :{prenom_du_mere} nombre d'enfants :{nombre_d_enfants} ")

    for x in range(1,nombre_d_enfants+1):
        prenom_des_enfants=str(input("prenom des enfants :"))
        FAMILLE.write(f"\n prenom des anfants : {prenom_des_enfants}")
## AFFICHAGE
with open("FAMILLE.TXT","r") as FAMILLE:
    contenu=FAMILLE.read()
    print(contenu)
FAMILLE.close()


'''





'''a=int(input())
INFORM = open("INFORM.TXT", "a")
print(f" le nbre d'enregistrement {a} :", end=" ")
for i in range(1,a+1):
    numero_de_matricule=int(input("entrez numero_de_matricule :"))
    nom=str(input("entrez le nom :"))
    prenom=str(input("entrez le prenom :"))

    INFORM.write(f"\nvotre numero_de_matricule :{numero_de_matricule}  votre nom : {nom} est votre prenom :{prenom}")

INFORM.close()

'''


'''nom=input()
age=int(input())

fichier = open("mon-fichier.txt","w")
fichier.write(f"votre nom {nom} est votre age {age}")

fichier.close()
'''
'''with open("mon-fichier.txt","r") as fichier:
    contenu=fichier.read()
    print(contenu)
'''


'''## 1)
import numpy as np
A=np.array([-3,5,6],
           [-1,2,2],
           [1,-1,-1])
print(A.dim)
print(A.shape)
print(A.shape[0])     ##(3,3)
## 2)
print(A[:,1])
A[0]
## 3)
print(A[0,2])
## 4)
print(A[1:,1:])
## 5)
print(np.sum(A,axis==0))
print(np.sum(A,axis=1))
A.sum(0)
## 6)
print(A+10)
## 7)
print(A+[1,2,3])
np.add(A,[1,2,5])
## 9)
A.transposer()
   A.T
## 10)
print(np.dot(A,A.T))
'''

'''## 1)
import numpy as np
x=np.array([1,2,3,4,5])
## 2)
print(type(x))
print(x.size)
## 3)
print(x[0])
print(x[-1])
## 4)
a=x[:3]
## 5)
b=x[[0,1,4]]
## 6)
print((x+10)*2)
## 7)
print(a+b)
## 8)
mlt2=x[x%2==0]
mult_int=np.where(x%2==0)
## 9)
x[0]=4

'''

'''##ex: 34
m=[]
for i in range(0,3):
    Ligne=[]
    for j in range(0,3):
        print(f" entrez la valeur de liste[{i}][{j}] :", end=" ")
        y=int(input())
        Ligne.append(y)
    m.append(Ligne)

for i in range(0,3):
    print(m[i])


a=[]
print(f"\n----------------liste----\n")

for x in range(0,3):
    for v in range(0,3):
        a.append(m[x][v])

for x in range(len(a)):
    print(a[x], end=" ")

print(f"\n------------trier le tableau ----\n",  end="")
p=0
k=int(0)
for x in range(0,9):
    for v in range(int(x)+1,9):
        if a[x]>a[v]:
            k=a[x]
            a[x]=a[v]
            a[v]=k

for x in range(len(a)):
    print(a[x], end=" ")

n=[]
k=0
for i in range(0,3):
    Ligne = []
    for j in range(0,3):
        Ligne.append(a[k])
        k = k + 1

    n.append(Ligne)

print("\n----------------matrice triée----")
for i in range(0,3):
    print(n[i])

'''
'''m = []
for i in range(0, 3):
    Ligne = []
    for j in range(0, 3):
        print(f"Entrez la valeur de liste[{i}][{j}]: ", end=" ")
        y = int(input())
        Ligne.append(y)
    m.append(Ligne)

# Affichage de la matrice d'origine
for i in range(0, 3):
    print(m[i])

a = []

# Collecte des éléments de la matrice dans une liste a
for x in range(0, 3):
    for v in range(0, 3):
        a.append(m[x][v])

# Affichage des éléments de la liste a
print("\n-------------------------liste----\n")
for x in range(len(a)):
    print(a[x], end=" ")

# Tri des éléments de la liste a
print("\n----------------trier-----\n", end="")
for x in range(0, 9):
    for v in range(x + 1, 9):
        if a[x] > a[v]:
            k = a[x]
            a[x] = a[v]
            a[v] = k

# Affichage des éléments triés de la liste a
for x in range(len(a)):
    print(a[x], end=" ")

n = []
k = 0

# Création d'une nouvelle matrice triée
for i in range(0, 3):
    Ligne = []
    for j in range(0, 3):
        Ligne.append(a[k])
        k = k + 1
    n.append(Ligne)

# Affichage de la matrice triée
print("\n----------------matrice triée----")
for i in range(0, 3):
    print(n[i])

'''


'''m=[]
for i in range(0,4):
    Ligne=[]
    for j in range(0,4):
        print(f" entrez la valeur de liste[{i}][{j}] :", end=" ")
        y=int(input())
        Ligne.append(y)
    m.append(Ligne)
for i in range(0,4):
    print(m[i])

##la somme de la colonne:
s=0
for i in range(0,4):

    for j in range(0,4):
        s+=int(m[j][i])
    print(f"la somme de colonne {i} = {s}")
    s=int(0)


'''




'''ex: 33
m=[]
for i in range(0,4):
    Ligne=[]
    for j in range(0,4):
        print(f" entrez la valeur de liste[{i}][{j}] :", end=" ")
        y=int(input())
        Ligne.append(y)
    m.append(Ligne)
for i in range(0,4):
    print(m[i])

##la somme de la ligne:
s=0
k=0
for i in range(0,4):

    for j in range(0,4):
        s+=int(m[i][j])
    print(f"la somme de ligne {i} = {s}")
    s=int(0)

'''








'''a=[]
## remplissage
for x in range(0,11):
    print(f"entrez la valeur de liste {x} : ",  end="")
    N=int(input())
    a.append(N)
## affichage
for x in range(0,11):
    print(a[x],end=" ")
 ##
for x in range(0,11):
    if a[x]>0:
        print(a[x],"positive")
    else:
        print(a[x],"negatif")

'''


'''
ex,31
m=[]
for i in range(0,3):
    Ligne=[]
    for j in range(0,3):
        print(f" entrez la valeur de liste[{i}][{j}] :", end=" ")
        y=int(input())
        Ligne.append(y)
    m.append(Ligne)
for i in range(0,3):
    print(m[i])

for i in range(0,3):
    print()
for i in range(0,3):
    for v in range(0,3):
        if i == v:
            m[i][v]=0



for i in range(0,3):
    print()
    for v in range(0,3):
        print(m[i][v],end=" ")'''

'''###ex:32
m=[]
for i in range(0,3):
    Ligne=[]
    for j in range(0,3):
        print(f" entrez la valeur de liste[{i}][{j}] :", end=" ")
        y=int(input())
        Ligne.append(y)
    m.append(Ligne)

n=[]
for i in range(0,3):
    Ligne=[]
    for j in range(0,3):
        print(f" entrez la valeur de liste[{i}][{j}] :", end=" ")
        y=int(input())
        Ligne.append(y)
    n.append(Ligne)

for i in range(0,3):
    print(m[i])
for i in range(0,3):
    print(n[i])

p=[]
s=0
for i in range(0,3):
    Lingne=[]
    for j in range(0,3):
        s=m[i][j]+n[i][j]
        Lingne.append(s)
    p.append(Lingne)

for i in range(0,3):
    print(p[i])
'''


'''ex1:liste
m=[]
s=0
for i in range(0,3):
    Ligne=[]

    for j in range(0,3):
        print(f" entrez la valeur de liste[{i}][{j}] :", end=" ")
        y=int(input())
        Ligne.append(y)

    m.append(Ligne)

for i in range(0,3):
    print(m[i])
for i in range(0,3):

    for j in range(0,3):
        s+=m[i][j]
print(f" la somme de la liste {s}")

'''





'''m=[]
for i in range(0,4):
    Ligne=[]

    for j in range(0,3):
        print(f" entrez la valeur de liste[{i}][{j}] :", end=" ")
        y=int(input())
        Ligne.append(y)

    m.append(Ligne)

##AFFICHAGE PAR LIGNE:
for i in range(0,4):
    print(m[i])
##AFFICHAGE PAR CELLULE :
for i in range(0,4):
    print()
    print(m[i][j], end=" ")

'''

'''a=[]


##remplissage
for x in range(0,4):
    print(f"entrez la valeur de liste {x} : ",  end="")
    N=int(input())
    a.append(N)

b=[]
for v in range(0,2):
    print(f"entrez la valeur de liste {v} : ",  end="")
    N=int(input())
    b.append(N)

##affichage
print(f"\n-------------------------tableau 1----\n")
for x in range(len(a)):
    print(a[x], end=" ")

print(f"\n-------------------------tableau 2----\n")
for v in range(len(b)):
    print(b[v],end=" ")


z=[]
s=0
y=0
print(f"\n-------------------------tableau 3----\n")

for x in range(len(a)):
    for v in range(len(b)):
     o=a[x]*b[v]
     s+=o
print(f"\nla somme est : {s}")

'''





'''a=[]
print("entrez la taille de liste : ")
t=int(input())
##remplissage
for x in range(0,t):
    print(f"entrez la valeur de liste {x} : ",  end="")
    N=int(input())
    a.append(N)
##affichage
print(f"\n-------------------------tableau 1----\n")
for x in range(len(a)):
    print(a[x], end=" ")

k=int(input("\n entrez la valeur de k : "))
y = int(0)
for x in range(0,t):
    if k == a[x]:
        y=int(1)

if y==1:
    print(f"x = {k} existe dans la liste , ")
else:
    print(f"x = {k} n'existe pas dans la liste , ")


'''
















'''nombres=list(range(0,11))

for i in range(0,11):
    nombres[i]=nombres[i]+1
    nombres.append(11)
    ##nombres.append(12)
    nombres.append(13)
    nombres.insert(len(nombres),12)
    print(nombres[0])
    print(nombres[:2])

    paires=[]
    impaires=[]
    for i in nombres:
      if i%2==0:
       paires.append(i)
    else:
         impaires.append(i)
    nombres.remove(5)
    nombres.reverse()
    a=int(input("saisir un nbre"))
    if a in nombres:
     print("exit")
    else:
     print("not exit")

'''








'''
def reduction(age):
    if age<10 :
        return 0.5
    elif age>10 and age<18:
        return 0.3
    elif age>60:
        return 0.2
    else :
        return 0

def montant(age,montant):
    p=montant-montant*reduction(age)
    return p

age=int(input("entrez votre age"))
mnt=float(input("entrez le montant"))
print("votre age est",age)
print("montant totale",montant(age,mnt))


'''







##n=int(input())
'''n=[]
print("entrez la valeur de n :")
n=int(input())
s=0
for i in range(1,n+1):
    s+=(2*i-1)**2

print(f"la valeur de la somme : {s}")
'''

'''p=4
def mult(x):
    res=p*x
    return res
print(p)
print(mult(3))
print(p)
'''

'''p=4
def mult(x):
    global p
    p=5
    res=p*x
    return res
print(p)
print(mult(3))
print(p)

la solusion de ex2:
1 :4....12.....4
2: 4....15.....4
3: 4....15.....4
'''





'''a=[]
p=0
q=0
for x in range(len(N))
    print(f"entrez la valeur de liste {x} : ",  end="")
    N=int(input())
    a.append(N)


for x in range(len(N)):
    print(N[x],end=" ")'''

'''print(f"la liste 1 : {}")
print(f"la liste 2 : {}")
print(f"la somme de 2 liste {}")'''

'''a=[]
print("entrez la taille de liste : ")
t=int(input())
for x in range(0,t):
    print(f"entrez la valeur de liste {x} : ",  end="")
    N=int(input())
    a.append(N)


b=[]
for v in range(0,t):
    print(f"entrez la valeur de liste {v} : ",  end="")
    N=int(input())
    b.append(N)

print(f"\n-------------------------tableau 1----\n")
for v in range(len(a)):
    print(a[x], end=" ")

print(f"\n-------------------------tableau 2----\n")
for v in range(len(b)):
    print(b[x],end=" ")


z=[]
print(f"\n-------------------------tableau 3----\n")
for x in range(len(b)):
    o=a[x]+b[x]
    z.append(o)
    print(z[x],end=" ")

'''


'''a=[]
s=0
p=0
nn=0
for x in range(0,6):
    print(f"entrez la valeur de liste {x} : ",  end="")
    N=int(input())
    a.append(N)
    s=s+N
    if a[x]>0:
        p=p+1
    if a[x]<0:
        nn=nn+1

for x in range(len(a)):
    print(a[x],end=" ")

print(f"\nla somme de la liste : {s}")
print(f"les nombres positife {p}")
print(f"les nombres negatifs {nn}")
'''





'''a=[]
for x in range(0,6):
    print(f"entrez la valeur de liste {x} : ",  end="")
    N=input()
    a.append(N)

for x in range(len(a)):
    print(a[x],end=" ")''''''



''for x in range(1,9):
    print()
    for x in range(1, 8):
      print(" ")
      for v in range(1,int(x)):
          print("*", end="")''''''

for x in range(1,9):
    print()
    for v in range(1,9-int(x)):
        print(" ",end="")

    for z in range(1,int(x)*2):
      print("*",end="")

for x in (range(1,9)):
    print()
    for v in range(1,int(x)):
      print(" ",end="")

    for z in range(1,18-(int(x)*2)):
      print("*",end="")'''






''''
for x in reversed(range(0,10)):
    print()
    for v in range(1,11-int(x)):
        print("*",end="")

'''
'''for x in range(1,11):
    print()
    for v in range(1,int(x)):
        print("*",end="")'''




'''for x in range(1,11):
    print()
    for v in range(1,11-int(x)):
        print("*",end="")'''




'''## la table de pytagore:
for x in range(1,11):
    print()
    for v in range(1,11):
        h=int(x)*int(v)
        print(f"{h}\t",end="")'''

'''
for x in range(1,6):
    print()
    for v in range(1,11):
        print("*",end="")
        
print("entrez un nbre :")
x=int(input())
f=0
s=0
m=99
y=0
g=998
##min=1
while x!=999:
    if(x!=999):
        f += 1
        s = s + x
        if x<m:
            m =x
        if x>0:
            y=y+x
            g=min(g,x)
    print("entrez un nbre")
    x=int(input())



print(f"la nombre totale de la suite {f}")
print(f"la somme de la suite : {s}")
print(f"le minimum de la suite : {m}")
print(f"la somme strictement positive de la suite : {y}")
print(f"le minimum positive de la suite : {g}")
'''






'''matieres=['info','pyton','algo','statistique']
print(matieres[-3:-2])'''

'''x=int(input("Entrez un nbre :"))
f=int(1)
  
for v in range(1,x+1):
   print(f"{v}*")
   f=int(v)*int(f)
   if v>x :
    print(f"{v}")

print(f"={f}")'''

'''x = int(input("Entrez un nombre :"))
f = 1

for v in range(1, x + 1):
    print(v, end="")
    if v < x:
        print("*", end="")
    f *= v
print(" =", f)'''
