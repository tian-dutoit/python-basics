def length_function(word):
    if(type(word) == int):
        return "Sorry integers don't have length"
    else:  
        return len(word)  

def temp_converter(celsius):
    return celsius * 9 / 5 + 32

  
print(length_function("hello how long is this?"))
print(length_function(5))
print(temp_converter(10))
