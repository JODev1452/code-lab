
import random

def jeu_justeprix(nom_joueur):
    nombre_secret = random.randint(1, 30)
    print(f"Bienvenue dans le Juste Prix, {nom_joueur} !")
    
    essais = 0 

    while True:
        try:
            proposition = int(input("Quelle est ta proposition ? "))
        except ValueError:
            print("Oups ! Tu dois entrer un nombre entier.")
            continue
        
        if proposition < 1 or proposition > 30:
            print("Hors-jeu ! Ta proposition doit être comprise entre 1 et 30.")
            continue  

        
        essais += 1

        if proposition == nombre_secret:
            print(f"🎉 Félicitations {nom_joueur}, tu as trouvé le juste prix en {essais} essai(s) !")
            break  
        elif proposition < nombre_secret:
            print("C'est PLUS grand !")
        else:
            print("C'est PLUS petit !")

# Lancement
nom = "Jeriel"
jeu_justeprix(nom)