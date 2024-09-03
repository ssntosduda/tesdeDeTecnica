# 5) Escreva um programa que inverta os caracteres de um string.

# IMPORTANTE:
# a) Essa string pode ser informada através de qualquer entrada de sua preferência ou 
# pode ser previamente definida no código;
# b) Evite usar funções prontas, como, por exemplo, reverse;

print("Digite a string que deseja inverter:")
entrada = input()


string_invertida = ""

for i in range(len(entrada) - 1, -1, -1):
    string_invertida += entrada[i]

print("String invertida:", string_invertida)
