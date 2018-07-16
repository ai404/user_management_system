from app import db


class SubscriptionPlan(db.Model):
    __tablename__ = 'subscription_plans'
    __table_args__ = {'sqlite_autoincrement': True}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    subscription_plan_name = db.Column(db.String(200), nullable=False)
    subscription_plan_description = db.Column(db.Text)
    users = db.relationship("User",back_populates="subscription",passive_deletes=True)
