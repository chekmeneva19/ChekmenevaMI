from abc import ABC


class Transport(ABC):
    def __init__(self, coordinates, speed, brand, year, number):
        self.coordinates = coordinates
        self.speed = speed
        self.brand = brand
        self.year = year
        self.number = number

    @property
    def coordinates(self):
        if self.__coordinates is None:
            return self.__coordinates

    @coordinates.setter
    def coordinates(self, coordinates):
        if isinstance(coordinates, tuple) and len(coordinates) == 2:
            self._coordinates = coordinates
        else:
            raise ValueError("Coordinates must be a tuple of two values")

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, speed):
        if isinstance(speed, (int, float)) and speed >= 0:
            self._speed = speed
        else:
            raise ValueError("Speed must be a non-negative number")

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, brand):
        if isinstance(brand, str):
            self._brand = brand
        else:
            raise ValueError("Brand must be a string")

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, year):
        current_year = 2023  # Assuming the current year is 2023
        if isinstance(year, int) and 1900 <= year <= current_year:
            self._year = year
        else:
            raise ValueError("Year must be an integer between 1900 and the current year")

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, number):
        if isinstance(number, str):
            self._number = number
        else:
            raise ValueError("Number must be a string")

    def __str__(self):
        return f"Transport: {self._brand}, Year: {self._year}, Number: {self._number}"

    def isInArea(self, pos_x, pos_y, length, width) -> bool:
        x, y = self.coordinates

        # Проверка нахождения координат в пределах области
        if pos_x <= x <= pos_x + length and pos_y <= y <= pos_y + width:
            return True
        else:
            return False

class Passenger(ABC):
    def __init__(self, passengers_capacity, number_of_passengers):
        self.passengers_capacity = passengers_capacity
        self.number_of_passengers = number_of_passengers

    @property
    def passengers_capacity(self):
        return self.__passengers_capacity

    @passengers_capacity.setter
    def passengers_capacity(self, passengers_capacity):
        if isinstance(passengers_capacity, int) and passengers_capacity >= 0:
            self.__passengers_capacity = passengers_capacity
        else:
            raise ValueError("Passengers capacity must be a non-negative integer")

    @property
    def number_of_passengers(self):
        return self.__number_of_passengers

    @number_of_passengers.setter
    def number_of_passengers(self, number_of_passengers):
        if isinstance(number_of_passengers, int) and number_of_passengers >= 0:
            self.__number_of_passengers = number_of_passengers
        else:
            raise ValueError("Number of passengers must be a non-negative integer")


class Cargo(ABC):
    def __init__(self, carrying):
        self.__carrying = carrying

    @property
    def carrying(self):
        return self.__carrying

    @carrying.setter
    def carrying(self, carrying):
        if not isinstance(carrying, int):
            print("ошибка")
        elif carrying < 0:
            print("ошибка")
        else:
            self.__carrying = carrying


class Plane(Transport):
    def __init__(self, coordinates, speed, brand, year, number, height):
        Transport.__init__(self, coordinates, speed, brand, year, number)
        self.height = height

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            print("ошибка")
        elif not (0 < height < 10000):
            print("ошибка")
        else:
            self.__height = height


class Auto(Transport):
    def __init__(self, coordinates, speed, brand, year, number):
        super().__init__(coordinates, speed, brand, year, number)


class Ship(Transport):
    def __init__(self, coordinates, speed, brand, year, number, port):
        self.port = port
        super().__init__(coordinates, speed, brand, year, number)

    @property
    def port(self):
        return self.__port

    @port.setter
    def port(self, port):
        if not isinstance(port, str):
            print("ошибка")
        elif port == '':
            print("ошибка")
        else:
            self.__port = port


class Car(Auto):
    def __init__(self, coordinates, speed, brand, year, number):
        super().__init__(coordinates, speed, brand, year, number)


class Bus(Auto, Passenger):
    def __init__(self, coordinates, speed, brand, year, number, passengers_capacity, number_of_passengers):
        Auto.__init__(self, coordinates, speed, brand, year, number)
        Passenger.__init__(self, passengers_capacity, number_of_passengers)

    @property
    def passengers_capacity(self):
        return self.__passengers_capacity

    @property
    def number_of_passengers(self):
        return self.__number_of_passengers

    @passengers_capacity.setter
    def passengers_capacity(self, passengers_capacity):
        if isinstance(passengers_capacity, int):
            print("ошибка")
        elif not (0 < passengers_capacity < 60):
            print("ошибка")
        else:
            self.__passengers_capacity = passengers_capacity

    @number_of_passengers.setter
    def number_of_passengers(self, number_of_passengers):
        if isinstance(number_of_passengers, int):
            print("ошибка")
        elif number_of_passengers < self.passengers_capacity:
            print("ошибка")
        else:
            self.__number_of_passengers = number_of_passengers


class CargoAuto(Auto, Cargo):
    def __init__(self, coordinates, speed, brand, year, number, carrying):
        Auto.__init__(self, coordinates, speed, brand, year, number)
        Cargo.__init__(self, carrying)

    @property
    def carrying(self):
        return self.__carrying

    @carrying.setter
    def carrying(self, carrying):
        if isinstance(carrying, int):
            print("ошибка")
        elif not (0 < carrying < 1000):
            print("ошибка")
        else:
            self.__carrying = carrying


class Boat(Ship):
    def __init__(self, coordinates, speed, brand, year, number, port):
        super().__init__(coordinates, speed, brand, year, number, port)


class PassengerShip(Ship, Passenger):
    def __init__(self, coordinates, speed, brand, year, number, port, passengers_capacity, number_of_passengers):
        Passenger.__init__(self, passengers_capacity, number_of_passengers)
        Ship.__init__(self, coordinates, speed, brand, year, number, port)


class CargoShip(Ship, Cargo):
    def __init__(self, coordinates, speed, brand, year, number, port, carrying):
        Ship.__init__(self, coordinates, speed, brand, year, number, port)
        Cargo.__init__(self, carrying)


# аналогично создать классы для самолета и класс Seaplane(Plane, Ship).

class Seaplane(Plane, Ship):
    def __init__(self, coordinates, speed, brand, year, number, height, port):

        super().__init__(coordinates, speed, brand, year, number, height)
        super(Plane, self).__init__(coordinates, speed, brand, year, number, port)

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            print("ошибка")
        elif height > 1000 or height < 0:
            print("ошибка")
        else:
            self.__height = height



seaPlane = Seaplane((2.0, 5.0), 90, "ABC", 2020, "AM100", 10, "first")
print(seaPlane.number, seaPlane.height, seaPlane.port)
