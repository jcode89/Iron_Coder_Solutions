import pytest
import secret_santa

def test_level_two():
    names = secret_santa.match_maker()
    if names != None:
        for the_name in names:
            assert(the_name[0] != the_name[1])
def test_level_three():
    fams = secret_santa.house_match_maker()
    if fams != None:
        for peeps in fams:
            assert(peeps[0] != peeps[1])
