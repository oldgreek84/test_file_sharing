import datetime
from datetime import timedelta
import os
import time

from app import db, client
from app.models import UploadedFile


@client.task
def clear_old(id):
    ''' func set task that find and delete file and db entry''' 

    file = UploadedFile.query.get(id)
    db.session.delete(file)
    db.session.commit()
    try:
        os.remove(file.link)
        print(f'file and db entry {id} successfully delete')
    except FileNotFoundError:
        print('file not exist')


@client.task
def clear_all():
    ''' func set task check all files and delete they if old '''

    print('task start')
    files = UploadedFile.query.all()
    for file in files:
        clear_one(file.id)
    print('task end')

def clear_one(id):
    ''' func get file by id and check him to date of delete '''

    file = UploadedFile.query.get(id)
    die_time = file.life_time
    now = datetime.datetime.now()
    if now > die_time:
        db.session.delete(file)
        db.session.commit()
        try:
            os.remove(file.link)
            print('file and db entry deleted ')
        except FileNotFoundError:
            print('file not exist')
    else:
        print('time to delete: ', die_time)
        print('this time not now')
