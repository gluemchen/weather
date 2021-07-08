days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
weather = ['Sunny', 'Cloudy', 'Windy', 'Rainy', ]
workdays = days[0:5]
weekend = days[5:7]
spring = months[2:5]
summer = months[5:8]
autumn = months[8:11]
winter = [months[11], months[0], months[1]]
seasons = [spring, summer, autumn, winter]
print(days)
print(workdays, weekend, sep=' | ')
print(months)
print(seasons)
