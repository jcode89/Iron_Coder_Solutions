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
    list_one = grab_participants('secret_santa_participants.txt')
    list_two = grab_participants('secret_santa_participants.txt')

    the_answer = []
    shuffle(list_one)
    shuffle(list_two)
    for num in range(len(list_one)):
        try:
            if (list_one[num] != list_two[num]) and ((list_one[num] or list_two[num]) not in the_answer):
                # Makes a list of tuples.
                the_answer.append((list_one[num], list_two[num]))
        except IndexError:
            pass
    if len(list_one) == len(the_answer):
        for names in the_answer:
            print("%s is paired with %s." % names)
    elif (len(list_one) != len(the_answer)):
        match_maker()

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
