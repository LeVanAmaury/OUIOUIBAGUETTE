def calculer_npi(expression):
    pile = []
    tokens = expression.split() # Découpe la phrase en mots
    
    for token in tokens:
        # Si c'est un nombre (positif ou négatif)
        if token.isdigit() or (token.startswith('-') and len(token) > 1):
            pile.append(int(token))
            
        # Si c'est un opérateur
        elif token in ['+', '-', '*', '/']:
            if len(pile) < 2:
                return "Erreur : Pas assez de nombres dans la pile"
            
            # Attention : le dernier sorti est le 2ème nombre du calcul
            b = pile.pop()
            a = pile.pop()
            
            if token == '+': pile.append(a + b)
            elif token == '-': pile.append(a - b)
            elif token == '*': pile.append(a * b)
            elif token == '/': 
                if b == 0: return "Erreur : Division par zéro"
                pile.append(int(a / b))
        else:
            return "Erreur : Caractère inconnu"
            
    # À la fin, il ne doit rester qu'un seul nombre
    if len(pile) == 1:
        return pile[0]
    else:
        return "Erreur : Le calcul n'est pas fini (trop de nombres ?)"
