def validating_credit_card(number):
    # your code goes here
    if number[0] != '4' and number[0] != '5' and number[0] != '6':
        return False
    if len(number) == 16:
        # check if 4 consecutive digits are the same
        for i in range(0, len(number) - 3):
            if number[i] == number[i + 1] == number[i + 2] == number[i + 3]:
                return False
        
        # check if all digits are numbers
        for i in range(0, len(number)):
            if not number[i].isdigit():
                return False
    if len(number) == 19:
        # check if there are dashes in the right places
        if number[4] != '-' or number[9] != '-' or number[14] != '-':
            return False

        # replace dashes with empty string
        number = number.replace('-', '')

        # check if 4 consecutive digits are the same
        for i in range(0, len(number) - 3):
            if number[i] == number[i + 1] == number[i + 2] == number[i + 3]:
                return False
        
        # check if all digits are numbers
        for i in range(0, len(number)):
            if not number[i].isdigit():
                return False
    
    if len(number) != 16 and len(number) != 19:
        return False

    return True

if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        number = input()
        ans = validating_credit_card(number)
        if ans:
            print('Valid')
        else:
            print('Invalid')
