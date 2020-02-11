# three_charts.py

#
# CHART 1 (PIE)
#

import matplotlib.pyplot as plt

pie_data = [
    {"company": "Company X", "market_share": 0.55},
    {"company": "Company Y", "market_share": 0.30},
    {"company": "Company Z", "market_share": 0.15}
]

print("----------------")
print("GENERATING PIE CHART...")
print(pie_data) # TODO: create a pie chart based on the pie_data

# list comprehension
labels = [d["company"] for d in pie_data]
sizes = [d["market_share"] for d in pie_data]

#for x in pie_data:
#    labels.append(x["company"])
#    sizes.append(x["market_share"])

colors = ['gold', 'lightcoral', 'lightskyblue']
explode = (0.1, 0, 0)

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, colors=colors, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis("equal")

plt.show()

#
# CHART 2 (LINE)
#

line_data = [
    {"date": "2019-01-01", "stock_price_usd": 100.00},
    {"date": "2019-01-02", "stock_price_usd": 101.01},
    {"date": "2019-01-03", "stock_price_usd": 120.20},
    {"date": "2019-01-04", "stock_price_usd": 107.07},
    {"date": "2019-01-05", "stock_price_usd": 142.42},
    {"date": "2019-01-06", "stock_price_usd": 135.35},
    {"date": "2019-01-07", "stock_price_usd": 160.60},
    {"date": "2019-01-08", "stock_price_usd": 162.62},
]

print("----------------")
print("GENERATING LINE GRAPH...")
print(line_data) # TODO: create a line graph based on the line_data

dates = [d["date"] for d in line_data]
stock_price = [d["stock_price_usd"] for d in line_data]

#for x in line_data:
#    dates.append(x["date"])
#    stock_price.append(x["stock_price_usd"])

plt.plot(dates, stock_price)

plt.xlabel("Date")
plt.ylabel("Stock Price USD")
plt.title("Line Chart")
plt.show()

#
# CHART 3 (HORIZONTAL BAR)
#

bar_data = [
    {"genre": "Thriller", "viewers": 123456},
    {"genre": "Mystery", "viewers": 234567},
    {"genre": "Sci-Fi", "viewers": 987654},
    {"genre": "Fantasy", "viewers": 876543},
    {"genre": "Documentary", "viewers": 283105},
    {"genre": "Action", "viewers": 544099},
    {"genre": "Romantic Comedy", "viewers": 121212}
]

print("----------------")
print("GENERATING BAR CHART...")
print(bar_data) # TODO: create a horizontal bar chart based on the bar_data

