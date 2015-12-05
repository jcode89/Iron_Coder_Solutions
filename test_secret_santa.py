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

def people_list():
    """ Returns a list of strings for testing """
    return ['Robert Downy', 'Alfred Hitchcock', 'Sally Ride', 'John Glenn', 'test']

def test_pop_other_returns_item_from_list():
    # creates an unaltered copy of the list
    people = people_list()
    people_copy = list(people)

    result = secret_santa.pop_other(people, 'foo')
    assert result in people_copy

def test_pop_other_removes_item_from_list():
    # creates an unaltered copy of the list
    people = people_list()
    people_copy = list(people)

    result = secret_santa.pop_other(people, 'foo')
    assert result not in people

def test_pop_other_does_not_remove_the_prohibited_item():
    for times in range(100):
        people = people_list()
        result = secret_santa.pop_other(people, 'test')
        assert 'test' != result

def test_pop_other_raises_value_error_if_not_me_is_the_only_value():
    try:
        result = secret_santa.pop_other(['test'], 'test')
    except ValueError as e:
        assert e.args[0] == "Prohibited value is the only remaining value"
    else:
        assert False, "Expected Value Error"
