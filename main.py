
print("Los suma de los numeros es: ", int(input("Enter a number: ")) + int(input("Enter another number: ")))

print("Los resta de los numeros es: ", int(input("Enter a number: ")) - int(input("Enter another number: ")))

print("Los multiplicacion de los numeros es: ", int(input("Enter a number: ")) * int(input("Enter another number: ")))

print("Los division de los numeros es: ", int(input("Enter a number: ")) / int(input("Enter another number: ")))

print("El residuo de los numeros es: ", int(input("Enter a number: ")) % int(input("Enter another number: ")))

a = int(input("Enter number 1: "))
op = input("Operator (+, -, *, /, %): ")
b = int(input("Enter number 2: "))

if op == "+": print(a + b)
elif op == "-": print(a - b)
elif op == "*": print(a * b)
elif op == "/": print(a / b)
elif op == "%": print(a % b)

print("Los suma de los numeros es: ", int(input("Enter a number: ")) + int(input("Enter another number: ")) + int(input("Enter another number: ")))

operacion = input("Escribe tu operación (ej. 2 + 4 - 3): ")
print("Resultado:", eval(operacion))






