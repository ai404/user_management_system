from app import db


class AccountStatus(db.Model):
    __tablename__ = 'account_status'
    __table_args__ = {'sqlite_autoincrement': True}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    status_name = db.Column(db.String(100), nullable=False)
    status_description = db.Column(db.Text)
    users = db.relationship("User",backref="users",passive_deletes=True)
