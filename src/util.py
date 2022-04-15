from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'],deprecated='auto')

# def hash(password:str):
#     return pwd_context.hash(password)

hash_password= lambda password :pwd_context.hash(password)


# def verify(hashed_password,plain_password):
#     return pwd_context.verify(hashed_password,plain_password)

verify_password=lambda hashed_password,plain_password:pwd_context.verify(hashed_password,plain_password)