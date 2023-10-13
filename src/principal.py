import os
import time
from view.splash_screen import SplashScreen
from view import menu
from reports.relatorios import Relatorio
from controller.controller_produto import controller_produto


tela_inicial = SplashScreen()
relatorio = Relatorio()


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
    else:
        print("[ERRO] - Opção inválida!")

# Main
def run():
    print(tela_inicial.get_updated_screen())
    menu.clear_console()

    while True:
        try:
            print(menu.menu_principal())
            opcao = int(input("Informe a sua opção: "))
            menu.clear_console(1)
        
            if opcao == 1: # Relatórios
                print(menu.relatorios())
                opcao_relatorio = int(input("Informe o relatório desejado: "))
                
                reports(opcao_relatorio)
            
            elif opcao == 2: # Inserir Novos Registros
                print(menu.menu_entidades())

            elif opcao == 3: # Atualizar Registros
                print(menu.menu_entidades())

            elif opcao == 4: # Excluir
                print("Escolheu a opção 4")

            elif opcao == 0:
                print("Saindo...")
                print("Agradecemos por utilizar o nosso sistema!")
                exit(0)

            else:
                print("[Erro] - Opção inválida! Tente novamente")
        except Exception as error:
            print(f"[ERRO] - {error}")

run()