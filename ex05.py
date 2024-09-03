print("Digite a string que deseja inverter:")
entrada = input()

# Inicializa a string invertida como uma string vazia
string_invertida = ""

# Percorre a string de trás para frente e constrói a string invertida
for i in range(len(entrada) - 1, -1, -1):
    string_invertida += entrada[i]

# Exibe a string invertida
print("String invertida:", string_invertida)