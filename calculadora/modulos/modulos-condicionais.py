#relacionais 

idade = 20

maior_idade = idade >= 18


if maior_idade:
    print("É maior de idade")


verifica_email = True
verifica_senha = False

login = verifica_email and verifica_senha
print(login)

if login:
    print("Entrar no progama")

#notass

nota_final = 200

if nota_final < 4:
    print("Reprovado")

elif nota_final < 6:
    print("Recuperação")

else:
    print("Aprovado")

print("FIM")