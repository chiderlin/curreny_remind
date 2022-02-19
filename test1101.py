from modules.database import Database  

Database.initialize()
Database.insert(collection="test", data={"name": "kevin", "age": "20"})
Database.insert(collection="test", data={"name": "Chi", "age": "20"})
print(Database.find_one(collection="test", query={"name": "kevin"}))
print(Database.find(collection="test", query={"age": "20"}))
print(Database.find_all(collection="test"))
