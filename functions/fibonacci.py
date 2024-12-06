def fibonacci(number):
    
    if number <= 1:
        return number
    
    a, b = 0, 1
    for _ in range(number):
        a, b = b, b+a
    
    return a
