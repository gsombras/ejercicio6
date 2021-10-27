#Input numbers

n1 = input("Introducir primer número: ")
n2 = input("Introducir segundo número: ")
n3 = input("Introducir tercer número: ")
list = [n1, n2, n3]
media = mean(list)
mediana = median(list)
varianza = pvariance(list)
print("Media: ", media)
print("Mediana: ", mediana)
print("Varianza: ", varianza)
print("Fin de la aplicación")