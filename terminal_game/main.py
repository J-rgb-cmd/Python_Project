default_matrix = [[1,2,3],[4,5,6],[7,8,9]]

def print_screen(matrix):
    for row in matrix:
        for index in row:
            print(index, end='    ')
        print('\n')

user1_sign = ''
user2_sign = ''

user1_input = ''
user2_input = ''

try_again = ''

def user_selection():
    bool_continue = False
    while (bool_continue == False):

        choice = input("Select Shape: x or o\n")
        if choice == 'x':
            user1_sign = 'x'
            user2_sign = 'o'
            bool_continue = True
        elif choice == 'o':
            user1_sign = 'o'
            user2_sign = 'x'
            bool_continue = True
        else:
            print('Invalid Input, Try Again')


def select_location(input, sign):
    for i in range(len(default_matrix)):
        for j in range(len(default_matrix[i])):
            if int(input) == default_matrix[i][j]:
                default_matrix[i][j] = sign
            
    


                    



user1_input= input('Select grid \n')
select_location(user1_input,'x')
print_screen(default_matrix)

