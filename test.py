

def max_num(numbers):
    max_ = 0
    second_max = numbers[0]
    for i in numbers[1:]:
        if i > max_:
            max_ = i
        elif i <= max_ and i >= second_max:
            second_max = i
    return second_max


numbers= [2,5,1,-4,44,22,10]
print(max_num(numbers))
