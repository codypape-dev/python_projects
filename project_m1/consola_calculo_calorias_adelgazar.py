import calculadora_indices as calc


# Estimate the number of calories a person needs to consume each day inorder to lose weight
def exec_calculate_calories_for_weight_lose() -> None:
    print("Esta herramienta calcula cuantas calorías debe consumir al dia una persona para adelgazar.",
          "Si las personas desean adelgazar deben reducir las calorías que ingieren a diario y/o deben aumentar",
          "el gasto calórico haciendo más deporte. Si se escoge la primera opción, se recomienda que las personas",
          "ingieran a diario entre un 15% a 20% menos calorías de las que arroja la TMB.")
    weight = float(input("Ingrese el peso de la persona en kilogramos: "))
    height = float(input("Ingrese la estatura de la persona en centimetros: "))
    age = int(input("Ingrese la edad de la persona en años: "))
    genre_value = float(input("Ingrese el valor de género de la persona: 5 para masculino y -161 para femenino: "))
    print(calc.calculate_calories_for_weight_lose(weight, height, age, genre_value))


exec_calculate_calories_for_weight_lose()
