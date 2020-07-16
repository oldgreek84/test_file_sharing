from app import db
from datetime import datetime

class UploadedFile(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(300))
    link = db.Column(db.String(300))
    created = db.Column(db.DateTime, default=datetime.now())
    life_time = db.Column(db.DateTime)

    def __repr__(self):
        return f'[{self.id} of file]'
