def menu_principal():
    return(
    """
    =-=-=-=-=-=-=-=-=-=-=-=-= MENU PRINCIPAL =-=-=-=-=-=-=-=-=-=-=-=-=
        [1] - Relatórios
        [2] - Inserir Registros
        [3] - Alterar Registros
        [4] - Remover Registros
        [0] - Sair
    """
    )

def menu_entidades():
    return(
    """
    =-=-=-=-=-=-=-=-=-=-=-=-= ENTIDADES =-=-=-=-=-=-=-=-=-=-=-=-=
    [1] - ESTOQUE
    [2] - PRODUTO
    [3] - ITEM ESTOQUE
    [0] - SAIR
    """
    )

def relatorios():
    return(
    """
    =-=-=-=-=-=-=-=-=-=-=-=-=-=-= RELATÓRIOS =-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    
    ------------------------------ produtos ------------------------------
        [1] - Todos os produtos
        [2] - Valor total dos produtos
        [3] - Produtos que precisam de reposição

        
    ------------------------------ estoque -------------------------------
        [4] - Todos os estoques
        [5] - Produtos em um estoque específico 

        
    ---------------------------- item_estoque ----------------------------
        [6] - Todos os itens
        [7] - Localização de um produto específico
            
        
        [0] - Sair
    =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    """
    )

# Consulta de contagem de registros por tabela
QUERY_COUNT = 'select count(1) as total_{tabela} from {tabela}'

def clear_console(wait_time:int=3):
    '''
       Esse método limpa a tela após alguns segundos
       wait_time: argumento de entrada que indica o tempo de espera
    '''
    import os
    import platform
    from time import sleep
    sleep(wait_time)

    # retorno de plataform.system() de acordo com o link: https://github.com/python/cpython/blob/356997cccc21a3391175d20e9ef03d434675b496/Lib/platform.py#L906-L913
    sistem_operational = platform.system()

    if sistem_operational == "Windows":
        os.system("cls")
    else:
        os.system("clear")
