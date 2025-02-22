#Leer un archivo línea por línea
"""with open('Caperucita.txt', 'r') as file:
    for lineas in file:
        print(lineas.strip())"""

#Leer todas la líneas en una lista. los saltos de línea se separan por "," dentro de la variable
"""with open('Caperucita.txt', 'r') as file:
    lines = file.readlines()
    print(lines)"""

# a hace referencia a append, no elimina el archivo, con w se reescribe todo el archivo
"""with open('Caperucita.txt', 'a') as file:
    file.write("\n\n By:ChatGPT")"""

#sobreescribe el archivo
"""with open('Caperucita.txt', 'w') as file:
    file.write("\n\n By:DeepSeek")"""

with open('Caperucita.txt', 'r') as file:
    lines = file.readlines()
    print(len(lines))
