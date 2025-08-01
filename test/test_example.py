import pytest

def test_equal_or_not():
    assert 3 == 3
    assert 3 != 1

def test_is_instance():
    assert isinstance('i am a string', str)
    assert not isinstance('10', int)

def test_boolean():
    validated= True
    assert validated is True
    assert ('hello' == 'world') is False

def test_type():
    assert type('str' is str)
    assert type('str' is not int)

def test_greater_and_lesser():
    assert 7>4
    assert 4<10

def test_list():
    num_list=[1, 2, 3, 4, 5]
    any_list= [False, False]
    assert 1 in num_list
    assert 7 not in num_list
    assert not all(any_list)
    assert not any(any_list)        

class Student:
    def __init__(self, first_name: str, last_name: str, major: str, years: int):
        self.first_name= first_name
        self.last_name= last_name
        self.major= major
        self.years= years

@pytest.fixture
def default_student():
    return Student('Vel', 'Sankar', 'Computer Science', 4)

def test_person_initialisation(default_student):
    assert default_student.first_name == 'Vel'
    assert default_student.last_name == 'Sankar'
    assert default_student.major == 'Computer Science'
    assert default_student.years == 4