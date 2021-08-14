

input_value=int(input('enter value in intiger'))
sum=0
for value in range(1,input_value+12):
    flor = input_value/value
    sum += int(value*flor)
    #sum = sum+product
print(sum)
