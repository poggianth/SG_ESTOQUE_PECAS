import os
import time
from view import menu
from model.produto import Produto
from model.estoque import Estoque
from model.item_estoque import ItemEstoque
from controller.controller_produto import controller_produto


# Main
def run():

    while True:
        try:
                
            time.sleep(2)
            # os.system('cls')
            menu.mostra_opcoes()
            
            opcao = int(input("Informe a sua opção: "))
        
            if opcao == 1:
                print("Listar todos os produtos!")
                produtos = controller_produto.lista_produtos()
                for prod in produtos:
                    print(f"{prod}")
            
            elif opcao == 2:
                print("Listar um único produto!")
                id_buscar = int(input("Informe o id do produto que deseja buscar: "))
                print(controller_produto.lista_unico_produto(id_buscar))

            elif opcao == 3:
                print("Escolheu a opção 3")
            elif opcao == 4:
                print("Escolheu a opção 4")
            elif opcao == 5:
                print("Escolheu a opção 5")
            elif opcao == 6:
                print("Escolheu a opção 6")
            elif opcao == 0:
                print("Saindo...")
                print("Agradecemos por utilizar o nosso sistema!")
            else:
                print("[Erro] - Opção inválida! Tente novamente")
        except Exception as error:
            print(f"[ERRO] - {error}")

run()