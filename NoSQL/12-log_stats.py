#!/usr/bin/env python3
"""wababa baba baba baba baba"""
from pymongo import MongoClient


def task_12():
    """wababa baba baba baba baba"""
    client = MongoClient()
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
    print(f'    method POST: {post}')
    print(f'    method PUT: {put}')
    print(f'    method PATCH: {patch}')
    print(f'    method GET: {get}')
    print(f'    method DELETE: {delete}')
    print(f'{status} status check')
    client.close()


if __name__ == "__main__":
    task_12()
