def mostrar_menu():
    municipios = [
        "Ibagué", 
        "Alpujarra", 
        "Alvarado", 
        "Ambalema", 
        "Anzoátegui", 
        "Armero Guayabal", 
        "Ataco", 
        "Cajamarca", 
        "Carmen de Apicalá", 
        "Casabianca", 
        "Chaparral", 
        "Coello", 
        "Coyaima", 
        "Cunday", 
        "Dolores", 
        "Espinal", 
        "Falan", 
        "Flandes", 
        "Fresno", 
        "Guamo", 
        "Herveo", 
        "Honda", 
        "Icononzo", 
        "Lérida", 
        "Líbano", 
        "Mariquita", 
        "Melgar", 
        "Murillo", 
        "Natagaima", 
        "Ortega", 
        "Palocabildo", 
        "Piedras", 
        "Planadas", 
        "Prado", 
        "Purificación", 
        "Rioblanco", 
        "Roncesvalles", 
        "Rovira", 
        "Saldaña", 
        "San Antonio", 
        "San Luis", 
        "Santa Isabel", 
        "Venadillo", 
        "Villahermosa",
        # Añade aquí el resto de los municipios
    ]

    print("Municipios de Tolima:")
    for i, municipio in enumerate(municipios, 1):
        print(f"{i}. {municipio}")

    eleccion = int(input("Por favor, selecciona un municipio por su número: "))
    if 1 <= eleccion <= len(municipios):
        print(f"Has seleccionado el municipio: {municipios[eleccion - 1]}")
    else:
        print("Número inválido. Por favor, intenta de nuevo.")

mostrar_menu()
