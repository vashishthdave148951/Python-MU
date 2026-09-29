class Encryption:
    def encrypt(self):
        print('user is encrypted')


class Authorization:
    def verify_user(self):
        print('user is authorized')


class SecureSystem(Encryption,Authorization):
    def secure_data(self):
        print('Secure data')

# Demonstration
s = SecureSystem()
s.verify_user()
s.encrypt()  
s.secure_data()   
 