# alumno: Angel Gabriel Saucedo
# Algoritmos y Programacion - B1

############ VARIABLES Y CONSTANTES ############

##3 Escribir un programa que almacene en distintas variables, dos valores enteros, dos reales, dos
## string y muestre el tipo de dato con la instrucción type() de todas las variables

# # defino las variables diferentes
var1,var2,var3,var4,var5,var6 = 12,13, 13.5, 14.5,"15","15.5"

# # # creo una funcion para mostrar el Type de todas las variables

for variable in (var1,var2,var3,var4,var5,var6): print(type(variable))

# # def mostrar_tipo_de_dato(tupla):
# #     for variable in tupla:
# #         print(type(variable))
# # # paso una tupla como argumento de la funcion.
# # mostrar_tipo_de_dato((var1,var2,var3,var4,var5,var6))

# variable1 = 12 # tipo de dato: int
# print(type(variable1))

# variable2 = 13 # tipo de dato: int
# print(type(variable2))

# variable3 = 13.5 # tipo de dato: float
# print(type(variable3))

# variable4 = 14.5 # tipo de dato: int
# print(type(variable4))

# variable5 = "15" # tipo de dato: str
# print(type(variable5))

# variable6 = "texto" # tipo de dato: int
# print(type(variable6))

# for var in (variable1,variable2,variable3,variable4,variable5,variable6):
#     print(type(var))