import random
import os
import time
import traceback

def EntreePourContinuer():
        input("(Appuyez sur entrée pour continuer)")
        ClearConsole()

def ClearConsole():
    # Vérifier le système d'exploitation pour déterminer la commande appropriée
    os.system("cls" if os.name == "nt" else "clear")

def WriteErrorInErrorLog(erreur):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    chemin_du_fichier = os.path.join(dir_path, "ErrorLog.txt")
    date_et_heure = time.strftime("%Y-%m-%d %H:%M")
    erreur = traceback.format_exc()
    with open(chemin_du_fichier, "a") as fichier:
        fichier.write(
            "-----------------------------------------"
            "------------------------------------------"
            "------------------------------------------"
            "------------------------------------------"
            f"---------\n{date_et_heure}\nDébut du Log\n\n"
        )
        fichier.write(f"{erreur}")
        fichier.write(
            "\nFin du Log\n-----------------------------"
            "-------------------------------------------"
            "-------------------------------------------"
            "-------------------------------------------"
            "------------------\n"
        )
    
    
class Plateau:

    def __init__(self):
        plateau = []
        nombres_possibles = []

        # remplissage du tableau de nombres possibles
        nombres_possibles = list(range(100)) 
        
        # utilisation du tableau de nombres possibles pour remplissage du plateau
        for numero_ligne in range(0, 9):
            ligne = []

            for position_du_numero_dans_la_ligne in range(0, 9):
                position_aleatoire = random.randint(0, (len(nombres_possibles) - 1))
                ligne.append(nombres_possibles.pop(position_aleatoire))

            plateau.append(ligne)
        
        self.plateau = plateau

    def affiche_plateau(self):
        for i in range(0, len(self.plateau)):

            for j in range(0, len(self.plateau[i])):
                if self.plateau[i][j] <= 9:
                    print(f"0{self.plateau[i][j]}", end="")
                else:
                    print(f"{self.plateau[i][j]}", end="")
                print("", end=" ")

            print("")
        EntreePourContinuer()



# création du plateau
# affectation d'un nombre random allant de 0 à 99 (jamais deux fois le même) sur chaque cases du plateau
try:
    plateau_de_jeu = Plateau()
    plateau_de_jeu.affiche_plateau()
except Exception as error:
    WriteErrorInErrorLog(error)


# création des évènements
# description
# notes

# création du solveur
# effet
# possessions
# notes joueur

# création du scripteur
# effet
# possessions
# notes joueur

# création des équipes
# position
# points
# notes equipe
# solveur
# scripteur
