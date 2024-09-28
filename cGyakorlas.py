def harom():
    pass
    for i in range(21):
        print(i,)
def negy():
    pass
    for i in range(20,58,2):
        print(i,)

def ot():
    pass
    for i in range(77,-80,-4):
        print(i, end=-77)
def beolvas():
    szam = int(input("Kérem adjon meg egy számot! "))
    return szam

def hat():
    szam1 = beolvas()
    szam2 = beolvas()
# melyik a nagyobb?
    if szam2 < szam1:
        #csere
        atmenet = szam1
        szam1 = szam2
        szam2 = atmenet
    for i in range(szam1, szam2+1,-1):
        print(i, end=" ")
    #6.	Kérj be 2 számot, majd írasd ki a számokat a legkisebbtől a legnagyobbig! (a legnagyobbat is! Ha az első szám nagyobb, abban az esetben is a legkisebbtől a legnagyobbig írasd ki!)

def het():
    szam1 = beolvas()
    szam2 = beolvas()
    szorzat = szam1 * szam2

    if szorzat>0:
        for i in range(0, szorzat+1,1):
            print(i, end=" ")
    else:
        for i in range(0,szorzat-1,-1):
            print(i,end=" ")


   #for i in range():
        #print(i,)

def nyolc():
    #8.	Írd meg a fenti feladatot while és for ciklussal is!
    szam1 = beolvas()
    szam2 = beolvas()
    szorzat = szam1 * szam2
    while szorzat > 0:
        for i in range(0, szorzat+1,1):
            print(i, end=" ")
