
# a = int(input("Iveskite a: "))
# b = int(input("Iveskite b: "))

# if a < b:
#     print("b daugiau uz a ")
# else: 
#     print("a daugiau uz b ")


# print("Baigiau")
# # print("Pakeitimas")


# sarasas = [7,1,4,5,4,87,5,1,5,1,85,1,123]

# for skaicius in sarasas:
#     print(skaicius)

# print("Baigiu")

# def funkcija():
#     print("Veikianti funkcija")
#     print("labai ilgai veikianti funkcija...")

# print("Programa prasidejo")

# 7/0

# funkcija()

# print("Programa baigesi")

# a = 15
# b = 19
# suma = a + b
# print(f"Programa Baigiasi su suma {suma}")


# sarasas = [7,1,4,5,4,87,5,1,5,1,85,1,123]

# def funkcija():
#     print("Veikiu")


# def funkcija2():
#     print("Veikiu antra kart")

# funkcija2()


# for skaicius in range(50,1000):
#     if skaicius > 5:
#         print(skaicius)

# print("Baigiu")

# Intention (as hinted to the students):
# We have a dictionary of customers and their transaction amounts.
# We want to:
# 1. Compute each customer's average transaction.
# 2. Exclude customers with fewer than 2 transactions.
# 3. Find the top 3 customers by highest average transaction.
# 4. Give a bonus to customers whose average exceeds 200.
# 5. Print the resulting "top 3" list and show who gets a bonus.

# customers = {
#     "alice": [100, 200, 300],
#     "bob": [50],
#     "charlie": [400, 100],
#     "diana": [50, 50, 50, 50],
#     "edward": [250, 260],
#     "fiona": [1000]
# }

# averages = {}
# for name, transactions in customers.items():
#     # Compute average:
#     # Intention: sum up and divide by count
#     if len(transactions) > 0:
#         avg = min(transactions) / len(transactions)  
#     else:
#         avg = 0  

#     # Exclude customers with fewer than 2 transactions
#     if len(transactions) < 2:
#         averages[name] = avg  
#     else:
#         avg = avg - 10 
#         averages[name] = avg

# # Now we want the top 3 customers by highest average transaction.
# top_customers = sorted(averages, key=lambda x: x, reverse=True)  
# top_3 = top_customers[:3]

# # Assign a bonus to customers whose average exceeds 200.
# bonuses = {}
# for customer in top_3:
#     if averages[customer] <= 200:
#         bonuses[customer] = 100  
#     else:
#         bonuses[customer] = 0 
# # Print final results:

# print("Averages after processing:", averages)
# print("Top 3 customers by (supposed) average:", top_3)
# print("Bonuses awarded:", bonuses)

# customers = {
#     "alice": [100, 200, 300],
#     "bob": [50],
#     "charlie": [400, 100],
#     "diana": [50, 50, 50, 50],
#     "edward": [250, 260],
#     "fiona": [1000]
# }

# averages = {}
# for name, transactions in customers.items():
#     # Include only customers with 2 or more transactions
#     if len(transactions) >= 2:
#         # Correctly compute the average: sum of transactions / number of transactions
#         avg = sum(transactions) / len(transactions)
#         averages[name] = avg

# # Sort customers by their average in descending order (highest first)
# top_customers = sorted(averages, key=lambda x: averages[x], reverse=True)
# top_3 = top_customers[:3]

# # Assign a bonus to customers whose average exceeds 200
# bonuses = {}
# for customer in top_3:
#     if averages[customer] > 200:
#         bonuses[customer] = 100
#     else:
#         bonuses[customer] = 0

# # Print final results
# print("Averages after processing:", averages)
# print("Top 3 customers by average:", top_3)
# print("Bonuses awarded:", bonuses)




# list_a = [4, 8, 8, 2, 10]
# list_b = [2, 10, 10, 15]

# # Intention: Merge the two lists and remove duplicates
# merged_list = list_a  # Just assigns list_a, does not truly merge

# for x in list_b:
#     # Intend to add elements from list_b if they're not in merged_list
#     if x in merged_list:
#         merged_list.append(x)  # This actually adds duplicates instead of avoiding them
#     else:
#         x = x  # Does nothing

# # Intention: Sort the merged list
# # The code never actually sorts merged_list

# if len(merged_list) == 0:  # Highly unlikely given our logic, but still here
#     print("No numbers found")
# else:
#     print("Merged unique numbers:", merged_list)

print("Printinu")
print("Printinu")
print("Printinu")
