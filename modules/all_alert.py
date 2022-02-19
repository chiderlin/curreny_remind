from modules.database import Database


class All_alert(object):
    def __init__(self, email, currency, rate_exchange, price):
        self.email = email
        self.currency = currency
        self.rate_exchange = rate_exchange
        self.price = price

    @staticmethod
    def create_alert(email, currency, rate_exchange, price):
        alert_data = Database.find_one(
            collection="all_alert", query={"email": email, "currency": currency, "rate_exchange": rate_exchange})
        if alert_data:
            return False

        All_alert(email, currency, rate_exchange, price).save_to_db()
        return True

    def save_to_db(self):
        Database.insert(collection="all_alert", data=self.json())

    def json(self):
        return {
            "email": self.email,
            "currency": self.currency,
            "rate_exchange": self.rate_exchange,
            "price": self.price,
        }

    @staticmethod
    def find_user_alert(email, rate_exchange):
        return Database.find(collection='all_alert', query={"email": email, "rate_exchange": rate_exchange})

    @staticmethod
    def update_user_alert(email, currency, rate_exchange, price):
        return Database.update(collection="all_alert", query={"email": email, "currency": currency, "rate_exchange": rate_exchange}, data={"$set": {"price": price}})

    @staticmethod
    def delete_user_alert(email, currency, rate_exchange):
        Database.remove(collection="all_alert", query={
                        "email": email, "currency": currency, "rate_exchange": rate_exchange})
