import json

file=input("dammi un file da inserire: ")
cartella=input("la tua cartella esiste gia ? ").lower()

while cartella!="si"and cartella!="no":
    cartella=input("la tua cartella esiste gia ? ").lower()  

if cartella=="no":
    creazione=input("vuoi crearla? ").lower()
    while creazione!="si"and creazione!="no":
        creazione=input("vuoi crearla? ").lower()
    if creazione=="si":
        file=open("desktop","r")
        pc=json.load(file)
        nome=input("dammi il nome della cartella ")
        diz={"nome_cartella":nome,"contenuto":[]}
        #unico modo per creare una cartella con nome l'input inserito
        pc.append(diz)
        json.dump(diz,file)