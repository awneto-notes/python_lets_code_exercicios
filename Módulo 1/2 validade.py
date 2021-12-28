


idade, salario, sexo = input("Digite a idade (entre 0 e 150), o salário (maior que zero) e o sexo (M ou F) da pessoa.").split()

idade = int(idade)
salario = int(salario)

if idade < 0 or idade > 150:
    print("Idade inválida.")

if salario < 0:
    print("Salário inválido")

if sexo != "M" and sexo != "F":
    print("Sexo inválido")