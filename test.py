# =======================================
# 測試把資料寫入
# from modules.database import Database  

# Database.initialize()
# # Database.insert(collection="test", data={"name": "kevin", "age": "20"})
# # Database.insert(collection="test", data={"name": "Chi", "age": "20"})
# # print("OK")

# print(Database.find_one(collection="test", query={"name": "kevin"}))

# print(Database.find(collection="test", query={"age": "20"})[0]) 
# print(Database.find(collection="test", query={"age": "20"})[1])

# print(Database.find_all(collection="test")[0])
# print(Database.find_all(collection="test")[1])


# ===================================================
# 測試把user密碼加密
# from passlib.hash import pbkdf2_sha512


# password = input("password")
# hash_password = pbkdf2_sha512.hash(password) #加密
# print(hash_password)
# print(pbkdf2_sha512.verify(password, hash_password)) #驗證True or False

#==================================
#測試update email
from modules.database import Database
from modules.user import User

Database.initialize()
User.update_user_email("test@test.com","testtest@test.com")




