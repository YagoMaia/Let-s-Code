idade = int(input("Digite sua idade: "))
while idade >= 150 or 0 >= idade: 
    print("Idade Inválida, Por favor digite uma idade consistente!")
    idade = int(input("Digite sua idade: "))
salario = float(input("Digite o valor do seu salário: "))
while salario <= 0:
    print("Salário inválido, Por favor digite um salário válido")
    salario = float(input("Digite o valor do seu salário: "))
sexo = input("Digite seu sexo: [M, F, Outro]").strip().upper()[0]
while (sexo != "M") and (sexo != "F") and (sexo != "O"):
    print("Sexo inválido, por favor digite um sexo válido")
    sexo = input("Digite seu sexo: [M, F, Outro]").strip().upper()[0]
print(f"Você tem {idade} anos, com um salário de {salario} e é do sexo {sexo}")
