from MyFunctions import is_capitalized, is_digits
class Person(object):
    def __init__(self, first_name, last_name, national_id):
        self.f_name = first_name
        self.l_name = last_name
        self.national_id = national_id

    #==========PROPERTIES AND SETTERS==========
    @property
    def f_name(self):
        return self._f_name
    @f_name.setter
    def f_name(self, new_name):
        if not is_capitalized(new_name):
            raise ValueError("Invalid input. First name must be capitalized. ")
        self._f_name = new_name

    @property
    def l_name(self):
        return self._l_name
    @l_name.setter
    def l_name(self, new_name):
        if not is_capitalized(new_name):
            raise ValueError("Invalid input. Last name must be capitalized. ")
        self._l_name = new_name

    @property
    def national_id(self):
        return self._national_id
    @national_id.setter
    def national_id(self, new_id):
        if not is_digits(new_id, 11):
            raise ValueError("Invalid input. ID code must be only 11 digits.")
        self._national_id = new_id

    def __str__(self):
        return f"Last name: {self.l_name} | First name: {self.f_name} | National ID: {self.national_id}"