# number = 15
# word = "Labas"
# print(type(number))

# sarasas = [4,9,8]

# if type(word) is int:
#     print("Tai yra skaicius")

# if type(sarasas) is list:
#     print("tai yra sarasas")

# # dict -> dictionary (zodynas)
# # tuple 

# mix_list = [4,9,"Labas",7,8.5,True,[4,5,2],"Jonas"]

# for element in mix_list:
#     print(element)

# Sukurkite miksuota sarasa kazka panasaus i mano sukurta mix_list turi b8ti bent 4 tipu elementai vienas is ju int arba float
# extra credit jeigu turesite ir float ir int bent kaip viena is tipu
# TIkslas surasti visu sarase esanciu skaiciu suma. Netureti saraso sarase, bet jeigu greitai viska padarote, galite turti ir ji itraukti


# import datetime

# dabar = datetime.date.today() # sakome kreipiames i biblioteka biblioteka. tada kreipiames i vidu jos siuo atveju i date biblioteka.date
# dabar_su_laiku = datetime.datetime.today()
# print(dabar)
# print(dabar_su_laiku)

# # print(dabar_su_laiku.strftime("%Y,%m %A")) # strftime -> String From Time 

# postumis = datetime.timedelta(hours=31,weeks=87,days=698975)
# pastumta_data = dabar_su_laiku - postumis
# print(pastumta_data)

# import datetime as dt # galima uzdeti bibliotekom slapyvardzius
# data = input("Please enter the date of your birth (example 2024-11-25) ")
# reali_data = dt.datetime.strptime(data,"%Y-%m-%d") # konvertavimas iš stringo į datetime
# print(reali_data)

# import datetime

# skirtumas = datetime.datetime.today() - datetime.datetime(1999,9,9)
# # datetime.timedelta()
# # print(skirtumas.)


# from dateutil.relativedelta import relativedelta
# import datetime
# # from datetime import date

# # date.today()
# start_date = datetime.datetime(2000, 1, 1, 0, 0, 0)
# end_date = datetime.datetime(2024, 11, 22, 12, 30, 45)

# difference = relativedelta(end_date, start_date)
# print(difference)

# total_months = difference.years * 12 + difference.months

# total_seconds = (end_date - start_date).total_seconds()
# total_days = total_seconds // (24 * 3600)
# total_hours = total_seconds // 3600
# total_minutes = total_seconds // 60

# result = {
#     "years": difference.years,
#     "months": difference.months,
#     "days": difference.days,
#     "total_months": total_months,
#     "total_days": total_days,
#     "total_hours": total_hours,
#     "total_minutes": total_minutes,
#     "total_seconds": total_seconds,
# }

# print(result)


# # ivesta = datetime(2000, 1, 1, 0, 0, 0)

# ivesta_data = datetime.datetime(2000, 1, 1, 0, 0, 0)
# now = datetime.datetime(2024, 11, 22, 12, 30, 45)
# skirtumas = now - ivesta_data

# print("Praėjo metų: ", skirtumas.days // 365)
# print("Praėjo mėnesių: ", round(skirtumas.days / 365 * 12))
# print("Praėjo savaičių: ", skirtumas.days // 7)
# print("Praėjo dienų: ", skirtumas.days)
# print("Praėjo valandų: ", round(skirtumas.total_seconds() / 3600))
# print("Praėjo minučių: ", round(skirtumas.total_seconds() / 60))
# print("Praėjo sekundžių: ", round(skirtumas.total_seconds()))
