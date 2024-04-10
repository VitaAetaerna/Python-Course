from cryptography.fernet import Fernet
# 16 . Implementiere die Ubungen der DesignPatterns des Python-Codelabs: Adapter, ay, Factory
# Iterator, Mediator, Observer, Prototype, Proxy, Singleton, Strategy, Template.

# ADAPTER
class Adapter():
    key = Fernet.generate_key()
    fernet = Fernet(key)
    def Encode(self, text, fernet=fernet, key=key):
        print("The encoding text is: ", text)
        token = fernet.encrypt(b"meow")
        return token
        
    def Decode(self, token,  fernet=fernet, key=key):
        print("Token is: ", token)
        encodedText = fernet.decrypt(token)
        return encodedText 
    

adaption = Adapter()
decoded = adaption.Encode("meow")
print(adaption.Decode(decoded))
