import indexes_calc as calc


# Calculates the body fat percentage following the formula:
# BFP = 1.2 ∗ BMI + 0.23 ∗ age - 5.4 − genre_value
# using the information provided by the user
# the prompt uses spanish for the user input
def exec_calculate_bfp() -> None:
    print("Esta herramienta calcula el porcentaje de grasa corporal de una persona",
          "que permite establecer si una persona tiene un nivel",
          "adecuado o excesivo de grasa en su cuerpo. ",
          "Este se calcula a partir del IMC, la edad y el género de la persona.")
    weight = float(input("Ingrese el peso de la persona en kilogramos: "))
    height = float(input("Ingrese la estatura de la persona en metros: "))
    age = int(input("Ingrese la edad de la persona en años: "))
    genre = str.upper(input("Ingrese el valor de genero: 10.8 para masculino y 0 para femenino: "))
    print("Su porcentaje de grasa corporal es: " +
          str(calc.calculate_body_fat_percentage(weight, height, age, genre_value)) + "%")


exec_calculate_bfp()
