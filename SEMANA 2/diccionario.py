# FIGURAS GEOMÉTRICAS

figuras = {
    3:"Triángulo",
    4:"Cuadrado o Rectángulo",
    5:"Pentágono",
    6:"Hexágono",
    7:"Heptágono",
    8:"Octágono"
}

lados = int(input("Ingrese los lados de la figura: "))

figura = figuras.get(lados, "Figura no reconocida.")

print(f"La figura con {lados} lados es: {figura}")



