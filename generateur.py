
import random
import string

def generer_mot_de_passe (longueur):
    if longueur < 4:
        print("Le mot de passe doit contenir au moins 4 caractères.")

        return ""

    minuscule = random.choice(string.ascii_lowercase)
    majuscule = random.choice(string.ascii_uppercase)
    chiffre = random.choice(string.digits)
    symbole = random.choice(string.punctuation)

    tous_les_caracteres = string.ascii_letters + string.digits + string.punctuation

    reste = [random.choice(tous_les_caracteres) for _ in range (longueur - 4)]

    mot_de_passe_liste = [minuscule, majuscule, chiffre, symbole] + reste
    random.shuffle(mot_de_passe_liste)


    return "".join(mot_de_passe_liste)


nom = "Jeriel"

if __name__ == '__main__':
    longueur = int(input(f"{nom}, quelle longueur veux-tu pour ton mot de passe ? : "))
    mot_de_passe = generer_mot_de_passe(longueur)

    if mot_de_passe != "":
        print(f"Voici votre mot de passe {mot_de_passe}, {nom} !")
    else:
        print("IL Y A UNE ERREUR DANS LA GENERATION !")