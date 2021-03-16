from io import open
archivo_texto=open("Vocales1.txt" , "a")

texto = input("Ingrese una palabra:")
texto = texto.lower()
vocales = ["a", "e", "i", "o", "u"]

print("Ingreso la palabra: " + texto + "\nResultado: \n")
archivo_texto.write("Ingreso la palabra: " + texto + "\nResultado: \n")

for x in vocales:
    veces=0
    for y in texto :
        if x==y:
            veces+=1
    print("La vocal", x, "aparece:", veces, "veces")
    archivo_texto.write("La vocal " + x + " aparece: " + str(veces) + " veces \n")
archivo_texto.write("\n")
archivo_texto.close()
