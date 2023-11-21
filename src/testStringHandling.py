import json

test = ['a', 'b', 'c', 'd', 'a', 'c']
print(test)
test = set(test)
print(test)

year = 2023
event = "testing"
print(f'this is {year} and I\'m  {event}')
print(("this is {} and I\'m {}").format(year,event))

x = 50
y = "price"
print("The " + y + " is " + repr(x))

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(f'{name:10}  ==> {phone:10d}')
    print(f'{name=} ==> {phone=}')

js = '{"name": "John", "age": 30, "city": "New York"}'

y = json.loads(js)

print(f'{y}, and  {y["name"]} \'s age is {y["age"]}')

diss = {"name": "John", "age": 30, "city": "New York"}

z = json.dumps(diss)

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

w = json.dumps(x,indent= 4,separators=(".","="),sort_keys=True)
print(w)

username = input("enter your name: ")
print(username)