perguntas = [
    "Mora perto da vítima?",
    "Já trabalhou com a vítima?",
    "Telefonou para a vítima?",
    "Esteve no local do crime?",
    "Devia para a vítima?"
]

pontos = 0
for pergunta in perguntas:
    resposta = input(pergunta)
    if(resposta == "sim" or resposta == "Sim" or resposta == "S" or resposta == "s"):
        pontos +=1

if pontos == 5:
    print("Assasino")
elif pontos > 3:
    print("Cúmplice")
elif pontos == 2:
    print("Suspeito")
else:
    print("Liberado")