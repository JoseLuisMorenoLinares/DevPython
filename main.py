# print("Hola Mundo");

'''
entero = 1;
decimal = 1.1;
cadena = "cadena";
tuple = 1,"pepe";
buleano = True;

print(type(entero));
print(type(decimal));
print(type(cadena));
print(type(tuple));
print(type(buleano));
'''

'''
name = input('Enter your name:');
print(name);

print('What is your name?');
name = input();
print(name);

x = input('Enter a number: ');
print(type(x));

y = int(input('Enter a number: '));
print(type(y));

x = 5;
print('The number is ' + str(x));
'''

'''
first_number = int(input('Type the first number: '));\
second_number = int(input('Type the second number: '));\
print("The sum is: ", first_number + second_number);
'''

'''
from datetime import date;
print(date.today());
print("Today's date is: " + str(date.today().min));
'''

'''
parsecs = 11;
lightyears = parsecs * 3.26;
print(str(parsecs) + " parsecs is " + str(lightyears) + " lightyears");
print(f'{str(parsecs)} parsecs is {str(lightyears)} lightyears');
print('{0} parsecs is {1} lightyears'.format(parsecs, lightyears));
'''

'''
import sys

print(sys.argv)
print(sys.argv[0]) # program name
print(sys.argv[1]) # first arg
'''

'''
print("Welcome to the greeter program")
name = input("Enter your name: ")
print("Greetings " + name)
'''

'''
print("calculator program")
first_number = input("first number: ")
second_number = input("second number: ")
print(first_number + second_number)
print(int(first_number) + int(second_number))
'''

'''
parsecs_input = input("Input number of parsecs:")
parsecs = int(parsecs_input)
lightyears = 3.26156 * parsecs

print(parsecs_input + " parsecs is " + str(lightyears) + " lightyears")
'''

'''
a = 97
b = 55
# test expression
if a < b:
    # statement to be run
    print("pp")
print(b)
'''

'''
a = 24
b = "a"
if a <= 0:
    print(a)
print(a, b)
'''

'''
a = 27
b = 93
if a >= b:
    print(a)
else:
    print(b)
'''

'''
a = 27
b = 93
if a < b:
    print("a is less than b")
elif a > b:
    print("a is greater than b")
else: 
    print ("a is equal to b")
'''

'''
a = 16
b = 25
c = 27
if a > b:
    if b > c:
        print ("a is greater than b and b is greater than c")
    else: 
        print ("a is greater than b and less than c")
elif a == b:
    print ("a is equal to b")
else:
    print ("a is less than b")
'''

'''
# Opcion 1
object_size = 10
if object_size > 5:
    print('We need to keep an eye on this object')
else:
    print('Object poses no threat.')
'''

'''
# Opcion 2
object_size = 10
print('We need to keep an eye on this object') if object_size > 5 else print('Object poses no threat.')
'''

'''
a = 23
b = 34
if a == 34 or b == 34:
    print(a + b)
'''

'''
a = 23
b = 34
if a == 34 and b == 34:
    print (a + b)
'''

'''
Exercise: Use complex logic to determine possible evasive maneuvers
In the previous exercise you created code to test the size of the object. Now you will test both the object's size and proximity. You will use the same threshold for size of 5m3. If the object is both larger than the threshold and within 1000km of the ship evasive maneuvers will be required.

For this step you will be presented with the goal for the exercise, followed by an empty cell. Enter your Python into the cell and run it. The solution is at the bottom of the exercise.

Add the code to the cell below to create two variables: object_size and proximity. Set object_size to 10 to represent 10m3. Set proximity to 9000.

Then add the code to display a message saying Evasive maneuvers required if both object_size is greater than 5 and proximity is less than 1000. Otherwise display a message saying Object poses no threat.
'''

'''
# Opcion uno
object_size = 10
proximity = 9000

if object_size > 5 and proximity < 1000:
    print('Evasive maneuvers required')
else:
    print('Object poses no threat')
'''

'''
# Opcion dos
object_size = 10
proximity = 9000

print('Evasive maneuvers required') if (object_size > 5 and proximity < 1000) else print('Object poses no threat')
'''

'''
fact = "The Moon has no atmosphere."
fact + "No sound can be heard on the Moon."
print(fact)
'''

'''
multiline = """Facts about the Moon:
 There is no atmosphere. 
 There is no sound."""
print(multiline)
'''

'''
print("temperatures and facts about the moon".title())
print("temperatures and facts about the moon".upper())

temperatures = "Daylight: 260 F Nighttime: -280 F"
temperatures_list = temperatures.split()
print(temperatures_list)
print("Moon" in "This text will describe facts and challenges with space travel")
print("Moon" in "This text will describe facts about the Moon")

temperatures = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
print(temperatures.find("Moon"))

temperatures = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
print(temperatures.find("Mars"))

temperatures = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
print(temperatures.count("Mars"))
print(temperatures.count("Moon"))
'''

'''
temperatures = "Mars Average Temperature: -60 C"
parts = temperatures.split(':')
print(parts)
print(parts[-1])

array = "1,2,3,4".split(",")
print(array[1: -1])
print(array[: -1])

moon_facts = ["The Moon is drifting away from the Earth.", "On average, the Moon is moving about 4cm every year."]
print(' '.join(moon_facts))
'''

'''
Exercise: Transform strings
There are several operations you can perform on strings when you manipulate them. In this exercise, you'll use string methods to modify text with facts about the Moon and then extract information to create a short summary.

This exercise is broken into a series of steps. For each step you will be presented with the goal for the step, followed by an empty cell. Enter your Python into the cell and run it. The solution for each step will follow each cell.
'''

'''
text = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C."""
sentences = text.split(".")

print(sentences)
print(sentences[0])

print(sentences)

for sentence in sentences:
    if 'temperature' in sentence:
        print(sentence.strip())
'''

'''
print("""Both sides of the %s get the same amount of sunlight, but only one side is seen from %s because the %s rotates around its own axis when it orbits %s.""" % ("Moon", "Earth", "Moon", "Earth"))

mass_percentage = "1/6"
print("On the Moon, you would weigh about %s of your weight on Earth.".strip() % mass_percentage)
print("On the Moon, you would weigh about {} of your weight on Earth.".format(mass_percentage))
print("""You are lighter on the {0}, because on the {0} you would weigh about {1} of your weight on Earth.""".format("Moon", mass_percentage))
print("""You are lighter on the {moon}, because on the {moon} you would weigh about {mass} of your weight on Earth.""".format(moon="Moon", mass=mass_percentage))
'''

'''
moon="Moon"
mass_percentage="1/6"
print(f"You are lighter on the {moon}, because on the {moon} you would weigh about {mass_percentage} of your weight on Earth.")
print(f"On the Moon, you would weigh about {round(100/6, 1)}% of your weight on Earth.")
'''

'''
Exercise: Formatting strings
Knowing how to format strings is essential when you're presenting information from a program. There are a few different ways to accomplish this in Python. In this exercise, you use variables that hold key facts about gravity on various moons and then use them to format and print the information.

This exercise is broken into a series of steps. For each step you will be presented with the goal for the step, followed by an empty cell. Enter your Python into the cell and run it. The solution for each step will follow each cell.
Create the variables
Start by creating three variables, name, gravity, and planet, and set them to the following values:
name: Ganymede
planet: Mars
gravity: 1.43

'''

'''
name = "Ganymede"
planet = "Mars"
gravity = 1.43

template = f"""Gravity Facts about {name}
{'-' * 25}
Planet Name: {planet}
Gravity on {name}: {gravity} m/s2"""

print(template)
'''
'''
seconds = 1042
display_minutes = 1052 // 60
display_seconds = 1042 % 60

print(display_minutes)
print(display_seconds)
'''

'''
numeraco = 235**455
print(numeraco)
print(type(numeraco))
'''

'''
Arithmetic operators in Python
Python provides common arithmetic operators so you can perform mathematic operations in your code. These include the four core operations of addition, subtraction, multiplication, and division.

Let's explore how we can create a program that can calculate the distance between two planets. We'll start by using two planet distances: Earth (149,597,870 km) and Jupiter (778,547,200 km).

This exercise is broken into a series of steps. For each step you will be presented with the goal for the step, followed by an empty cell. Enter your Python into the cell and run it. The solution for each step will follow each cell.

Note: Remove the commas when you're using the values.

Create variables to store the distances
Start by creating two variables named first_planet and second_planet. Set first_planet to the distance from the sun to Earth, and second_planet for the distance from the sun to Jupiter.
'''

'''
first_planet = 149597870
second_planet = 778547200

distance_km = second_planet - first_planet
print(distance_km)

distance_mi = distance_km / 1.609344
print(distance_mi)
'''

'''
from math import pi
print(pi)

import math
print(pi)
'''

'''
numero1 = input('Introduce numero1: ')
numero2 = input('Introduce numero2: ')

numero1 = int(numero1)
numero2 = int(numero2)
print (numero1 + numero2)
'''


'''
Create an application to work with numbers and user input
You'll frequently need to convert string values into numbers to properly perform different operations, or determine the absolute value of a number. In this exercise, you will create a project to calculate the distance between two planets based on user input.

This exercise is broken into a series of steps. For each step you will be presented with the goal for the step, followed by an empty cell. Enter your Python into the cell and run it. The solution for each step will follow each cell.

Read the values from the user
To create our application, we want to read the distance from the sun for two planets, and then display the distance between the planets. We'll do this by using input to read the values, int to convert to integer, and then abs to convert the result into its absolute value.

Start by adding the code to prompt the user for the distance between the sun and the first planet, and then the second. Store each result in variables named first_planet_input and second_planet_input.
'''

'''
first_planet_input = input('Enter the distance from the sun for the first planet in km: ')
second_planet_input = input('Enter the distance from the sun for the second planet in km: ')

first_planet_input = float(first_planet_input)
second_planet_input = float(second_planet_input)
resultado = abs(int(second_planet_input - first_planet_input))
print (resultado)
'''

'''
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
print("The first planet is", planets[0])
print("The second planet is", planets[1])
print("The third planet is", planets[2])

planets[3] = "Red Planet"
print("Mars is also known as", planets[3])
'''

'''
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"]
print(planets.pop()) # Goodbye, Pluto
mercury_index = planets.index("Mercury")
print("Mercury is the", mercury_index + 1, "planet from the sun")
print(planets.pop(0))  # Goodbye, Mercury
number_of_planets = len(planets)
print("No, there are definitely", number_of_planets, "planets in the solar system.")

print("The last planet is", planets[-1])
print("The penultimate planet is", planets[-2])
'''

'''
Exercise: Use lists to store planet names
Lists allow you to store multiple values in a single variable. In this notebook you'll create a project to display information about the planets.

This exercise is broken into a series of steps. For each step you will be presented with the goal for the step, followed by an empty cell. Enter your Python into the cell and run it. The solution for each step will follow each cell.

Add all planets to a list
First, create a variable named planets. Add the eight planets (without Pluto) to the list. The planets are:

Mercury
Venus
Earth
Mars
Jupiter
Saturn
Uranus
Neptune
Finish by using print to display the list of planets.
'''


'''
import os

os.system("cls")
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
gravity_on_planets = [0.378, 0.907, 1, 0.377, 2.36, 0.916, 0.889, 1.12]
bus_weight = 124054 # in Newtons, on Earth

print(planets)
print(f"Hay {len(planets)} en el sistema solar")
print(planets[-1], "is the last planet")

for i in range(len(planets)):
    print(f"En {planets[i]} el peso del autobus es {int(bus_weight * gravity_on_planets[i]/9.81)}")
    print(f"En {planets[i]} el peso del autobus es {(bus_weight * gravity_on_planets[i]/9.81):.2f}")
    print(f"En {planets[i]} el peso del autobus es {(bus_weight * gravity_on_planets[i]/9.81):.1F}")

print("The lightest a bus would be in the solar system is", bus_weight * min(gravity_on_planets), "N")
print("The heaviest a bus would be in the solar system is", bus_weight * max(gravity_on_planets), "N")
'''

'''
amalthea_group = ["Metis", "Adrastea", "Amalthea", "Thebe"]
galilean_moons = ["Io", "Europa", "Ganymede", "Callisto"]

regular_satellite_moons = amalthea_group + galilean_moons
print("The regular satellite moons of Jupiter are", regular_satellite_moons)
regular_satellite_moons.sort()
print("The regular satellite moons of Jupiter are", regular_satellite_moons)
regular_satellite_moons.sort(reverse=True)
print("The regular satellite moons of Jupiter are", regular_satellite_moons)

print()
nueva_lista = sorted(regular_satellite_moons)
print(nueva_lista)
nueva_lista = sorted(regular_satellite_moons, reverse=True)
print(nueva_lista)
'''

'''
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
user_planet = input("Please enter the name of the planet (with a capital letter to start)")
planet_index = planets.index(user_planet)

print("Here are the planets closer than " + user_planet)
print(planets[0:planet_index])

print("Here are the planets further than " + user_planet)
print(planets[planet_index + 1:])
'''

'''
# Create the variable for user input
user_input = ''
# Create the list to store the values
inputs = []

import os
os.system("cls")

# The while loop
while user_input.lower() != 'done':
    # Check if there's a value in user_input
    if user_input:
        # Store the value in the list
        inputs.append(user_input)
    if len(inputs) > 0:
        print(inputs)
    # Prompt for a new value
    user_input = input('Enter a new value, or done when done: ')

print(inputs)
'''


'''
import os
os.system("cls")

new_planet = ''
planets = []

while new_planet.lower() != 'done':
    if new_planet:
        planets.append(new_planet)
    new_planet = input('Enter a new planet, or done if done: ')

print(planets)
'''

'''
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

print("The first planet is ", planets[0])
print("The second planet is ", planets[1])
print("The third planet is ", planets[2])

countdown = [4, 3, 2, 1, 0]
for number in countdown:
    print(number)
    print(planets[number])

print("Blast off!! 🚀")
'''

'''
from time import sleep

countdown = [4, 3, 2, 1, 0]

for number in countdown:
    print(number)
    sleep(1)  # Wait 1 second
print("Blast off!! 🚀")
'''


'''
# Run this cell and provide a list of planets
import os
os.system("cls")

new_planet = ''
planets = []

while new_planet.lower() != 'done':
    if new_planet:
        planets.append(new_planet)
    print(planets)
    new_planet = input('Enter a new planet or done if done: ')

for planeta in planets:
    print(planeta)
'''

'''
import os
os.system("cls")

planet = {
    'name': 'Earth',
    'moons': 1
}

print(planet.get('name'))
print(planet['name']) # planet['name'] is identical to using planet.get('name')

print(planet.get('wibble')) # Returns None
print(planet.get('wibble', "Tierra")) # Returns Tierra
# print(planet['wibble']) # Throws KeyError

planet.update({'name': 'Makemake'})
print(planet.get('name'))
# No output: name is now set to Makemake.

planet['orbital period'] = 4333

# planet dictionary now contains: {
#   name: 'jupiter'
#   moons: 79
#   orbital period: 4333
# }

print(planet.keys())
print(planet.values())

planet.pop('orbital period')

# planet dictionary now contains: {
#   name: 'jupiter'
#   moons: 79
# }

print(planet.keys())
print(planet.values())

planet.update({
    'name': 'Jupiter',
    'moons': 79
})

planet['diameter (km)'] = {
    'polar': 133709,
    'equatorial': 142984
}

print(planet.keys())
print(planet.values())

print(f'{planet["name"]} polar diameter: {planet["diameter (km)"]["polar"]} equatorial diameter: {planet["diameter (km)"]["equatorial"]}')
'''

'''
import os
os.system("cls")

rainfall = {
    'october': 3.5,
    'november': 4.2,
    'december': 2.1
}

# Opcion 1
for key in rainfall.keys():
    print(f'{key}: {rainfall[key]}cm')

print()
# Opcion 2
for item in rainfall.items():
    print(f'{item[0]}: {item[1]}cm')

print()
# Opcion 3
for key, value in rainfall.items():
    print(f'{key}: {value}cm')

print()
if 'december' in rainfall:
    rainfall['december'] = rainfall['december'] + 1
else:
    rainfall['december'] = 1

if 'enero' in rainfall:
    rainfall['enero'] = rainfall['enero'] + 1
else:
    rainfall['enero'] = 1

# Because december exists, the value will be 3.1

for key, value in rainfall.items():
    print(f'{key}: {value}cm')

total_rainfall = 0
for value in rainfall.values():
    total_rainfall = total_rainfall + value

print()
print(f'There was {total_rainfall}cm in total.')
print(f'There was {sum(rainfall.values())}cm in total.')
'''

'''
import os
import numpy as np

os.system("cls")

planet_moons = {
    'mercury': 0,
    'venus': 0,
    'earth': 1,
    'mars': 2,
    'jupiter': 79,
    'saturn': 82,
    'uranus': 27,
    'neptune': 14,
    'pluto': 5,
    'haumea': 2,
    'makemake': 1,
    'eris': 1
}

print(planet_moons.keys())
print(planet_moons.values())
print(f"Total de planetas: {len(planet_moons)}")
print(f"Total de lunas: {sum(planet_moons.values())}")
print(f"Media de lunas/planetas: {sum(planet_moons.values())/len(planet_moons)}") # Opcion 1
print(f"Media de lunas/planetas: {np.mean(list(planet_moons.values()))}") # Opcion 2
print(list(planet_moons.keys()))
'''

'''
import os
os.system("cls")

def rocket_parts():
    return "payload, propellant, structure"



output = rocket_parts()
print(output)
'''

'''
import os
os.system("cls")

def distance_from_earth(destination):
    if destination == "Moon":
        return "238,855"
    else:
        return "Unable to compute to that destination"

print(distance_from_earth("Moon"))
print(distance_from_earth("Tierra"))
print(distance_from_earth()) # esto falla al no pasar el parametro
'''

'''
import os
os.system("cls")

def days_to_complete(distance, speed):
    hours = distance/speed
    return hours/24

resultado = days_to_complete(238855, 75)

print(resultado)
'''

'''
import os
os.system("cls")

def generate_report(main_tank, external_tank, hydrogen_tank):
    return f"""Fuel Report:
    Main tank: {main_tank}
    External tank: {external_tank}
    Hydrogen tank: {hydrogen_tank} 
    """

print(generate_report(80, 70, 75))
'''

'''
import os
os.system("cls")

from datetime import timedelta, datetime

def arrival_time(hours=51):
    now = datetime.now()
    arrival = now + timedelta(hours=hours)
    return arrival.strftime("Arrival: %A %H:%M")

print(arrival_time(1))
print(arrival_time(48))
'''

'''
import os
os.system("cls")

from datetime import timedelta, datetime

def arrival_time(destination, hours=51):
    now = datetime.now()
    arrival = now + timedelta(hours=hours, days=1)
    return arrival.strftime(f"{destination} Arrival: %A %H:%M")

print(arrival_time("Moon", 5))
'''
'''
import os
os.system("cls")

def variable_length(*args):
    print(args)

variable_length(1,2,5, "r", 6)
'''

'''
import os
os.system("cls")

def sequence_time(*args):
    total_minutes = sum(args)
    if total_minutes < 60:
        return f"Total time to launch is {total_minutes} minutes"
    else:
        return f"Total time to launch is {total_minutes/60} hours"

print(sequence_time(1,2,3,4,5))

print(sequence_time(4, 14, 48))
'''

'''
import os
os.system("cls")


def variable_length(**kwargs):
    print(kwargs)

    for key, value in kwargs.items():
        print(f'{key}: {value}cm')

def crew_members(**kwargs):
    print(f"{len(kwargs)} astronauts assigned for this mission:")
    for title, name in kwargs.items():
        print(f"{title}: {name}")


variable_length(tanks=1, day="Wednesday", pilots=3)
crew_members(captain="Neil Armstrong", pilot="Buzz Aldrin", command_pilot="Michael Collins")
'''

'''
import os
os.system("cls")

def fuel_report(**fuel_tanks):
    for name, value in fuel_tanks.items():
        print(f'{name}: {value}')

fuel_report(main = 50, external = 100, emergency = 60)
'''

'''
import os
os.system("cls")

def main():
    open("/path/to/mars.jpg")

if __name__ == '__main__':
    main()
'''

'''
import os
os.system("cls")

def main():
    try:
        configuration = open('config.txt')
    except FileNotFoundError:
        print("Couldn't find the config.txt file!")
    except IsADirectoryError:
        print("Found config.txt but it is a directory, couldn't read it")
    except (BlockingIOError, TimeoutError):
        print("Filesystem under heavy load, can't complete reading configuration file")        
    except Exception as ex:
        print(ex)
    finally:
        print("Todo correcto")

main()
'''

'''
import os
os.system("cls")

def main():
    try:
        open("config.txt")
    except OSError as err:
        if err.errno == 2:
            print("Couldn't find the config.txt file!")
        elif err.errno == 13:
            print("Found config.txt but couldn't read it")

main()
'''

'''
import os
os.system("cls")

loaded_config = """# Rocket Ship Configuration File!
fuel_tanks=4
oxygen_tanks=3
initial_propulsion_level=84
$ End of file"""

parsed_config = {}
for line in loaded_config.split('\n'):
    try:
        key, value = line.split('=')
        parsed_config[key] = value
    except ValueError:
        print(f'Unable to parse {line}')
print(parsed_config)
'''

'''
import os
os.system("cls")

def water_left(astronauts, water_left, days_left):
    daily_usage = astronauts * 11
    total_usage = daily_usage * days_left
    total_water_left = water_left - total_usage
    return f"Total water left after {days_left} days is: {total_water_left} liters"

print(water_left(5, 100, 2))
'''

'''
import os
os.system("cls")

def water_left(astronauts, water_left, days_left):
    daily_usage = astronauts * 11
    total_usage = daily_usage * days_left
    total_water_left = water_left - total_usage
    if total_water_left < 0:
        raise RuntimeError(f"There is not enough water for {astronauts} astronauts after {days_left} days!")
    return f"Total water left after {days_left} days is: {total_water_left} liters"

def alert_navigation_system(err):
    print(err)

try:
    #print(water_left(5, 100, 2))
    print(water_left("3", "200", None))
except RuntimeError as err:
    alert_navigation_system(err)
except Exception as ex:
    alert_navigation_system(ex)
'''

'''
import os
os.system("cls")

def water_left(astronauts, water_left, days_left):
    for argument in [astronauts, water_left, days_left]:
        try:
            # If argument is an int, the following operation will work
            argument / 10
        except TypeError:
            # TypeError will be raised only if it isn't the right type 
            # Raise the same exception but with a better error message
            raise TypeError(f"All arguments must be of type int, but received: '{argument}'")
    daily_usage = astronauts * 11
    total_usage = daily_usage * days_left
    total_water_left = water_left - total_usage
    if total_water_left < 0:
        raise RuntimeError(f"There is not enough water for {astronauts} astronauts after {days_left} days!")
    return f"Total water left after {days_left} days is: {total_water_left} liters"

def alert_navigation_system(err):
    print(err)

try:
    print(water_left("3", "200", None))
except RuntimeError as err:
    alert_navigation_system(err)
'''

'''
# Creating a utility to convert strings to boolean values
import os
os.system("cls")

true_values = ['yes', 'y']
false_values = ['no', 'n']


## Create the function to test for true or false

# You will use `true_values` and `false_values` to create a function named `str_to_bool` to convert strings to Boolean values. `str_to_bool` will accept one parameter named `value`.

# Create the function `str_to_bool`. Convert `value` to lower case letters. If `value` matches an entry in `true_values` the function should return `True`. If `value` matches an entry in `false_values` it should return `False`. If it doesn't match any of the values, it should raise a `ValueError`, with a message of **Invalid entry**.
def str_to_bool(value):
    value = value.lower()
    if value in true_values:
        return True
    elif value in false_values:
        return False
    raise ValueError("Tipo Erroneo")

try:
    print(str_to_bool("Yes"))
    print(str_to_bool("N"))
    print(str_to_bool(""))
except Exception as ex:
    print(ex)
'''


class Car:
    def __init__(self):
        self.color = "Red" # ends up on the object
        self.make = "Mercedes" # becomes a local variable in the constructor

car = Car()
print(car.color) # "Red"
print(car.make) # would result in an error, `make` does not exist on the object
