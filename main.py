# assessment 1

def inr_conversion(number):
    '''
    :param number: number(digit)
    :return: INR Notation
    '''

    number = str(number)  # typecasting to string
    return_list = []      # return container

    # taking out last 3 digit as per our INR
    last = number[-3:]    # 123456 => '456'
    return_list.append(last)

    # after last 3 digit we need comma for every 2nd digit
    front = number[:-3]   # 123456 => '123'

    # reversed the digit for easiness of adding commas
    rev_front = front[::-1]  # '321'
    j = 0
    for i in range(1, len(rev_front)+1):
        # if 2nd digit, we add it to return_list in reversed order
        if i % 2 == 0:
            return_list.append(rev_front[j:i][::-1])  # return_list = ['456', '23', '1']
            j = i

        # if the len is odd and its last digit we add it as normal
        elif i == len(rev_front):
            return_list.append(rev_front[-1])

    # joined the list back to get desired output
    inr = ','.join(return_list[::-1])
    return inr

number = input('amount: ')
print(inr_conversion(number))


# Assessment 2

def find_person(players: list, person):
    '''

    :param players: test case: list
    :param player: player to be found
    :return: index of the player
    '''

    person = int(person)  # player with height '8' to be found
    players = [int(i) for i in players]  # [ 9, 3, 8, 8, 4]

    # removal of duplication as the line of fire will get all the equal heights in single shot
    players = list(set(players))  # [9,3,8,4]
    players = sorted(players)  # [3, 4, 8, 9]

    # arranged reversely to get output easily
    players = players[::-1]  # [9, 8, 4, 3]

    # setting highest index so that if person height is lowest he will get
    # shot atlast ie after the length of array.
    index = len(players)

    if person >= max(players):
        index = 0  # if player height is higher than all the rest players he will get shot first
    else:
        # else we will fidn closest player for that person
        for i in players:
            if i <= person:
                index = players.index(i)
                break

    people_to_be_shot = index
    return people_to_be_shot


T = int(input('no. of test cases: '))
while T > 0:
    N = input('number, player to be found: ').split()
    test_case = input('players: ').split()
    print(find_person(test_case, N[1]))
    T -= 1
