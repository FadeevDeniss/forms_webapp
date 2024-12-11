import os

from typing import Any

from pymongo import MongoClient


class MongoDbConnection:
    """
    Обертка над MongoClient, устанавливает соединение с БД
    и реализует основные операции.
    """

    def __init__(self):
        self.connection = MongoClient(os.environ.get('MONGODB_URI'))
        self.db = self.connection[os.environ.get('MONGODB_NAME', 'dev')]

    def insert(self, collection, data):
        self.db[collection].insert_one(data)

    def bulk_insert(self, collection, documents):
        self.db[collection].insert_many(documents)

    def find(self, collection, query: dict[str, Any] = None):
        self.db[collection].find(query or {})

    def __repr__(self):
        return f'<MongoDbConnection: {self.db}'
