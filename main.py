# import custom package " I have created custom package which contains reusable code to look clean and well-structured "
from game import matrixtraverse

# initialize parameters
n = int(input("Enter matrix size: "))
m = [[0 for j in range(n)] for i in range(n)]

#indicates the power slider position when brick name is B
extended_slider = 0

# enter no. of balls
no_of_balls = int(input("Enter number of balls: "))

# initialize model
model = matrixtraverse.gamemodels_initialization(matrix=m, total_size=n, extended_slider=extended_slider, score=no_of_balls)

# create matrix of n*n
model.create_matrix(n)

# enter inputs
while True:
    a, b, c = input("Enter values a,b,c: ").split()

    # convert digit-string to integers, neglect case characters
    model.input_matrix(int(a), int(b), model.check_alpha(c))
    _ = input("Do you want to continue y or n: ")
    if _ == "n" or _ == "N":
        break

# print values
for i in model.getvalues():
    print(*i)

# main model run..
while True:

    # check for game finished
    if model.check_scoreboard():
        print("win hurray!....")
        break
    elif no_of_balls == 0:
        print("your out!")
        break

    # take user input
    stri = input("enter directions for the ball: s (straight), r (right), l (left) or n to stop: ")
    if stri == "n":
        break

    # get current position of ball
    i, j = model.current_pos()
    if stri == "s":
        no_of_balls = model.straight_ball(i - 1, j)
        for i in model.getvalues():
            print(*i)
        print("no_of_balls: " + str(no_of_balls))
    elif stri == "r":
        no_of_balls = model.right_diagnol(i - 1, j + 1, 1)
        for i in model.getvalues():
            print(*i)
        print("no_of_balls: " + str(no_of_balls))
    elif stri == "l":
        no_of_balls = model.left_diagnol(i - 1, j - 1, -1)
        for i in model.getvalues():
            print(*i)
        print("no_of_balls: " + str(no_of_balls))
    else:
        continue

# print values
for i in model.getvalues():
    print(*i)
