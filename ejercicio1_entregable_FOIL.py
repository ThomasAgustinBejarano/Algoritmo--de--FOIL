#Ejercicio 1

set_de_datos = [
    {"edad": 22, "departamento": "IT", "nivel_educativo": "terciario", "en_formacion": True},
    {"edad": 24, "departamento": "IT", "nivel_educativo": "universitario", "en_formacion": True},
    {"edad": 21, "departamento": "RRHH", "nivel_educativo": "terciario", "en_formacion": True},
    {"edad": 35, "departamento": "IT", "nivel_educativo": "universitario", "en_formacion": False},
    {"edad": 40, "departamento": "Finanzas", "nivel_educativo": "maestría", "en_formacion": False},
    {"edad": 29, "departamento": "RRHH", "nivel_educativo": "universitario", "en_formacion": False},
    {"edad": 23, "departamento": "IT", "nivel_educativo": "terciario", "en_formacion": True},
    {"edad": 38, "departamento": "Finanzas", "nivel_educativo": "universitario", "en_formacion": False}]


P = [d for d in set_de_datos if d["en_formacion"]]
N = [d for d in set_de_datos if not d["en_formacion"]]

filtro_edad = [d["edad"] for d in P if d["edad"] not in [nd["edad"] for nd in N] and d["edad"] not in filtro_edad]
#print (filtro_edad)

filtro_departamento = [d["departamento"] for d in P if d["departamento"] not in [nd["departamento"] for nd in N] and d["departamento"] not in filtro_departamento]
#print (filtro_departamento)

filtro_nivel_educativo = [d["nivel_educativo"] for d in P if d["nivel_educativo"] not in [nd["nivel_educativo"] for nd in N] and d["nivel_educativo"] not in filtro_nivel_educativo]
#print (filtro_nivel_educativo)



if len(filtro_departamento) > 0:
    print("- los valores de departamento que aparecen solo en los positivos: ", filtro_departamento)
else:
    print("- no hay departamentos únicos en los positivos")

print("--------------")

if len(filtro_nivel_educativo) > 0:
    print("- los niveles educativos que son comunes en los positivos pero no en los negativos: ", filtro_nivel_educativo)
else:
    print("- no hay niveles educativos únicos en los positivos")

print("--------------")

if len(filtro_edad) > 0:
    print("- las edades que aparecen solo en los positivos: ", filtro_edad)
else:
    print("- no hay edades únicas en los positivos")


