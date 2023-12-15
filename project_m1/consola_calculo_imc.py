import calculadora_indices as calc


# Calculates the body mass index following the formula:
# BMI = weight (kg)/(height(m))^2
# using the information provided by the user
# the prompt uses spanish for the user input
def calcular_IMC() -> None:
    print("Esta herramienta calcula el índice de masa corporal de una persona.",
          "Este metodo se utiliza para estimar si el peso de una persona es ",
          "adecuado con respecto a su altura. El IMC se calcula como la razón",
          "entre el peso en kilogramos y el cuadrado de la altura en metros de la persona.")
    weight = float(input("Ingrese el peso de la persona en kilogramos: "))
    height = float(input("Ingrese la estatura de la persona en metros: "))
    print("Su índice de masa corporal es: ", calc.calculate_bmi(weight, height))


exec_calculate_bmi()
