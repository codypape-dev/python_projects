import calculadora_indices as calc


# Calculates the basal metabolic rate (bmr) by activity level following the formula:
# BMR_by_activity = BMR_at_rest * activity_level
# using the information provided by the user
# the prompt uses spanish for the user input
def exec_calculate_bmr_by_activity_level() -> None:
    print("Esta herramienta calcula la tasa metabólica basal de una persona segun su actividad fisica.",
          "Dado que las personas realizamos actividad física en el día, el consumo de calorías diarias",
          "es mayor al TMB. Para poder calcularlo es necesario multiplicar el TMB por un valor que",
          "depende de la actividad física semanal que realiza cada persona.")
    weight = float(input("Ingrese el peso de la persona en kilogramos: "))
    height = float(input("Ingrese la estatura de la persona en centimetros: "))
    age = int(input("Ingrese la edad de la persona en años: "))
    genre_value = float(input("Ingrese el valor de género de la persona: 5 para masculino y -161 para femenino: "))
    print("Segun la siguiente tabla de niveles de actividad fisica: ")
    print("Nivel: Poco o ningún ejercicio                       - Valor de actividad 1.2")
    print("Nivel: Ejercicio ligero (1 a 3 días a la semana)     - Valor de actividad 1.375")
    print("Nivel: Ejercicio moderado (3 a 5 días a la semana)   - Valor de actividad 1.55")
    print("Nivel: Deportista (6 -7 días a la semana)            - Valor de actividad 1.72")
    print("Nivel: Atleta (entrenamientos mañana y tarde)        - Valor de actividad 1.9")
    activity_level = float(input("Ingrese el valor de actividad que se ajusta a su rutina de ejercicio semanal: "))
    print("Su tasa metabólica basal es: ",
          calc.calcular_calorias_en_actividad(weight, height, age, genre_value, activity_level), " cal")


exec_calculate_bmr_by_activity_level()
