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

class Evenement:

    def __init__(self, numero, nom, description):
        self.numero = int(numero)
        self.nom = nom
        self.description = description
        self.notes = []

    def get_nom(self):
        return self.nom

    def get_numero(self):
        return self.numero

    def get_description(self):
        return self.description

    def get_notes(self):
        return self.notes
    
    def ajoute_note(self, note):
        self.notes.append(note)

    def supprime_note(self, position_note):
        self.notes.pop(position_note)

    def nettoie_note(self):
        self.notes = []

class Solveur:

    def __init__(self, nom, type):
        self.nom = nom
        self.type = type
        self.possessions = []
        self.notes = []
        self.etat = []

    def get_nom(self):
        return self.nom

    def get_type(self):
        return self.type

    def get_possessions(self):
        return self.possessions
    
    def ajoute_possession(self, possession):
        self.possessions.append(possession)

    def supprime_possession(self, position_objet):
        self.possessions.pop(position_objet)

    def nettoie_possession(self):
        self.possessions = []

    def get_notes(self):
        return self.notes
    
    def ajoute_note(self, note):
        self.notes.append(note)

    def supprime_note(self, position_note):
        self.notes.pop(position_note)

    def nettoie_note(self):
        self.notes = []

    def get_etats(self):
        return self.etat
    
    def ajoute_etat(self, etat):
        self.etat.append(etat)

    def supprime_etat(self, position_etat):
        self.etat.pop(position_etat)

    def nettoie_etat(self):
        self.etat = []


# DONE

# création du plateau
# affectation d'un nombre random allant de 0 à 99 (jamais deux fois le même) sur chaque cases du plateau

# création des évènements
# description
# notes


try:
    plateau_de_jeu = Plateau()
    plateau_de_jeu.affiche_plateau()

    evenement_1 = Evenement(1,"nom_test","description_test")
    evenement_1.ajoute_note("Note 1")
    evenement_1.ajoute_note("Note 2")
    print(f"numero_event : {evenement_1.get_numero()}\n")
    print(f"nom_event : {evenement_1.get_nom()}\n")
    print(f"description_event : {evenement_1.get_description()}\n")
    print("notes_event :")
    for note in evenement_1.get_notes():
        print(f" - {note}")
    EntreePourContinuer()

    solveur_1 = Solveur("solveur", 2)
    solveur_1.ajoute_note("Note 1")
    solveur_1.ajoute_note("Note 2")
    solveur_1.ajoute_etat("Etat 1")
    solveur_1.ajoute_possession("Objet 1")
    solveur_1.ajoute_possession("Objet 2")
    print(f"nom_solveur : {solveur_1.get_nom()}\n")
    print(f"type_solveur : {solveur_1.get_type()}\n")
    print("etats_solveur :")
    for etat in solveur_1.get_etats():
        print(f" - {etat}")
    print("possessions_solveur :")
    for objet in solveur_1.get_possessions():
        print(f" - {objet}")
    print("notes_solveur :")
    for note in solveur_1.get_notes():
        print(f" - {note}")
    EntreePourContinuer()
    
except Exception as error:
    WriteErrorInErrorLog(error)

# TODO

# création du solveur
# etat
# type
# possessions
# notes joueur

# création du scripteur
# etat
# possessions
# notes joueur

# création des équipes
# position
# points
# notes equipe
# solveur
# scripteur
