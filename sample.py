import pandas as pd 

df=pd.read_csv("C:/Users/yuvarani/Downloads/archive/zomato.csv")

print(df)



class Restaurant:
    def __init__(self, name, food_url, age, rate, address):
        self.name = name
        self.food_url = food_url
        self.age = age
        self.rate = rate
        self.address = address

    def get_food_url(self):
        return self.food_url

    def get_age(self):
        return self.age

    def get_rate(self):
        return self.rate

    def get_address(self):
        return self.address

restaurant1 = Restaurant("ABC Restaurant", "https://www.zomato.com/abc", 5, 4.2, "123 Main St")

# Get restaurant details
print("Restaurant Name:", restaurant1.name)
print("Food URL:", restaurant1.get_food_url())
print("Age:", restaurant1.get_age())
print("Rate:", restaurant1.get_rate())
print("Address:", restaurant1.get_address())
