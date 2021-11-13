import pymongo
from pymongo import MongoClient
class model:
    def __init__(self):
        # self.client = pymongo.MongoClient(host='localhost', port=27017)
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client.admin
        self.collection = self.db.modige
    def hello(self):
        # 选择数据库
        db = self.client.admin
        '''
        或
        db = client['test']
        '''
        print(db)
        # 选择集合
        collection = db.modige
        # 插入数据
        student = {
            'id': '20170101',
            'name': 'Jordan',
            'age': 20,
            'gender': 'male'
        }
        # 插入单条数据
        result = collection.insert_one(student)
        student1 = {
            'id': '20170101',
            'name': 'Jordan',
            'age': 20,
            'gender': 'male'
        }
        student2 = {
            'id': '20170202',
            'name': 'Mike',
            'age': 21,
            'gender': 'male'
        }
        # 插入多条数据
        results = collection.insert_many([student1,student2])

        print(result)
    def query(self):
        # 单个查找
        ans = self.collection.find_one({'name': 'Jordan'})
        print(ans)
        # 查找所有
        ans_all = self.collection.find({'name': 'Jordan'})
        for a in ans_all:
            print(a)
        # 条件查询 年龄大于20
        results = self.collection.find({'age': {'$gt': 20}})

        # 正则匹配 以M开头的名字
        results = self.collection.find({'name': {'$regex': '^M.*'}})
        for r in results:
            print(r)

if __name__ == '__main__':
    m = model()
    m.query()
