from random import shuffle

def grab_participants(name_of_file):
    with open(name_of_file, 'r') as ssf:
        the_people = ssf.read().splitlines()
    return the_people

# Solves Level One
def your_match_maker(your_name):
    our_list = grab_participants('secret_santa_participants.txt')
    shuffle(our_list)
    for people in our_list:
        if your_name != people:
            print("Your partner is %s" % people )
            break

# Solves Level Two
def match_maker():
    our_list = grab_participants('secret_santa_participants.txt')
    list_one = []
    list_two = []
    # Splits up the original list in two seperate lists
    for num in range(len(our_list)):
        if (our_list[num] not in list_one )and (our_list[num] not in list_two):
            try:
                list_one.append(our_list[num])
                list_two.append(our_list[num+1])
            except IndexError:
                list_one.append(our_list[num])
    # Shuffles the lists up
    shuffle(list_one)
    shuffle(list_two)
    for index in range(int(len(our_list)/2)+1):
        try:
            print("%s's secret santa is %s" % (list_one[index], list_two[index]))
        except IndexError:
            print("%s's secret santa is %s" % (list_one[index], list_two[index-1]))

# Solves Level Three
def house_match_maker():
    our_list = grab_participants('secret_santa_participants.txt')
    families = []
    checked_families = []
    # Sorts the families into households
    for first in our_list:
        household = []
        for names in our_list:
            if (first[-4:] == names[-4:]) and (names not in household):
                household.append(names)
        families.append(household)
    for overcrowd in families:
        if overcrowd not in checked_families:
            checked_families.append(overcrowd)
    # Matches non-family with non-family
    # There are seven families, I may be able to use zip(*checked_families)
    # to seperate the nested lists, however, I am not sure.



if __name__ == '__main__':
    print("Level One Solution:")
    your_match_maker('George Thomas')
    print("\nLevel Two Solution:")
    match_maker()
    print("\nLevel Three Solution:")
    house_match_maker()
