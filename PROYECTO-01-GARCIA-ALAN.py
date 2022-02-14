from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches
import math

"""
User login section
User: Lifestore
Password: store15
"""

#----------------------------LOGIN---------------------------------#

userAccess = False
attempts = 0

#Welcome message
print("Welcome to the data analysis program!\nPlease log in with your username and password\n")

#loop for log in attempts
while userAccess == False and attempts < 3:
  user = input("Please write your username here: ")
  password = input("Please write your password here: ")
  attempts += 1
  if user == "Lifestore" and password == "store15":
    userAccess = True
  elif attempts == 3:
    print("You have reached the maximum number of attempts. The program will now close.")
    exit()
  elif user != "Lifestore":
    print("This user is not registered in the system. Please try again (attempt " + str(attempts) + "/3)")
  elif password != "store15":
    print("The password is incorrect. Please try again(attempt " + str(attempts) + "/3)")

print("\n\nWelcome, ", user, "\n\n")

#----------------------------MOST SOLD PRODUCTS---------------------------------#

#Generate a list with the product id appearing as many times as it was sold without taking into account the refunds
sales_per_product = [sales[1] for sales in lifestore_sales if sales[4] != 1]

#Generate a list with the product id appearing as many times as it was searched
search_per_product =[search[1] for search in lifestore_searches]

#Generate a list with the product category appearing as many times as the products that belong to it
products_per_category =[producto[3] for producto in lifestore_products]

#Generate a list containing each category once
categories = []
[categories.append(ctgry) for ctgry in products_per_category if ctgry not in categories]

#Sort the categories in alphabetical order
categories.sort()

#Generate a list with 4 values per item: product id, sales per product, searches per product and category
product_sales_searches = [[product[0], sales_per_product.count(product[0]), search_per_product.count(product[0]), product[3]] for product in lifestore_products]

#Defines a function necessary to sort product_sales_searches by sales
def function_sales(e):
  return e[1]

#Defines a function necessary to sort product_sales_searches by searches
def function_searches(e):
  return e[2]

#Sort our list by sales, with the most sold products on the top 
product_sales_searches.sort(reverse = True, key = function_sales)

#Displays the 5 most sold products
print("The most sold products were: ")
for q in range(5):
  print(f"ID number: {product_sales_searches[q][0]} // Name: {lifestore_products[product_sales_searches[q][0] - 1 ][1]} // Sales: {product_sales_searches[q][1]}.")
print("\n\n")

#----------------------------LEAST SOLD PRODUCTS---------------------------------#

#Sort our list by sales, with the least sold products on the top 
product_sales_searches.sort(reverse = False, key = function_sales)  

#Displays the 5 least sold products by category
print("The least sold products by category were: \n")
i = 0
for item in categories:
  print("\n" + categories[i] + ": ")
  i += 1
  q1 = 0
  q2 = 0
  for q in product_sales_searches: 
    if item == product_sales_searches[q1][3] and q2 < 5:
      print(f"ID number: {product_sales_searches[q1][0]} // Name: {lifestore_products[product_sales_searches[q1][0] - 1 ][1]} // Sales: {product_sales_searches[q1][1]}.")
      q2 += 1
    q1 += 1 
print("\n\n")   

#----------------------------MOST SEARCHED PRODUCTS---------------------------------#

#Sort our list by searches, with the most searched products on the top 
product_sales_searches.sort(reverse = True, key = function_searches)

#Displays the 10 most searched products
print("The most searched products were: ")
for q in range(10):
  print(f"ID number: {product_sales_searches[q][0]} // Name: {lifestore_products[product_sales_searches[q][0] - 1 ][1]} // Searches: {product_sales_searches[q][2]}.")
print("\n\n")

#Sort our list by searches, with the least searched products on the top 
product_sales_searches.sort(reverse = False, key = function_searches)

#----------------------------LEAST SEARCHED PRODUCTS---------------------------------#

#Displays the 10 least searched products by category
print("The least searched products by category were: \n")
i = 0
for item in categories:
  print("\n" + categories[i] + ": ")
  i += 1
  q1 = 0
  q2 = 0
  for q in product_sales_searches :    
    if item == product_sales_searches[q1][3] and q2 < 10 :
      print(f"ID number: {product_sales_searches[q1][0]} // Name: {lifestore_products[product_sales_searches[q1][0] - 1 ][1]} // Searches: {product_sales_searches[q1][2]}.")
      q2 += 1
    q1 += 1 
print("\n\n")   

#----------------------------BEST SCORED PRODUCTS---------------------------------#

#Make a list containing product id and score from lifestore_sales
id_reviews_not_separated = [[sale[1], sale[2]] for sale in lifestore_sales]

#Make a dictionary to save the scores as lists for each product
id_reviews_count = {}

#Add values to each element in the dictionary and add score value lists for each element
for par in id_reviews_not_separated:
    id = par[0]
    review = par[1]
    if id not in id_reviews_count.keys():
        id_reviews_count[id] = []
    id_reviews_count[id].append(review)

#Create a list containing only the product ids of the products with a score
id_with_score = []
[id_with_score.append(idprdct) for idprdct in id_reviews_count if idprdct not in id_with_score]

#Create a list to save the average values of each product
averages = []

#Get the average score value of each product and put it into the averages list
for id_product in id_reviews_count.keys():
    lista_reviews = id_reviews_count[id_product]
    promedio = sum(lista_reviews) / len(lista_reviews)
    # Set the decimals to 2
    decimales = 2
    multiplicador = 10 ** decimales
    promedio = math.ceil(promedio * multiplicador) / multiplicador
    averages.append(promedio)
    
#Join the id_with_score list with the averages list
id_avgscore = list(zip(id_with_score,averages))

#Defines a function necessary to sort id_avgscore by the average score
def function_avgscore(e):
  return e[1]

#Sort our list by averege score, with the highest scored products on the top 
id_avgscore.sort(reverse = True, key = function_avgscore)

#Displays the 5 highest rated products
print("The highest rated products were: ")
for q in range(5):
  print(f"ID number: {id_avgscore[q][0]} // Name: {lifestore_products[id_avgscore[q][0] - 1 ][1]} // Average score: {id_avgscore[q][1]}.")
print("\n\n")

#----------------------------WORST SCORED PRODUCTS---------------------------------#

#Sort our list by averege score, with the lowest scored products on the top 
id_avgscore.sort(reverse = False, key = function_avgscore)

#Displays the 5 lowest rated products
print("The lowest rated products were: ")
for q in range(5):
  print(f"ID number: {id_avgscore[q][0]} // Name: {lifestore_products[id_avgscore[q][0] - 1 ][1]} // Average score: {id_avgscore[q][1]}.")
print("\n\n")

#----------------------------TOTAL MONEY BY MONTH---------------------------------#

# Creates a list that contains the sale and the date of each sale
id_date = [ [sale[0], sale[3]] for sale in lifestore_sales if sale[4] == 0 ]

# Creates a dictionary that contains the months and the sales per month
category_months = {}

#Create a list of months that had any sales in them
months_with_sales = []

for par in id_date:
    # Obtains sale and month
    id = par[0]
    _, month, _ = par[1].split('/')
    # Makes each month into a key, if it isn't one already
    if month not in category_months.keys():
        category_months[month] = []
    #Include into months_with_sales every month that had any sales in it (no refunds)
    if month not in months_with_sales:
        months_with_sales.append(month)
    #Appends each sale to the month it belongs to
    category_months[month].append(id)

#Creates a list that contains the sum of money earned each month, without mentioning the month
money_per_month = []

#Creates a list that contains the amount of sales each month
sales_per_month = []

for key in category_months.keys():
    list_month = category_months[key]
    sum_sale = 0
    for id_sale in list_month:
        index = id_sale - 1
        info_sale = lifestore_sales[index]
        id_product = info_sale[1]
        price = lifestore_products[id_product-1][2]
        sum_sale += price
    #Append the sum money earned every month 
    money_per_month.append(sum_sale)
    #Append the number of sales of each month
    sales_per_month.append(len(list_month))

#Join the months_with_sales, money_per_month and sales_per_month lists into a single list
month_money_sale = list(zip(months_with_sales,money_per_month, sales_per_month))

#Defines a function necessary to sort month_money_sale by month
def function_month1(e):
  return e[0]

#Defines a function necessary to sort month_money_sale by ammount of money
def function_money1(e):
  return e[1]

#Defines a function necessary to sort month_money_sale by number of sales
def function_sale1(e):
  return e[2]

#Sort our list by month, with the first on the top 
month_money_sale.sort(reverse = False, key = function_month1)

#Prints the sum of money obtained by each month
m = 0
for months in month_money_sale:
  print(f"The sum of money obtained in the month {month_money_sale[m][0]} was: {month_money_sale[m][1]}")
  m += 1
print("\n\n")

#----------------------------AVERAGE SALES PER MONTH---------------------------------#

#Average number of sales per month
avg_salePerMonth = sum(sales_per_month) / len(sales_per_month)

print(f"The average number of sales per month was: {avg_salePerMonth}\n\n")

#----------------------------TOTAL MONEY THROUGHOUT YEAR---------------------------------#

#Total money obtained throughout the year
total_money = sum(money_per_month)

print(f"The total sum of money throughout the year was: {total_money}\n\n")

#----------------------------MONTHS WITH MOST SALES---------------------------------#

#Sort our list by number of sales, with the biggest ammount of sales on the top
month_money_sale.sort(reverse = True, key = function_sale1)

#Prints the 5 months with the most sales
print("The months with the most ammount of sales were :")
for m in range(5):
  print(f"Month :{month_money_sale[m][0]} // Number of sales: {month_money_sale[m][2]}")
  m
print("\n\n")

#----------------------------MONTHS WITH MOST MONEY GAINED---------------------------------#

#Sort our list by money, with the biggest ammount of money on the top
month_money_sale.sort(reverse = True, key = function_money1)

#Prints the 5 months with the most sales
print("The months with the most ammount of money earned were :")
for m in range(5):
  print(f"Month :{month_money_sale[m][0]} // Ammount of money: {month_money_sale[m][1]}")
  m
print("\n\n")