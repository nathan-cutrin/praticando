def move_zeros(array):
    """Função que recebe um array que tem como objetivo mover todos os zeros
    para o final, preservando a ordem dos outros elementos.

    Args:
        array ([list]): Lista de números

    Returns:
        Retorna o array com as mudanças feitas.
    """

    for elemento in array:
        if elemento == 0:
            array.append(elemento)
            array.remove(elemento)
    return array
