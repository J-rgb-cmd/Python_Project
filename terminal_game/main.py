default_matrix = [[1,2,3],[4,5,6],[7,8,9]]

def print_screen(matrix):
    for row in matrix:
        for index in row:
            print(index, end='    ')
        print('\n')

user1 = ''
user2 = ''

try_again = ''

def user_selection():
    bool_continue = False
    while (bool_continue == False):

        choice = input("Select Shape: x or o\n")
        if choice == 'x':
            user1 = 'x'
            user2 = 'o'
            bool_continue = True
        elif choice == 'o':
            user1 = 'o'
            user2 = 'x'
            bool_continue = True
        else:
            print('Invalid Input, Try Again')

print_screen(default_matrix)


def win_check():

user_input = 

user_selection()

