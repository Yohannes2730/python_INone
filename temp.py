def temperature_advisor(temp):
    if temp < 10:
        return "It's very cold. Wear a heavy jacket."
    elif 10 <= temp <= 20:
        return "It's cool. Wear a light jacket."
    elif 21 <= temp <= 30:
        return "Nice weather. A T-shirt is fine."
    else:
        return "It's hot! Stay hydrated."

temperature = float(input("Enter the temperature: "))

advice = temperature_advisor(temperature)

print("Advice:", advice)

