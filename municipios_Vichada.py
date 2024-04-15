def mostrar_menu():
    municipios = [
        "Cumaribo", 
        "La Primavera", 
        "Puerto Carreño", 
        "Santa Rosalía"
    ]

    print("Municipios de Vichada:")
    for i, municipio in enumerate(municipios, 1):
        print(f"{i}. {municipio}")

    eleccion = int(input("Por favor, selecciona un municipio por su número: "))
    if 1 <= eleccion <= len(municipios):
        print(f"Has seleccionado el municipio: {municipios[eleccion - 1]}")
    else:
        print("Número inválido. Por favor, intenta de nuevo.")

mostrar_menu()
