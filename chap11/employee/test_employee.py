from Employee import Employee

def test_give_default_raise():
    emp = Employee('Marvin', 'Tan', 36_000)
    emp.give_raise()
    assert emp.annual_salary == 41_000

def test_give_custom_raise():
    emp = Employee('Marvin', 'Tan', 36_000)
    emp.give_raise(4000)
    assert emp.annual_salary == 40_000