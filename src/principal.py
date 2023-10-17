from view.splash_screen import SplashScreen
from view import menu
from reports.relatorios import Relatorio
from controller.controller_produto import Controller_Produto
from controller.controller_estoque import Controller_Estoque
from controller.controller_item_estoque import Controller_Item_Estoque


tela_inicial = SplashScreen()
relatorio = Relatorio()
controller_produto = Controller_Produto()
controller_estoque = Controller_Estoque()
controller_item_estoque = Controller_Item_Estoque()


def reports(opcao_relatorio):
    
    if opcao_relatorio == 1:
        relatorio.get_produto_todos_produtos()
    elif opcao_relatorio == 2:
        relatorio.get_produto_valor_total()
    elif opcao_relatorio == 3:
        relatorio.get_produto_produtos_reposicao()
    elif opcao_relatorio == 4:
        relatorio.get_estoque_todos_estoques()
    elif opcao_relatorio == 5:
        relatorio.get_estoque_produto_em_estoque_especifico()
    elif opcao_relatorio == 6:
        relatorio.get_item__todos_itens()
    elif opcao_relatorio == 7:
        relatorio.get_item_localizacao_produto_especifico()
    elif opcao_relatorio == 0:
        print("Voltando ao menu pricipal!")
    else:
        print("[ERRO] - Opção inválida!")


def inserir(opcao_inserir):
    if opcao_inserir == 1:
        print("------------- Inserir estoque -------------")
        controller_estoque.inserir_estoque()

    elif opcao_inserir == 2:
        print("------------- Inserir produto -------------")
        controller_produto.inserir_produto()        
        
    elif opcao_inserir == 3:
        print("------------- Inserir item -------------")
        controller_item_estoque.inserir_item_estoque()
        

    elif opcao_inserir == 0:
        print("Voltando ao menu pricipal!")

    else:
        print("[OPS] - Opçao inválida!")


def alterar(opcao_alterar):
    if opcao_alterar == 1:
        print("------------- Alterar estoque -------------")
        controller_estoque.alterar_estoque()

    elif opcao_alterar == 2:
        print("------------- Alterar produto -------------")
        controller_produto.alterar_produto()       
        
    elif opcao_alterar == 3:
        print("------------- Alterar item -------------")
        controller_item_estoque.alterar_item_estoque()

    elif opcao_alterar == 0:
        print("Voltando ao menu pricipal!")

    else:
        print("[OPS] - Opçao inválida!")


def excluir(opcao_excluir):
    if opcao_excluir == 1:
        print("------------- Excluir estoque -------------")
        controller_estoque.excluir_estoque()

    elif opcao_excluir == 2:
        print("------------- Excluir produto -------------")
        controller_produto.excluir_produto()              
        
    elif opcao_excluir == 3:
        print("------------- Excluir item -------------")
        controller_item_estoque.excluir_item_estoque()

    elif opcao_excluir == 0:
        print("Voltando ao menu pricipal!")

    else:
        print("[OPS] - Opçao inválida!")

# Main
def run():
    while True:
        try:
            print(tela_inicial.get_updated_screen())
            menu.clear_console()

            print(menu.menu_principal())
            opcao = int(input("Informe a sua opção: "))
            menu.clear_console(1)
        
            if opcao == 1: # Relatórios
                print(menu.relatorios())
                opcao_relatorio = int(input("Informe o relatório desejado: "))
                
                reports(opcao_relatorio)
            
            elif opcao == 2: # Inserir Novos Registros
                print(menu.menu_entidades())
                opcao_inserir = int(input("Informe a entidade para inserir: "))

                inserir(opcao_inserir)               

            elif opcao == 3: # Alterar Registros
                print(menu.menu_entidades())
                opcao_alterar = int(input("Informe a entidade para alterar: "))

                alterar(opcao_alterar)

            elif opcao == 4: # Excluir
                print(menu.menu_entidades())
                opcao_excluir = int(input("Informe a entidade para excluir: "))

                excluir (opcao_excluir)

            elif opcao == 0:
                print("Saindo...")
                print("Agradecemos por utilizar o nosso sistema!")
                menu.clear_console()
                exit(0)

            else:
                print("[Erro] - Opção inválida! Tente novamente")
        except Exception as error:
            print(f"[ERRO] - {error}")

run()