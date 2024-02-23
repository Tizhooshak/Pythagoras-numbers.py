def Choosable():
    # here, we make a loop, so it will ask question from us until we wish to stop
    while True:
        place = int(input("What is the placement of the Stack you want?  "))
        # after getting the placement of the stack, we explain the algorythm of the combination of Pythagoras numbers
        p2 = place * place

        n1 = 2 * place
        n2 = p2 - 1
        n3 = p2 + 1

        # be careful that you cant use those equations with the numbers 1 and 0, because the Pythagoras relation
        #                                                                        won't be applying to the answer
        if place == 1:
            print("There is no algorythm for Pythagoras numbers with 1 ")
            cont = input("do you want to try again? (y/n) ")
            # we will check if the user wants to continue with the questions or not
            # if the user did not want to continue, the loop will break
            if cont == 'y':
                continue
            elif cont == 'n':
                break
        elif place == 0:
            print('There is no algorythm for Pythagoras numbers with 0')
            cont = input("do you want to try again? (y/n) ")
            if cont == 'y':
                continue
            elif cont == 'n':
                break
        else:
            # if the input was ok, the answer will be printed
            print(f'The first number: {n1} | The second number: {n2} | The third number: {n3} ')

            cont = input("do you want to have another chain? (y/n) ")
            if cont == 'y':
                continue
            elif cont == 'n':
                print('\n\t\t\t |   --->            - Made by Tizhooshak   <---|            |')
                break


def Chain():
    goal = int(input("How many chains of Pythagoras numbers do you want? "))
    # the reason that we use 2 except of other numbers, is that there is no algorythm for Pythagoras numbers with 1
    # and 0 as we mentioned earlier, and also, we cant less than 1 amount of stacks
    if goal >= 2:
        for i in range(2, goal + 1):
            p2 = i * i
            n1 = 2 * i
            n2 = p2 - 1
            n3 = p2 + 1
            print(f'{i} = The first number: {n1} | The second number: {n2} | The third number: {n3}')
        print('\n\t\t\t |   --->            - Made by Tizhooshak   <---|            |')
    else:
        print("The least amount you can choose is 2 ")


# in this def, the user will get to choose
def Chain2():

    start = int(input("What is the starting number? "))
    amount = int(input("How many of Stacks do you want? "))

    for i in range(start, start + amount):
        p2 = i * i
        n1 = 2 * i
        n2 = p2 - 1
        n3 = p2 + 1

        print(f'{i} = The first number: {n1} | The second number: {n2} | The third number: {n3} \n')
    print(f'\nTotal amount of printed stacks: {amount}')
    print('\n\t\t\t |   --->            - Made by Tizhooshak   <---|            |')


# now, the user is asked whether if they want a certain stack, or the amount they want
print("1 = have a certain stack of Pythagoras numbers \n"
      "2 = have multiple stacks of Pythagoras numbers starting from 1 \n"
      "3 = have multiple stacks of Pythagoras numbers starting from where you want and how much you want \n")


defi = input("Which output do you want? (1/2/3) ")

if defi == '1':
    Choosable()

elif defi == '2':
    Chain()

elif defi == '3':
    Chain2()

else:
    print('Error- you can only choose between "1" , "2" and "3" ')
