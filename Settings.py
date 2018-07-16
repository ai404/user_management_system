from app import db
from app.mod_account.models.Role import Role
from app.mod_account.models.AccountStatus import AccountStatus
from app.mod_account.models.SubscriptionPlan import SubscriptionPlan


class Settings:
    def populate_db(self):

        if not AccountStatus.query.all():
            self.set_account_status()
        if not SubscriptionPlan.query.all():
            self.set_subscription_plans()
        if not Role.query.all():
            self.set_roles()

    def set_subscription_plans(self):

        # subscription_plans
        subscription_plans = [["Free Plan", "Free plan with limited options. Free for life."],
                              ["Small Enterprise", "Plan for small enterprises. Monthly and Yearly Subscription"],
                              ["Large Enterprise", "Plan for large enterprises. Monthly and Yearly Subscription."]]
        for name, description in subscription_plans:
            a = SubscriptionPlan(subscription_plan_name=name, subscription_plan_description=description)
            db.session.add(a)
            db.session.commit()

    def set_roles(self):

        # Roles
        roles = [["Admin", "Adminstrator for the account."], ["Staff", "Staff for the account."],
                 ["Super Admin", "Super admin user."]]
        for name,decription in roles:
            a = Role(role_name=name, role_description=decription)
            db.session.add(a)
            db.session.commit()

    def set_account_status(self):
        # account_status
        account_status = [["Active", "Active user."], ["Inactive", "Inactive user."], ["Suspended", "Suspended user."]]
        for name,decription in account_status:
            a = AccountStatus(status_name=name, status_description=decription)
            db.session.add(a)
            db.session.commit()


if __name__ == "__main__":
    settings = Settings()
    settings.populate_db()
