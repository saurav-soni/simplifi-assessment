# assessment 1

def inr_conversion(number):
    '''
    :param number: number(digit)
    :return: INR Notation

    1. Take the number into string
    2. separate front and last 3 elements
    3. Reversed to loop through and add commas from last of front string
    4. Loop through front, take 2 elements and append it to result container
    5. if last single digit left append it too
    6. join back with ',' to get INR notation
    '''

    number = str(number)  # typecasting to string
    return_list = []      # return container

    # taking out last 3 digit as per our INR
    front, last = number[:-3], number[-3:]    # 1234567 => '12345', '678'
    return_list.append(last)

    # reversed the digit for easiness of adding commas
    rev_front = front[::-1]  # '4321'
    j = 0
    for i in range(1, len(rev_front)+1):
        # if 2nd digit, we add it to return_list in reversed order
        if i % 2 == 0:
            return_list.append(rev_front[j:i][::-1])  # return_list = ['678', '45', '23']
            j = i

        # if the len is odd and its last digit we add it as normal
        elif i == len(rev_front):
            return_list.append(rev_front[-1])       # return_list = ['678', '45', '23', '1']

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

    1. first we take list of player's heights and the person height supposed to be found
    2. removed duplicates as 1 bullet is enough and sorted height wise
    3. arranged reversely to get output easily
    4. setting highest index as flag so that if person height is lowest he will get shot atlast
     ie after the length of array.
    5. if player height is higher than all the rest players he will get shot first
    6. else we will find closest player for that person
    '''

    person = int(person)  # player with height '2' to be found
    players = [int(i) for i in players]  # [ 9, 3, 8, 8, 4]

    players = list(set(players))  # [9,3,8,4]
    players = sorted(players)  # [3, 4, 8, 9]
    players = players[::-1]  # [9, 8, 4, 3]

    index = len(players)    # 4, he will get shot after 4 guys

    if person >= max(players):
        index = 0  # if player height is higher than 9, he would get killed first
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
