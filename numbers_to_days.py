"""
This project intends to return the day by the input of the number
"""

days_dict = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday"
}

day = int(input("Type in the day: "))
print(days_dict[day % 7])
