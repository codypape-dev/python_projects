def calcular_BMI(peso_lb: float, altura_inch: float) -> float:
    #peso_lb = peso_lb * 0.45
    #altura_inch = altura_inch * 0.025
    bmi = peso_lb / (altura_inch**2)
    return round(bmi, 2)

#print(calcular_BMI(180,66))

peso = float(input('peso'))
alt = float(input('alt'))
print(calcular_BMI(peso,alt))
