"""
Module de calcul pour le projet Druide (Notation Polonaise Inverse).
Gère les opérations arithmétiques de base via une structure de pile.
"""

# Constante pour éviter l'erreur "Hardcoded password"
OPERATEURS = "+-*/"


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


def main():
    """
    Point d'entrée pour les tests du programme.
    """
    tests = ["3 5 +", "4 7 + 3 *", "3 4 7 + *", "10 4 + 2 /"]
    print("--- Tests Automatiques ---")
    for test in tests:
        res = calculer_npi(test)
        print(f"Calcul : {test} \t-> {res}")

    print("\n--- Test Manuel ---")
    val = input("Entrez votre calcul : ")
    print(f"Résultat : {calculer_npi(val)}")


if __name__ == "__main__":
    main()
