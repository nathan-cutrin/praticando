def scramble(s1, s2):
    """Função com objetivo de verificar se uma porção de letras contidas
    no S1 pode ser reorganizada para formar uma palavra em S2.

    Args:
        s1 (string): Uma string de caracteres
        s2 (string): Uma string de caracteres

    Returns:
        Boolean: A função retornará True ou False
    """

    dicionario_s1 = {}
    dicionario_s2 = {}

    for letra in s2:
        if letra not in s1:
            return False
        else:
            if letra not in dicionario_s2:
                dicionario_s1[letra] = s1.count(letra)
                dicionario_s2[letra] = s2.count(letra)
                if dicionario_s2[letra] > dicionario_s1[letra]:
                    return False
    return True

# Essa questão eu levei quase um mês pra resolver porque levava
# em consideração uma boa performance de código.

# Eu acabava utilizando muitas funções de iteração
# que deixavam o código pesado.

# Fui pesquisar e falar com pessoas sobre essa questão, o que
# me levou a descobrir a complexidade algorítmica.

# A solução utiliza a estrutura de dados do Dicionário por ser
# mais simples de ser acessado.