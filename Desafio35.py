print('-='*20)
print('Analisador de Triângulos')
print('-='*20)
a = float(input("Digite a reta a: "))
b = float(input("Digite a reta b: "))
c = float(input("Digite a reta c: "))
print("Reta a = {}".format(a))
print("Reta b = {}".format(b))
print("Reta c = {}".format(c))
if c<(a+b) and a<(b+c) and b<(a+c):
    print("Essas retas \033[7;32mPODEM\033[m formar um triângulo !!")
else:
    print("Essas retas \033[7;31mNÃO PODEM\033[m formar um triângulo !!")
print("end")


