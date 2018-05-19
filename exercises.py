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
      return celsius * 9 / 5 + 32

  
print(length_function("hello how long is this?"))
print(length_function(5))
print(length_function(5.5))
print(temp_converter(10))
print(temp_converter(-1110))

