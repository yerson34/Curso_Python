python
apellidos = ["Pérez", "González", "Cortés", "Fernández", "Gómez"]
terminan_en_es = []
for apellido in apellidos:
    if apellido[-2:] == "es":
        terminan_en_es.append(apellido)

print("Los siguientes apellidos terminan en 'es':")
for apellido in terminan_en_es:
    print(apellido)
