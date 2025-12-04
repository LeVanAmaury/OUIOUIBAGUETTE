def executer_op(a, b, op):
    if op == '+': return a + b
    if op == '-': return a - b
    if op == '*': return a * b
    if op == '/' and b != 0: return int(a / b)
    return None

def traiter_op(pile, op):
    if len(pile) < 2: return "Erreur : Pas assez d'opérandes"
    b = pile.pop()
    a = pile.pop()
    res = executer_op(a, b, op)
    if res is None: return "Erreur : Division par zéro"
    pile.append(res)
    return None

def calculer_npi(expression):
    pile = []
    for token in expression.split():
        if token.replace('-', '', 1).isdigit():
            pile.append(int(token))
        elif token in "+-*/":
            err = traiter_op(pile, token)
            if err: return err
        else: return "Erreur : Caractère inconnu"
    return pile[0] if len(pile) == 1 else "Erreur : Expression mal formée"

def main():
    tests = ["3 5 +", "4 7 + 3 *", "3 4 7 + *", "10 4 + 2 /"]
    print("--- Tests Automatiques ---")
    for t in tests:
        print(f"Calcul : {t} \t-> {calculer_npi(t)}")
    
    print("\n--- Test Manuel ---")
    val = input("Entrez votre calcul : ")
    print(f"Résultat : {calculer_npi(val)}")

if __name__ == "__main__":
    main()
