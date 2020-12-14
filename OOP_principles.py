
import random

class Node():
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next



class MyQueue():
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, x):
        if self.head == None:
            self.tail = self.head = Node(x, None)
        else:
            self.tail.next = self.tail = Node(x, None)

    def remove(self, pos):
        if self.head == None:
            return
        current = self.head
        count = 0
        if pos == 0:
            self.head = self.head.next
            return
        while current != None:
            if count == pos:
                if current.next == None:
                    self.last = current
                previos.next = current.next
                break
            previos = current
            current = current.next
            count += 1

    def to_list(self):
        if self.head == None:
            return self.list
        self.list = []
        current = self.head
        while current != None:
            self.list.append(current.value)
            current = current.next
        return self.list

    def clear(self):
        self.__init__()


        

class Country():
    def __init__(self, name="not received", capital="not received", population="X", area="not received"):
        self.name = name 
        self.capital = capital 
        self.population = population
        self.area = area
    def __str__(self):
        information = ("The country name is " + self.name + " The capital is " + self.capital +\
             " Population " + str(self.population) + " million of people " + " The area is " +str(self.area) +" km 2^")
        return (information)


"""
a = Country("Russia", "Moscow", 177, 1828348)
a.__str__()

a=Country(capital="Riga")
a.__str__()
"""

numbers = MyQueue()
for i in range(10):
    numbers.add(random.randint(0, 100))
print(numbers.to_list())


country_list = [Country("Russia", "Moscow", 147, 17098246), Country("USA", "Washington", 328, 9826675), \
    Country("Uzbekistan", "Tashkent"), Country("Programmers_land", "Silicon Valley")]
countries = MyQueue()
    
for i in country_list:
    countries.add(i.__str__())


for t in countries.to_list():
    print(t)
