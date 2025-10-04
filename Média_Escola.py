 #escolha= int(input(f'1- Para calcular a média geral do 1º Bimestre\n2- Para calcular a média geral do 2º Bimestre\n3- Para calcular a média geral do 3º Bimestre\n4- Para calcular a média geral do 4º Bimestre\n5- Para calcular a média geral de uma matéria específica\n6- Para calcular a média geral do aluno 1º, 2º, 3º e 4º bimestre\n7- Para encerrar\n\nEscolha uma oção:'))
# print()


while True:
    print(f'1- Para calcular a média geral do 1º Bimestre')
    print(f'2- Para calcular a média geral do 2º Bimestre')
    print(f'3- Para calcular a média geral do 3º Bimestre')
    print(f'4- Para calcular a média geral do 4º Bimestre')
    print(f'5- Para calcular a média geral de uma matéria específica')
    print(f'6- Para calcular a média geral do aluno 1º, 2º, 3º e 4º bimestre')
    print(f'7- Para encerrar\n')
    print()

    try:
        escolha = int(input('Escolha uma opção (1 a 7): '))
        print()

        if escolha < 1 or escolha > 7:
            print('Opção inválida! Digite um número inteiros de 1 a 7.\n')
            print()
            

        else:
            print()

        if escolha == 1:
            print(f'1º Bimestre :\n')

            nome = input("digite o nome do aluno: ")
            serie_turma = input("digite a Série e a turma do aluno: ")

            nota2 = float(input('Digite a média geral de Matemática: '))
            nota3 = float(input('Digite a média geral de Ciências: '))
            nota4 = float(input('Digite a média geral de Biologia: '))
            nota1 = float(input('Digite a média geral de Português: '))
            nota5 = float(input('Digite a média geral de Química: '))
            nota6 = float(input('Digite a média geral de Geografia: '))
            nota7 = float(input('Digite a média geral de História: '))
            nota8 = float(input('Digite a média geral de Projeto de Vida: '))
            nota9 = float(input('Digite a média geral de Sociologia: '))
            nota10 = float(input('Digite a média geral de Filosofia: '))
            nota11 = float(input('Digite a média geral de Física: '))
            nota12 = float(input('Digite a média geral de Inglês: '))
            nota13 = float(input('Digite a média geral de Artes: '))

            media1 = (nota1 + nota2 + nota3 + nota4 + nota5 + nota6 +
                      nota7 + nota8 + nota9 + nota10 + nota11 + nota12 + nota13) / 13

            print(f'A média geral do {nome} do {serie_turma} no 1º bimestre é: {media1}.\n')

        elif escolha == 2:
            print(f'2º Bimestre :\n')

            nome = input("digite o nome do aluno: ")
            serie_turma = input("digite a Série e a turma do aluno: ")

            nota1 = float(input('Digite a média geral de Português: '))
            nota2 = float(input('Digite a média geral de Matemática: '))
            nota3 = float(input('Digite a média geral de Ciências: '))
            nota4 = float(input('Digite a média geral de Biologia: '))
            nota5 = float(input('Digite a média geral de Química: '))
            nota6 = float(input('Digite a média geral de Geografia: '))
            nota7 = float(input('Digite a média geral de História: '))
            nota8 = float(input('Digite a média geral de Projeto de Vida: '))
            nota9 = float(input('Digite a média geral de Sociologia: '))
            nota10 = float(input('Digite a média geral de Filosofia: '))
            nota11 = float(input('Digite a média geral de Física: '))
            nota12 = float(input('Digite a média geral de Inglês: '))
            nota13 = float(input('Digite a média geral de Artes: '))

            media2 = (nota1 + nota2 + nota3 + nota4 + nota5 + nota6 +
                      nota7 + nota8 + nota9 + nota10 + nota11 + nota12 + nota13) / 13

            print(f'A média geral do {nome} do {serie_turma} no 2º bimestre é: {media2}.\n')

        elif escolha == 3:
            print(f'3º Bimestre :\n')

            nome = input("digite o nome do aluno: ")
            serie_turma = input("digite a Série e a turma do aluno: ")

            nota1 = float(input('Digite a média geral de Português: '))
            nota2 = float(input('Digite a média geral de Matemática: '))
            nota3 = float(input('Digite a média geral de Ciências: '))
            nota4 = float(input('Digite a média geral de Biologia: '))
            nota5 = float(input('Digite a média geral de Química: '))
            nota6 = float(input('Digite a média geral de Geografia: '))
            nota7 = float(input('Digite a média geral de História: '))
            nota8 = float(input('Digite a média geral de Projeto de Vida: '))
            nota9 = float(input('Digite a média geral de Sociologia: '))
            nota10 = float(input('Digite a média geral de Filosofia: '))
            nota11 = float(input('Digite a média geral de Física: '))
            nota12 = float(input('Digite a média geral de Inglês: '))
            nota13 = float(input('Digite a média geral de Artes: '))

            media3 = (nota1 + nota2 + nota3 + nota4 + nota5 + nota6 +
                      nota7 + nota8 + nota9 + nota10 + nota11 + nota12 + nota13) / 13

            print(f'A média geral do {nome} do {serie_turma} no 3º bimestre é: {media3}.\n')

        elif escolha == 4:
            print(f'4º Bimestre :\n')

            nome = input("digite o nome do aluno: ")
            serie_turma = input("digite a Série e a turma do aluno: ")

            nota1 = float(input('Digite a média geral de Português: '))
            nota2 = float(input('Digite a média geral de Matemática: '))
            nota3 = float(input('Digite a média geral de Ciências: '))
            nota4 = float(input('Digite a média geral de Biologia: '))
            nota5 = float(input('Digite a média geral de Química: '))
            nota6 = float(input('Digite a média geral de Geografia: '))
            nota7 = float(input('Digite a média geral de História: '))
            nota8 = float(input('Digite a média geral de Projeto de Vida: '))
            nota9 = float(input('Digite a média geral de Sociologia: '))
            nota10 = float(input('Digite a média geral de Filosofia: '))
            nota11 = float(input('Digite a média geral de Física: '))
            nota12 = float(input('Digite a média geral de Inglês: '))
            nota13 = float(input('Digite a média geral de Artes: '))

            media4 = (nota1 + nota2 + nota3 + nota4 + nota5 + nota6 +
                      nota7 + nota8 + nota9 + nota10 + nota11 + nota12 + nota13) / 13

            print(f'A média geral do {nome} do {serie_turma} no 4º bimestre é: {media4}.\n')

        elif escolha == 5:
            print('Matéria específica:\n')
            nome = input("digite o nome do aluno: ")
            serie_turma = input("digite a Série e a turma do aluno: ")
            materia = input('Escolha a matéria que deseja calcular a média: ')
            print()

            nota1 = float(input('Digite a nota do 1º bimestre: '))
            nota2 = float(input('Digite a nota do 2º bimestre: '))
            nota3 = float(input('Digite a nota do 3º bimestre: '))
            nota4 = float(input('Digite a nota do 4º bimestre: '))

            media5 = (nota1 + nota2 + nota3 + nota4) / 4

            if media5 >= 5:
                print(f'O {nome} do {serie_turma} está com média normal: {media5} (Aprovado nessa matéria).\n')
            else:
                print(f'O {nome} do {serie_turma} está com média baixa: {media5} (Reprovado nessa matéria).\n')

        elif escolha == 6:
            print('Aprovado ou Reprovado\n')
            nome = input("digite o nome do aluno: ")
            serie_turma = input("digite a Série e a turma do aluno: ")

            nota1 = float(input('Digite a média geral do 1º bimestre: '))
            nota2 = float(input('Digite a média geral do 2º bimestre: '))
            nota3 = float(input('Digite a média geral do 3º bimestre: '))
            nota4 = float(input('Digite a média geral do 4º bimestre: '))

            mediaGeral = (nota1 + nota2 + nota3 + nota4) / 4

            if mediaGeral >= 5:
                print(f'O {nome} do {serie_turma} está com média normal: {mediaGeral} (Aprovado).\n')
            else:
                print(f'O {nome} do {serie_turma} está com média baixa: {mediaGeral} (Reprovado).\n')

        elif escolha == 7:
            print('Sistema encerrado!')
            break

    except ValueError:
        print('Entrada inválida! Digite apenas números de 1 a 7.\n')
