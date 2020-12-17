def mysum(*data, l=0):
    answer = 0
    for i in data:
        answer += i 

    return answer


def average(*data, l=0):
    answer = 0
    for i in data:
        answer += i 

    average = answer/len(data)
    return average

print("Sum: ", mysum(1,3,4))
print("Average: ", average(1,3,4), 6)
