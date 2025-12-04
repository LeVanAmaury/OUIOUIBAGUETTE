"""
Module de calcul pour le projet Druide (Notation Polonaise Inverse).
Lit les calculs depuis un fichier texte et affiche les résultats.
"""

import sys

# Constante pour les opérateurs supportés
OPERATEURS = "+-*/"
# Nom du fichier d'entrée par défaut
FICHIER_INPUT = "calculs.txt"


def executer_op(val_a, val_b, operator):
    """
    Exécute l'opération mathématique sur deux nombres.
    Retourne None en cas d'erreur (division par zéro).
    """
    if operator == '+':
        return val_a + val_b
    if operator == '-':
        return val_a - val_b
    if operator == '*':
        return val_a * val_b
    if operator == '/':
        if val_b == 0:
            return None
        return int(val_a / val_b)
    return None


def traiter_op(pile, operator):
    """
    Gère la logique de dépilement et d'appel au calcul.
    Modifie la pile directement.
    """
    if len(pile) < 2:
        return "Erreur : Pas assez d'opérandes"

    val_b = pile.pop()
    val_a = pile.pop()
    res = executer_op(val_a, val_b, operator)

    if res is None:
        return "Erreur : Division par zéro"

    pile.append(res)
    return None


def calculer_npi(expression):
    """
    Fonction principale qui parse la chaîne et orchestre le calcul.
    """
    pile = []
    tokens = expression.split()

    for token in tokens:
        # Vérifie si le token est un nombre (gère les négatifs)
        if token.replace('-', '', 1).isdigit():
            pile.append(int(token))
        elif token in OPERATEURS:
            err = traiter_op(pile, token)
            if err:
                return err
        else:
            return "Erreur : Caractère inconnu"

    if len(pile) == 1:
        return pile[0]
    return "Erreur : Expression mal formée"


def traiter_fichier(chemin):
    """
    Lit le fichier ligne par ligne et lance le calcul pour chaque ligne.
    Gère l'erreur si le fichier n'existe pas.
    """
    try:
        with open(chemin, 'r', encoding='utf-8') as f_in:
            print(f"--- Lecture du fichier : {chemin} ---")
            for ligne in f_in:
                ligne = ligne.strip()
                if ligne:
                    res = calculer_npi(ligne)
                    print(f"Entrée : {ligne:<20} -> Résultat : {res}")
    except FileNotFoundError:
        print(f"Erreur critique : Le fichier '{chemin}' est introuvable.")
    except IOError:
        print("Erreur critique : Impossible de lire le fichier.")


def main():
    """
    Point d'entrée. Vérifie si un argument est passé, sinon utilise le défaut.
    """
    fichier = FICHIER_INPUT
    
    # Permet de lancer : python script.py mon_fichier.txt
    if len(sys.argv) > 1:
        fichier = sys.argv[1]

    traiter_fichier(fichier)


if __name__ == "__main__":
    main()
