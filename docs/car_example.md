# Car Example

The following set of classes is an example of instantiating classes and nesting classes.

The `blueprints` module contains the __template__, __abstraction__, or __class__, while the `car_factory` module contains the __implementation__, or __instantiation__.

__blueprints.py__
```
class Engine:

    def __init__(self, displacement, cylinders, configuration, notes=''):
        self.__displacement = displacement
        self.__cylinders = cylinders
        self.__configuration= configuration
        self.__notes = notes

    def change(self, displacement, cylinders, configuration, notes=''):
        self.__displacement = displacement
        self.__cylinders = cylinders
        self.__configuration= configuration
        self.__notes = notes

    def get_displacement(self):
        return self.__displacement

    def get_cylinders(self):
        return self.__cylinders

    def get_configuration(self):
        return self.__configuration

    def get_notes(self):
        return self.__notes

    def __str__(self):
        if self.__notes:
            notes = ' - ' + self.__notes
        else:
            notes = ''
        return "{:}L {:}{:}".format(self.__displacement, self.__configuration, self.__cylinders) + notes


class Transmission:

    def __init__(self, type, gear_count):
        self.__type = type
        self.__gear_count = gear_count

    def get_type(self):
        return self.__type

    def get_gear_count(self):
        return self.__gear_count

    def __str__(self):
        return "{:}-Speed {:}".format(self.__gear_count, self.__type)


class Tires:

    def __init__(self, tire_width, wall_rim_ratio, rim_size):
        self.__tire_width = tire_width
        self.__wall_rim_ratio = wall_rim_ratio
        self.__rim_size = rim_size

    def get_tire_width(self):
        return self.__tire_width

    def get_wall_rim_ratio(self):
        return self.__wall_rim_ratio

    def get_rim_size(self):
        return self.__rim_size

    def __str__(self):
        return "{:}/{:}R{:}".format(self.__tire_width, self.__wall_rim_ratio, self.__rim_size)


class Car:
    def __init__(self, year, make, model, trim, engine, transmission, tires):
        self.__year = year
        self.__make = make
        self.__model = model
        self.__trim = trim
        self.__engine = engine
        self.__transmission = transmission
        self.__tires = tires

    def get_year(self):
        return self.__year

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_trim(self):
        return self.__trim

    def get_engine(self):
        return self.__engine

    def get_transmission(self):
        return self.__transmission

    def get_tires(self):
        return self.__tires

    def __str__(self):
        return "{:} {:} {:} {:}\nEngine: {:}\nTransmission: {:}\nTires: {:}" \
            .format(self.__year, self.__make, self.__model, self.__trim,
                    self.__engine, self.__transmission, self.__tires)

```

__car_factory.py__
```
from src.blueprints import Engine
from src.blueprints import Transmission
from src.blueprints import Tires
from src.blueprints import Car

################
# Simple Example
################

# 2019 Toyota Corolla SE
# Data courtesy of: https://www.toyota.com/Corolla
corolla_engine = Engine(1.8, 4, 'I')
corolla_transmission = Transmission('Manual', 6)
corolla_tires = Tires(205, 55, 16)
corolla_se = Car(2019, 'Toyota', 'Corolla', 'SE', corolla_engine, corolla_transmission, corolla_tires)

print('Single Car Example')
print('--------------------')
print(corolla_se)
print('--------------------')


################
# Trims Example
################

# 2019 Ford Mustang
# Data courtesy of: https://www.ford.com/mustang
mustang_base_engine = Engine(2.3, 4, 'I', 'Turbocharged')
mustang_base_transmission = Transmission('Automatic', 10)
mustang_base_tires = Tires(235, 55, 17)
mustang_base = Car(2019, 'Ford', 'Mustang', 'EcoBoost',
                   mustang_base_engine, mustang_base_transmission, mustang_base_tires)

mustang_shelby_engine = Engine(5.2, 8, 'V', 'Flat Plane Crank')
mustang_shelby_transmission = Transmission('Manual', 6)
mustang_shelby_tires = Tires(305, 35, 19)
mustang_shelby = Car(2019, 'Ford', 'Mustang', 'Shelby GT350',
                     mustang_shelby_engine, mustang_shelby_transmission, mustang_shelby_tires)

print('Trims Example')
print('--------------------')
print(mustang_base)
print('--------------------')
print(mustang_shelby)
print('--------------------')

############################
# Sharing Instances Example
# Changing one component will
# change it for all vehicles.
############################

# Data courtely of:
#    * https://www.ramtrucks.com/
#    * https://www.chrysler.com/300.html
#    * https://www.dodge.com/challenger.html
#    * https://www.dodge.com/charger.html
chrysler_hemi = Engine(5.7, 8, 'V', 'HEMI')

ram_transmission = ('Automatic', 8)
ram_tires = Tires(275, 65, 18)
ram_1500 = Car(2019, 'Dodge', 'RAM', '1500 - Crew Cab', chrysler_hemi, ram_transmission, ram_tires)

challenger_transmission = Transmission('Automatic', 8)
challenger_tires = Tires(245, 45, 20)
challenger = Car(2019, 'Dodge', 'Challenger', 'R/T', chrysler_hemi, challenger_transmission, challenger_tires)

charger_transmission = Transmission('Automatic', 8)
charger_tires = Tires(245, 45, 20)
charger = Car(2019, 'Dodge', 'Charger', 'R/T', chrysler_hemi, charger_transmission, charger_tires)

print('Sharing Instances Example - Before Change')
print('--------------------')
print(ram_1500)
print('--------------------')
print(challenger)
print('--------------------')
print(charger)
print('--------------------')

# Note how this line changes the engine for all vehicles it was put in.
# This is because they all share the same instance of an engine, NOT the same blueprint.
# Object-Oriented design will allow you to do this, but you must be aware that it may
# result in unintended consequences.
chrysler_hemi.change(3.6, 6, 'V', 'Different Engine')

print('Sharing Instances Example - After Change')
print('--------------------')
print(ram_1500)
print('--------------------')
print(challenger)
print('--------------------')
print(charger)
print('--------------------')

```

[Go back to the main lab](../README.md)