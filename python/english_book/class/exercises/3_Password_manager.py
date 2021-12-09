class Password_manager:
    def __init__(self, old_passwords = []):
        self.old_passwords = old_passwords

    def get_password(self):
        return self.old_passwords[-1]

    def set_password(self, password):

        if password not in self.old_passwords:
            self.old_passwords.append(password)

    def is_correct(self, test_password):
        if self.old_passwords[-1] == test_password:
            return True
        else:
            return False

x = Password_manager(['1', '2'])

x.set_password('3')
print(x.get_password())
print(x.is_correct('5'))