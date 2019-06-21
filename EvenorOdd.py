def even_or_odd(number):
    if number == 0:
        return 'Even'
    elif number % 2 == 0:
        return 'Even'
    elif number % 2 == 1:
        return 'Odd'
    else:
        "Please enter a integer"

def positive_sum(arr):
    sum = 0
    for num in arr:
        if num > 0:
            sum = sum + num
    return sum

def fizzbuzz(n):
    arr =[]
    for num in range (1, n + 1):
        if num % 3 == 0:
            arr.append("Fizz")
        elif num % 5 == 0:
            arr.append("Buzz")
        elif num % 3 == 0 and num % 5 == 0:
            arr.append("FizzBuzz")
        else:
            arr.append(num)
return arr

def openOrSenior(data):
    list =[]
    for i in data:
        if i[0] >= 55 and i[1] > 7:
            list.append("Senior")
        else:
            list.append("Open")
    return list
