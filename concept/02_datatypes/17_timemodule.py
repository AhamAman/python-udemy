import arrow

brewing_time = arrow.utcnow()


Indian_time = brewing_time.to("Asia/Kolkata")
print(f"UTC Time:  {brewing_time}")

print(f"Current Indian Time: {Indian_time.format('YYYY-MM-DD HH:mm:ss ZZ')}")

from collections import namedtuple
chaiProfile = namedtuple("chaiProfile", ["flavor", "aroma"])

# 1. Instantiate the namedtuple
morning_chai = chaiProfile(flavor="Spicy & Bold", aroma="Cinnamon-forward")

# 2. Access the data
print(morning_chai)


print(f"Flavor profile: {morning_chai.flavor}")
