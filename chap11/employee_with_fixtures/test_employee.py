from Employee import Employee
import pytest

@pytest.fixture

#note that the function name has to be the same as what you are parsing into the test functions
def emp():
   emp = Employee('Marvin', 'Tan', 36_000)
   return emp
 
def test_give_default_raise(emp):
    emp.give_raise()
    assert emp.annual_salary == 41_000

def test_give_custom_raise(emp):
    emp.give_raise(4000)
    assert emp.annual_salary == 40_000