numbers = [1, -10, 0, -5, -1000, 100, 7]
maximum = numbers[0]

for num in numbers:
    if num > maximum:
        maximum = num

print("Result: ", maximum)


x = 132453
print(type(x))
x = "Game of thrones"
print(type(x))
x = True
print(type(x))


# Initialize list
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Slice from index 2 to 5
print(lst[2:6]) # Output: [3, 4, 5, 6]

# reverse the list
print(lst[::-1])

print(lst[1:5:2])


import random as rand
# initialize a variable n to a random integer between 0 and 10 (incl. range limits).
n = rand.randint(0, 10)

result = [n*n if n>=5 else (n if n==0 else -n) ]
# If the number is lower than 5 but higher than 0, invert it (change sign).

# If the number is 0 do nothing
result
# print the result to the console


print("area(1, 5) = ", 1 * 5)
print("area(1.5, 2.4) = ", 1.5 * 2.4)
print("is_square(1, 8) = ", 1 == 8)
print("is_square(8, 8) = ", 8 == 8)


def area(a,b):
    return a*b

def is_square(a,b):
    return a==b


def area(a,b,user_name="Jeneesh"):
    result = a*b
    return result


class Room:
    def __init__(self,number,capacity,properties):
        assert 1<=number<=100
        self.number= number
        self.capacity = capacity
        self.properties = properties
    
    def __str__(self):
        return f"Room number: {self.number}"


class Building:
    def __init__(self,rooms,size,location):
        self.rooms = rooms
        self.size=size
        self.location = location

    def swap_rooms(self,room1,room2):
        room1.number,room2.number = room2.number,room1.number


room1 = Room(45,10,"Great View")
room2 = Room(46,20,"Large Hall")

building = Building([room1,room2],1400,'north-east')

print(room1)
print(room2)
building.swap_rooms(room1,room2)

print(room1)
print(room2)
