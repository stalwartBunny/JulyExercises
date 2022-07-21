def add(a, b):
    print(f"Adding your values:")
    return a + b

def subtract(a, b):
    print(f"Subtracting 2nd value from 1st:")
    return a - b

def multiply(a, b):
    print(f"Multiplying your values:")
    return a * b

def divide(a, b):
    print(f"Dividing the first value by the second:")
    return a / b

def modulus(a, b):
    print(f"Determining the remainder of the first value divided by the second:")
    return a % b

age = add(27, 7)
height = subtract(200, 20)
weight = multiply(55, 3)
strength = divide(160, 4)
mod = modulus(53, 17)

print(f"I am not {age} years old. I am roughly {height} cms tall, as well as {weight} lbs with a grip strength on average being {strength}. And here's a random modulus that should be 3: {modulus}")
answer = age + height / weight - strength 
print(f"It's super nice that python recognizes order of operations: so age plus height divided by weight minus strength should actually work! The answer being... {answer}.")
