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

def pop_other(participants, not_me):
    """
    Pops a name from participants that is not not_me

    Raises ValueError if only choice is the prohibited value
    """
    if len(participants) == 1 and participants[0] == not_me:
        raise ValueError("Prohibited value is the only remaining value")

    clean_participants = [person for person in participants if person != not_me]
    selected = clean_participants[0]

    participants.remove(selected)
    return selected


# Solves Level Two
def match_maker():
    list_one = grab_participants('secret_santa_participants.txt')
    list_two = list(list_one)

    the_answer = []
    list_one
    shuffle(list_two)

    for index, name in enumerate(list_one):
        try:
            receiver = pop_other(list_two, name)
        except ValueError:
            # There is a rare case when the only value left is the prohibited value.
            # In this case, try again
            return match_maker()

        the_answer.append((name, receiver))

    for names in the_answer:
        print("%s gets a gift for %s." % names)
    return the_answer

# Solves Level Three
def house_match_maker():
    families_one = []
    families_two = []
    response = []
    with open('secret_santa_participants.txt', 'r') as ssf:
        # Creates two lists of tuples (firstname, lastname)
        for names in ssf:
            (key, value) = names.split()
            families_one.append((key, value))
            families_two.append((key, value))
    shuffle(families_one)
    shuffle(families_two)
    # Some recursion to ensure that our list has the correct number of people
    # and that the last names do not match.
    for index in range(len(families_one)):
        try:
            if ((families_one[index][1] != families_two[index][1]) and
                ((families_one[index] or families_two[index]) not in response)):
                response.append((families_one[index], families_two[index]))
        except IndexError:
            pass
    if len(response) == len(families_one):
        for names in response:
            print("%s gets a gift for %s" % names)
        return response
    elif len(response) != len(families_one):
        house_match_maker()

if __name__ == '__main__':
    print("Level One Solution:")
    your_match_maker('George Thomas')
    print("\nLevel Two Solution:")
    match_maker()
    print("\nLevel Three Solution:")
    house_match_maker()
