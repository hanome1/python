my_list = [7, 5, 3, 3, 2]
def rating(user_list):
    user_list.append(int(input('input your num: ')))
    user_list.sort(reverse=1)
    print(user_list)
    return user_list
my_list = rating(my_list)
my_list = rating(my_list)
my_list = rating(my_list)
    