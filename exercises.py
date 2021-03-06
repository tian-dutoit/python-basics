def length_function(word):
    if type(word) == int:
        return "Sorry integers don't have length"
    elif type(word) == float:
        return "Sorry floats don't have length"    
    else:  
        return len(word)  

def temp_converter(celsius):
    if celsius < -273.15:
      return "Lowest possible temperature is -273.15 Celsius"
    else:
      return float(celsius * 9 / 5 + 32)

def fruits():
    file = open("fruits.txt")
    content = file.read()
    file.close()
    print(content)

def loops():
    mylist= [1, 2, 3, 4, 5]
    for number in mylist:
        print(number)

def greater():
    mylist= [1, 2, 3, 4, 5]
    for number in mylist:
        if number > 2:
            print(number)

def fruits_length():
    file = open("fruits.txt")
    content = file.read()
    # split = content.split() both appear to work
    split = content.splitlines()
    file.close()
    for fruit in split:
      print(len(fruit))

    # file = open("fruits.txt")
    # content = file.readlines()
    # content = [line.strip() for line in content]
    # file.close()
    # for i in content:
    #     print(len(i))

def tempiteration():
    temperatures = [10,-20,-289,100]
    for temperature in temperatures:
        print(temp_converter(temperature))

def createandread():
    numbers = [1, 2, 3]
    file = open('open.py', 'w')
    for number in numbers:
        file.write(str(number) + "\n")
    file.close()

def iterations():
    a = ['a', 'b', 'c']
    b = [1, 2, 3]
    for i, j in zip(a, b):
        print("%s is %s" % (i, j)) 

def output():
    temperatures = [10,-20,-289,100]
    with open("output.py", "w") as myfile:
        for temperature in temperatures:
            if temperature > -273.15:
                converted = temperature * 9 / 5 + 32
                myfile.write(str(converted) + "\n")  

# Could make it so list and filepath are paramaters of the function 
  
print(length_function("hello how long is this?"))
print(length_function(5))
print(length_function(5.5))
print(temp_converter(10))
print(temp_converter(-1110))
fruits()
loops()
greater()
fruits_length()
tempiteration()
createandread()
iterations()
output()

