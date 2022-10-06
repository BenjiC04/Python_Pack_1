import datetime as dt
current_year = dt.datetime.now().year
#input age in years
age = int(input("Hello! Tell me your age in years and let me wow you!"))

#days alive
days_alive = age * 365
print("you've been alive for about", days_alive, "days.")
if (days_alive <= 6570):
     print("looks like you're legal...")

#decades alive
decades_alive = age / 10
print("you've been alive for about", decades_alive, "decades.")
if (decades_alive >= 5):
    print("man, you're old as dirt!")

#weeks alive
weeks_alive = age * (365 / 7)
print("you've been alive for about", weeks_alive, "weeks.")

#minutes alive
minutes_alive = age * (365 * 24 * 60)
print("you've been alive for approximately", minutes_alive, "minutes.")