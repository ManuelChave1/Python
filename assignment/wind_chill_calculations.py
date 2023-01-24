import math

def round_wind_chill( temperature, wind_speed):
     return temperature * wind_speed


#def wind_chill(temperature, wind_speed):
#    return temperature + wind_speed

def celsius():
     temperature * (9/5) + 32  

temperature = float(input("What is the temperature"))
choice_temperature = input("fahrenheit or celsius  (F/C)?")  

wind_speeds = []

for wind_speed in range(0,60,5):
    wind_speed += 5 
    if choice_temperature == "C":
        celsius_temperature = ( temperature * 9/5) + 32
        wind_chill = 35.74 + (0.6215 * celsius_temperature) -(35.75*(wind_speed**0.16)) + (0.4275 * celsius_temperature * (wind_speed**0.16) )
        print(f"At temperature { celsius_temperature}F, and wind speed at{wind_speed} mph, the wind chill is: {wind_chill:.2f}F")

    elif choice_temperature == "F":
        wind_chill = 35.74 +(0.6215 * temperature) - (35.75*(wind_speed**0.16)) +(0.4275*temperature* (wind_speed**0.16))
        print(f"At temperature {temperature}F, and wind speed at {wind_speed}mph, the wind chill is: {wind_chill:.2f} F")

