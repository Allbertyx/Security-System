from cryptography.fernet import Fernet

class cifrar():
    # we will be encrypting the below string.
    def __init__(self, mail):

        self.mensage = mail

        key = Fernet.generate_key()

        fernet = Fernet(key)


        self.encMessage = fernet.encrypt(self.mensage.encode())

        #print("original string: ", mensage)
        #print("encrypted string: ", encMessage)

        decMessage = fernet.decrypt(self.encMessage).decode()

        print("el mail se ha encryptado")
        print(self.encMessage)
        #print("decrypted string: ", decMessage)
        #print(key)
