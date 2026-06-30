
nom = "Jeriel"


def deviner_nombre_inverse(nom):
    print(f"{nom}, pense à un nombre entre 1 et 100 dans ta tête, je vais essayer de le deviner : ")

    borne_min = 1
    borne_max = 100
    compteur_essais = 0

    while borne_min <= borne_max:
        compteur_essais += 1

        proposition = (borne_min + borne_max) // 2
        reponse = input(f"{nom}, est-ce que votre nombre est {proposition} ? : ")

        if reponse == "Trop petit":
            borne_min = proposition + 1
        elif reponse == "Trop grand":
            borne_max = proposition - 1
        elif reponse == "Oui":
            print(f"J'ai gagné!, après {compteur_essais} essais.")
            break
        else:
            print(f"Tu dois répondre par Trop petit ou Trop grand, {nom}.")
            compteur_essais -= 1

deviner_nombre_inverse(nom)