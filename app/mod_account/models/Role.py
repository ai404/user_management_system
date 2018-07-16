from app import db
from flask_security import RoleMixin


class Role(db.Model,RoleMixin):
    __tablename__ = 'roles'
    __table_args__ = {'sqlite_autoincrement': True}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    role_name = db.Column(db.String(100), nullable=False)
    role_description = db.Column(db.Text)
    users = db.relationship("User",back_populates="role",passive_deletes=True)

    def __init__(self,role_name, role_description):
        self.role_name = role_name
        self.role_description = role_description
