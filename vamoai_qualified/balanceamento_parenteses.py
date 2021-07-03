def balanceado(texto):

    """Função que recebe um texto com o objetivo de verificar
    se há balanceamento de parênteses.

    Returns:
        Boolean: A função retornará True ou False.
    """

    esq_paren = texto.find('(')
    dir_paren = texto.find(')')
    ult_paren_esq = texto.rfind('(')
    ult_paren_dir = texto.rfind(')')

    if dir_paren < esq_paren or ult_paren_dir < ult_paren_esq:
        return False
    elif texto.count('(') == texto.count(')'):
        return True
    else:
        return False






