class user:
    def __init__(self,seats,fuel):
        print("new user being created...")
        self.seat = seats
        self.fuel = fuel

    def race_mode(self):
        self.seat = 2
        return



user1 = user(3,"petrol")
#user1.user_name = 'loki'

print(user1.seat)
print(user1.race_mode())