
import matplotlib.pyplot as plt

# Market share of different smartphone operating systems in 2020
os_names = ['Android', 'iOS', 'Others']
market_share = [74.6, 24.8, 0.6]

plt.figure(figsize=(10, 6))
plt.pie(market_share, labels=os_names, autopct='%1.1f%%', colors=['green', 'blue', 'grey'], startangle=90, wedgeprops={'edgecolor': 'black'})
plt.title('Market Share of Smartphone Operating Systems (2020)')
plt.legend()
plt.show()

# Created by Dr Aamir Adeeb
# Contact for more info at aamir@uum.edu.my