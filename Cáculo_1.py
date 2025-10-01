#Ejercicio 1 
def ejercicio_1 ():
 suma = 0 

 for n in range(5):
    num = int(input(f"Ingrese el número {n+1}: "))
    
    if num > 0 and num % 2 == 0:  # positivo y par
        print(f"El número {num} es positivo y par.")
        suma += num

 print("La suma total de los números positivos y pares es:", suma)

uno = ejercicio_1()
print(uno)

#ejercicio 2
def ejercicio_2():
 
 edad = int(input("hola, digite su edad: "))
 if edad < 13:
   print("Niño")
 elif 13 <= edad <= 17:
  print("Adolescente")
 elif 18 <= edad <= 59 :
  print("Adulto")
 elif edad >= 60:
  print("Adulto mayor")

dos = ejercicio_2()
print(dos)

#ejercicio 3

def ejercicio_3():
 palabra = input("ingrese una palabra: ")
 
 palabra1= palabra.lower()
 print("a:", palabra1.count("a")) 
 print("e:", palabra1.count("e")) 
 print("i:", palabra1.count("i"))
 print("o:", palabra1.count("o"))
 print("u:", palabra1.count("u"))
  
tres = ejercicio_3()
print(tres)
