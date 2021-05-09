n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
a = n1 + n2
s = n1 - n2
m = n1 * n2
d = n1 / n2
p = n1 ** n2
di = n1 // n2
rd = n1 % n2
print(" Os resultados são: \n adição {}, \n subtracão {}, multiplicação {}, divisão {:.3f} ".format(a, s, m, d), end=" >>> ")
print("Os resultados restantes são: potenciação {}, divisão inteira {} e resto da divisão {} ".format(p, di, rd))






