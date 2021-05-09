nome = str(input("Digite seu nome completo: ")).strip()
print('Analisando seu nome...')
print("O seu nome em letras maiúsculas é: {} ".format(nome.upper()))
print("O seu nome em letras minúsculas é: {} ".format(nome.lower()))
print('O nome digitado tem {} espaços entre eles'.format(nome.count(' ')))
print("O seu nome tem um total de {} letras".format(len(nome) - nome.count(' ')))
print("O seu primeiro nome tem {} letras".format(nome.find(' ')))
separa = nome.split()
print('O seu primeiro é {} e ele tem {} letras'.format(separa[0], len(separa[0])))
print('Quantidade de letra 1° nome é {}'.format(len(separa[0])))
print('Qual o primeiro nome ?? {} '.format(separa[0]))






