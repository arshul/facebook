from tdg_fb_group import db
from tdg_fb_group.models.base import Base

class Groups(Base):
    id = db.Column(db.Integer, primary_key=True)
    group_id = db.Column(db.String(20))
    group_name = db.Column(db.String(100))
    privacy = db.Column(db.String(10))

    def __init__(self, group):
        self.group_id = group['id']
        self.group_name = group['name']
        self.privacy = group['privacy']

    def __repr__(self):
        return '<%s%s%s>' %(self.group_id,self.group_name,self.privacy)