# alumno: Angel Gabriel Saucedo
# Algoritmos y Programacion - B1

############ ESTRUCTURAS ITERATIVAS FOR ############

##20 Escribir un programa que solicita el ingreso de una palabra, debe pasarla al jeringoso y 
## mostrarla al finalizar la conversión. 
## 1. Convertir la palabra a minúsculas o mayúsculas. 
## 2. Utilizar un acumulador (de letras) mientras, pasa la palabra al jeringoso 
## 3. Mostrarla convertida (use else). 
## Definición de jeringoso: Forma festiva de hablar, que añade tras cada vocal una sílaba formada 
## por una letra (p) y la misma vocal precedente. por ejemplo: 
## yo no se nada 
## yopo nopo sepe napadapa

frase_original = input("ingrese una frase para convertir en jeringoso: ").lower()
vocales = ("a","e","i","o","u")
frase_jeringoso = ""

for letra in frase_original:
    if letra in vocales:
        frase_jeringoso += letra+"p"+letra
    else:
        frase_jeringoso += letra

print(frase_jeringoso)