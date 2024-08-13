def suma(*args):
  """
  Suma una cantidad indefinida de números enteros.

  Args:
    *args: Argumentos variables que representan los números a sumar.

  Returns:
    La suma de todos los números enteros proporcionados.

  Raises:
    TypeError: Si alguno de los argumentos no es un número entero.
    
>>> suma(2, 3)
5
>>> suma(10, -3, 5)
12
>>> suma()  # Sin argumentos
0
>>> suma(2, 3.5)  # Argumento no entero
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 11, in suma
TypeError: Todos los argumentos deben ser números enteros.
  """
  # Verificar que todos los argumentos sean enteros
  for arg in args:
    if not isinstance(arg, int):
      raise TypeError("Todos los argumentos deben ser números enteros.")

  # Sumar todos los argumentos
  total = 0
  for num in args:
    total += num
  return total

# Ejemplos de uso
print(suma(2, 3))        # Salida: 5
print(suma(1, 5, 7, 2))  # Salida: 15
print(suma(2,3,4,10))
