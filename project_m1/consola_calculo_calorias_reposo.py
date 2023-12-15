import calculadora_indices as calc


# Calculates the basal metabolic rate (bmr) at rest following the formula:
# BMR = (10 ∗ weight) + (6.25 ∗ height) - (5 ∗ age) + genre_value
# using the information provided by the user
# the prompt uses spanish for the user input
def exec_calculate_bmr_at_rest() -> None:
    print("Esta herramienta calcula la tasa metabólica basal de una persona",
          "Este es el mínimo de calorías necesarias para vivir, es decir el número de calorías que un ser",
          "humano quema al día estando en reposo.")
    weight = float(input("Ingrese el peso de la persona en kilogramos: "))
    height = float(input("Ingrese la estatura de la persona en centimetros: "))
    age = int(input("Ingrese la edad de la persona en años: "))
    genre_value = float(input("Ingrese el valor de género de la persona: 5 para masculino y -161 para femenino: "))
    print("Su tasa metabólica basal es: ",
          calc.calculate_bmr_at_rest(weight, height, age, genre_value), " cal")


exec_calculate_bmr_at_rest()
