height=float(input("Enter the height from which the ball is dropped: "))
index= float(input("Enter the bounciness index of the ball: "))
bounces=int(input("eEnter the number of times the ball bounced: "))
total_distance = 0
for eachBounce in range(bounces):
    newHeight = height * index
    bounceDistance = newHeight + height
    total_distance += bounceDistance
    height = newHeight
print("Total distance traveled is %.3f" % total_distance)
