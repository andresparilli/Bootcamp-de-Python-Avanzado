lista: list = [1, 2, 3, 4]
tupla: tuple = (1, 2, 3, 4)

DROPDOWN: dict = {
    1: "Colombia",
    2: "Mexico",
    3: "Venezuela"
}

print(tupla)
print(DROPDOWN[3])

# Mostrar que el str es inmutable
nombre: str = "Andres"
print(f"Primera variable: {id(nombre)}")

nombre: str = "Camila"
print(f"rescrito: {id(nombre)}")


# fin de orograma
