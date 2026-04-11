# imagina um sistema que recolha a escolha do usuario
#escolha_usuario
#se ..
# 0 ---> sair do rogama
# 1 ---> entrar no progama
#---> erro!

escolha_usuario = 0

match escolha_usuario:
    case 0:
        print("sair do progama")
    case 1: 
        print("Entrar no progama")
    case _:
        print("Erro")