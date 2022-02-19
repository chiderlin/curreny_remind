import pymongo


class Database(object):
    URI = ['localhost:27017']
    DATABASE = None

    @staticmethod
    def initialize():  # 初始:先連線，建立database
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['currency']

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)  # 加條件搜尋全部

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)

    @staticmethod
    def find_all(collection):
        return Database.DATABASE[collection].find()  # 不加條件搜尋全部

    @staticmethod
    def update(collection, query, data):
        Database.DATABASE[collection].update(query, data)

    @staticmethod
    def remove(collection, query):
        Database.DATABASE[collection].remove(query)


'''connect'''
# client = pymongo.MongoClient(['localhost:27017'])

'''make new database'''
# DATABASE = client['class']


'''insert_one, insert_all'''
# DATABASE['students'].insert_one({"name":"kevin","age":"16"})
# DATABASE['students'].insert_one({"name":"leo","age":"18"})
# print("successed")


'''find_one, find_all'''
# print(DATABASE['students'].find_one({"name":"leo"}))


'''delete_one, delete_all'''
# DATABASE['students'].delete_one({"name":"leo"})
# print("ok")
