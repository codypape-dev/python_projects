import math


# Calculates the body mass index following the formula:
# BMI = peso (kg)/(altura(m))^2
def calcular_IMC(peso: float, altura: float) -> float:
    return round(peso / math.pow(altura, 2), 2)


# Calculates the body fat percentage following the formula:
# BFP = 1.2 ∗ BMI + 0.23 ∗ edad - 5.4 − valor_genero
def calcular_porcentaje_grasa(peso: float, altura: float, edad: int, valor_genero: float) -> float:
    bmi = calcular_IMC(peso, altura)
    return round(1.2 * bmi + 0.23 * edad - 5.4 - valor_genero, 2)


# Calculates the basal metabolic rate (bmr) at rest following the formula:
# BMR = (10 ∗ peso) + (6.25 ∗ altura) - (5 ∗ edad) + valor_genero
def calcular_calorias_en_reposo(peso: float, altura: float, edad: int, valor_genero: float) -> float:
    return round((10 * peso) + (6.25 * altura) - (5 * edad) + valor_genero, 2)


# Calculates the basal metabolic rate (bmr) by activity level following the formula:
# BMR_by_activity = BMR_at_rest * activity_level
def calculate_bmr_by_activity_level(peso: float, altura: float, edad: int, valor_genero: float,
                                    activity_level: float) -> float:
    bmr_at_rest = calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
    return round(bmr_at_rest * activity_level, 2)


# Estimate the number of calories a person needs to consume each day inorder to lose peso
def calcular_calorias_en_actividad(peso: float, altura: float, edad: int, valor_genero: float) -> str:
    bmr_at_rest = calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
    return "Para adelgazar es recomendado que consumas entre: " + str(round(bmr_at_rest * 0.80, 2)) + \
        " y " + str(round(bmr_at_rest * 0.85, 2)) + ' calorías al día.'
