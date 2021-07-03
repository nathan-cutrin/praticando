def balanceado(texto):

    """Função que recebe um texto com o objetivo de verificar
    se há balanceamento de parênteses.

    Returns:
        Boolean: A função retornará True ou False.
    """

    if texto.count('(') == texto.count(')'):
        if texto[0] == '(' and texto[-1] == ')':
            return True
    return False

# Solução 2.0 pra tentar melhorar a primeira solução.

# Testei várias vezes, espero que esteja funcionando.
