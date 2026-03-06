def celsius_para_fahrenheit(celsius):
    if type(celsius) != int and type(celsius) != float:
        raise TypeError("Somente valores númericos")

    temp_fah = celsius * (9/5) + 32

    return round(temp_fah, 2)

def fahrenheit_para_celsius(fahrenheit):
    if type(fahrenheit) != int and type(fahrenheit) != float:
        raise TypeError("Somente valores númericos") 

    temp_cel = (fahrenheit - 32) * (5/9)

    return round(temp_cel, 2)
