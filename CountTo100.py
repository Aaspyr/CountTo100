print ("A program adds numbers divisible by 3.")

score = 0
while score < 100:
    number = int(input("Enter the number: "))
    if (number < 0):
        print ("Number has to be higher than 0.")
        break;
    if (number % 3 == 0):
        score += number
        print(score)
    else:
        continue
print (score)