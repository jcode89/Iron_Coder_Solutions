import pytest
import secret_santa

def test_level_two():
    names = secret_santa.match_maker()
    if names != None:
        for the_name in names:
            assert the_name[0] != the_name[1]
    elif names == None:
        test_level_two()

def test_level_three():
    fams = secret_santa.house_match_maker()
    if fams != None:
        for peeps in fams:
            assert peeps[0] != peeps[1]
    elif fams == None:
        test_level_three()

# I wrote these tests as a way to check the logic behind the other two main tests
def test_the_level_two_test():
    some_list = [('Robert Downy', 'Alfred Hitchcock'), ('Sally Ride', 'John Glenn')]
    for people in some_list:
        assert people[0] != people[1]

def test_the_level_three_test():
    the_list = [(('billy', 'bob'), ('silly', 'throb')), (('Sally', 'Ride'),( 'John', 'Glenn'))]
    for people in the_list:
        assert people[0] != people[1]
