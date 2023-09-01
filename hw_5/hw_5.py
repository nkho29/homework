dict_ = {
    "month1": "October",
    "month2": "September",
    "month3": "December",
    "month4": "February",
    "month5": "June",

}

print(dict_)

dict_["month6"] = "July"
print(dict_)

print(dict_.values())
print(dict_.keys())
print(dict_.items())

del dict_["month2"]
print(dict_)

drivers = dict(drvr1="LH44", drvr2="FA14", drvr3="LN4")
print(drivers)

drivers.update(dict_)
print(drivers)