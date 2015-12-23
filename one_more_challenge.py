"""
Solves http://www.codenewbie.org/blogs/just-one-more .

Everything was kept in one function and can handle all three levels.
"""
import re

def add_one(some_list):
    new_list = []
    if type(some_list[0]) == int:
        for index in range(len(some_list)):
            some_list[index] = some_list[index] + 1
        return some_list
    if type(some_list[0]) == str:
        if some_list[0] == "1":
            for index in range(len(some_list)):
                # checks for positive and negative numbers.
                items = re.findall('(-?\d+)', some_list[index])
                if items:# Checks to make sure it is not None
                    new_list.append(int(items[0])+1)
            return new_list
        else:
            for item in some_list:
                if re.match('[a-z]{2}[0-9]{3}', item) or re.match('[a-z]{2}[0-9]{2}', item):
                    # Sperate letters and numbers
                    letters = item[0:2]
                    numbers = item[2:]
                    if numbers == "00":
                        numbers = item[-1]
                        # Change numbers to type int to do the math than back
                        # to type str before adding them to new_list.
                        new_list.append(letters + str(0) + str(int(numbers) + 1))
                    # To catch and handle the tricky part of level 3.
                    elif re.match('[0-9]{2}[a-z]{2}[0-9]{2}' ,numbers):
                        first = item[0:2]
                        nums = item[2:4]
                        more_letters = item[4:6]
                        more_nums = item[6:]
                        new_list.append(first + str(int(nums) + 1) + more_letters + str(int(more_nums) + 1))
                    # If no special cases are needed, we can proceed normally.
                    else:
                        new_numbers = str(int(numbers)+1)
                        new_list.append(letters + new_numbers)
                elif re.match('[a-z]{3}[0-9]', item) or re.match('[a-z]{3}[0-9]{2}', item):
                    letters = item[0:3]
                    numbers = int(item[3:])
                    new_numbers = str(numbers + 1)
                    new_list.append(letters + new_numbers)
                elif re.match('[a-z][0-9]{2}[a-z][0-9]{2}', item):
                    first_letter = item[0]
                    first_number = item[1:3]
                    second_letter = item[3]
                    last_number = item[4:]
                    new_list.append(first_letter + str(int(first_number) + 1)
                                    + second_letter + str(int(last_number) + 1))
                elif re.match('[a-z][0-9]', item):
                    letters = item[0]
                    numbers = item[1]
                    new_list.append(letters + str(int(numbers) + 1))
            return new_list


if __name__ == '__main__':
    #add_one(['1', 'c', '0', '-1', '5', 'b', '100', '37', 'a', '20', '18', '12', '0'])
    print(add_one(['ab123', 'gh00', 'ijk8', 'lmn12', 'cd99ef11']))
