class User:

        def __init__(self, name):
                self.name = name
                self.amount = 0

        def make_deposit(self, amount):
                self.amount += amount

        def make_withdrawal(self, amount):
                self.amount -= amount


        def display_user_balance(self):
                print(f"User: {self.name}, Balance: {self.amount}")


tiffany = User("Tiffany")
kevin = User("Kevin")
kilequa =User("Kilequa")

tiffany.make_deposit(500)
tiffany.make_deposit(500)
tiffany.make_deposit(500)
tiffany.make_withdrawal(250)
tiffany.display_user_balance()


kevin.make_deposit(600)
kevin.make_deposit(300)
kevin.make_withdrawal(200)
kevin.make_withdrawal(150)
kevin.display_user_balance()

kilequa.make_deposit(5000)
kilequa.make_withdrawal(500)
kilequa.make_withdrawal(500)
kilequa.make_withdrawal(500)
kilequa.display_user_balance()
