import math


# Calculates the body mass index following the formula:
# BMI = weight (kg)/(height(m))^2
def calculate_bmi(weight: float, height: float) -> float:
    return round(weight / math.pow(height, 2), 2)


# Calculates the body fat percentage following the formula:
# BFP = 1.2 ∗ BMI + 0.23 ∗ age - 5.4 − genre_value
def calculate_body_fat_percentage(weight: float, height: float, age: int, genre_value: float) -> float:
    bmi = calculate_bmi(weight, height)
    return round(1.2 * bmi + 0.23 * age - 5.4 - genre_value, 2)


# Calculates the basal metabolic rate (bmr) at rest following the formula:
# BMR = (10 ∗ weight) + (6.25 ∗ height) - (5 ∗ age) + genre_value
def calculate_bmr_at_rest(weight: float, height: float, age: int, genre_value: float) -> float:
    return round((10 * weight) + (6.25 * height) - (5 * age) + genre_value, 2)


# Calculates the basal metabolic rate (bmr) by activity level following the formula:
# BMR_by_activity = BMR_at_rest * activity_level
def calculate_bmr_by_activity_level(weight: float, height: float, age: int, genre_value: float,
                                    activity_level: float) -> float:
    bmr_at_rest = calculate_bmr_at_rest(weight, height, age, genre_value)
    return round(bmr_at_rest * activity_level, 2)


# Estimate the number of calories a person needs to consume each day inorder to lose weight
def calculate_calories_for_weight_lose(weight: float, height: float, age: int, genre_value: float) -> str:
    bmr_at_rest = calculate_bmr_at_rest(weight, height, age, genre_value)
    return "Para adelgazar es recomendado que consumas entre: " + str(round(bmr_at_rest * 0.80, 2)) + \
        " y " + str(round(bmr_at_rest * 0.85, 2)) + ' calorías al día.'
