organisms = int(input("Enter the initial number of organisms:"))
rateOfGrowth = int(input("Enter the rate of growth [a real number > 0]: "))
numOfHours = int(input("Enter the number of hours to achieve the rate of growth:"))
totalHours = int(input("Enter the total hours of growth: "))
while numOfHours <= totalHours:
    organisms *= rateOfGrowth
    numOfHours += numOfHours
print("The total population is ",organisms)
