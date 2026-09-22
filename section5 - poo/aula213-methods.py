'''
method vs @classmethod vs @staticmethod.

    method -> self, metodo de instancia
    @classmethod -> cls, metodo de classe
    @staticmethod -> metodo estatico 

'''

class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        self.user = user

    def set_password(self, password):
        self.password = password

    @classmethod
    def set_user_password(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password

        return connection


c1 = Connection()
c1.set_user('Samuel')
c1.set_password(434242)

print(c1.host)
print(c1.user)
print(c1.password)