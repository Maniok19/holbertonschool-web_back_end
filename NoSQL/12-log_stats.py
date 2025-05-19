#!/usr/bin/env python3
"""wababa baba baba baba baba"""
from pymongo import MongoClient


def task_12():
    """wababa baba baba baba baba"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    collec = client.logs.nginx

    nb_logs = collec.count_documents({})
    get = collec.count_documents({"method": "GET"})
    post = collec.count_documents({"method": "POST"})
    put = collec.count_documents({"method": "PUT"})
    patch = collec.count_documents({"method": "PATCH"})
    delete = collec.count_documents({"method": "DELETE"})
    status = collec.count_documents({"method": "GET", "path": "/status"})

    print(f'{nb_logs} logs')
    print('Methods:')
    print(f'\tmethod POST: {post}'.expandtabs(4))
    print(f'\tmethod PUT: {put}'.expandtabs(4))
    print(f'\tmethod PATCH: {patch}'.expandtabs(4))
    print(f'\tmethod GET: {get}'.expandtabs(4))
    print(f'\tmethod DELETE: {delete}'.expandtabs(4))
    print(f'{status} status check')
    client.close()


if __name__ == "__main__":
    task_12()
