#Ejercicio 2

import math 

def log2_safe(x):
    return math.log2(x) if x > 0 else float('-inf')


set_de_datos = [
    {"edad": 22, "departamento": "IT", "nivel_educativo": "terciario", "en_formacion": True},
    {"edad": 24, "departamento": "IT", "nivel_educativo": "universitario", "en_formacion": True},
    {"edad": 21, "departamento": "RRHH", "nivel_educativo": "terciario", "en_formacion": True},
    {"edad": 35, "departamento": "IT", "nivel_educativo": "universitario", "en_formacion": False},
    {"edad": 40, "departamento": "Finanzas", "nivel_educativo": "maestría", "en_formacion": False},
    {"edad": 29, "departamento": "RRHH", "nivel_educativo": "universitario", "en_formacion": False},
    {"edad": 23, "departamento": "IT", "nivel_educativo": "terciario", "en_formacion": True},
    {"edad": 38, "departamento": "Finanzas", "nivel_educativo": "universitario", "en_formacion": False}]


P = sum(1 for d in set_de_datos if d["en_formacion"])
N = sum(1 for d in set_de_datos if not d["en_formacion"])

#A)

filtro_nivel_educativo = [d for d in set_de_datos if d["nivel_educativo"] == "terciario"]
p = sum(1 for d in filtro_nivel_educativo if d["en_formacion"])
n = sum(1 for d in filtro_nivel_educativo if not d["en_formacion"])

foil_gain = p * (log2_safe(p / (p + n)) - log2_safe(P / (P + N)))

print("Condición: nivel_educativo == 'terciario'")
print(f"P (positivos antes) = {P}")
print(f"N (negativos antes) = {N}")
print(f"p (positivos después) = {p}")
print(f"n (negativos después) = {n}")
print(f"p / (p + n) = {p / (p + n):.3f}")
print(f"P / (P + N) = {P / (P + N):.3f}")
print(f"log2(p / (p + n)) = {log2_safe(p / (p + n)):.3f}")
print(f"log2(P / (P + N)) = {log2_safe(P / (P + N)):.3f}")
print(f"FOIL Gain = {foil_gain:.3f}")


#C)

filtro_edad_menor_igual_23 = [d for d in set_de_datos if d["edad"] <= 23]
p_edad = sum(1 for d in filtro_edad_menor_igual_23 if d["en_formacion"])
n_edad = sum(1 for d in filtro_edad_menor_igual_23 if not d["en_formacion"])

foil_gain_edad = p_edad * (log2_safe(p_edad / (p_edad + n_edad)) - log2_safe(P / (P + N)))

print("\nCondición: edad <= 23")
print(f"P (positivos antes) = {P}")
print(f"N (negativos antes) = {N}")
print(f"p (positivos después) = {p_edad}")
print(f"n (negativos después) = {n_edad}")
print(f"p / (p + n) = {p_edad / (p_edad + n_edad):.3f}")
print(f"P / (P + N) = {P / (P + N):.3f}")
print(f"log2(p / (p + n)) = {log2_safe(p_edad / (p_edad + n_edad)):.3f}")
print(f"log2(P / (P + N)) = {log2_safe(P / (P + N)):.3f}")
print(f"FOIL Gain = {foil_gain_edad:.3f}")