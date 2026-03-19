#Let's do math! I have a user who needs some help figuring out how much their groceries will cost. The user has entered the prices of four items. Costs are in $
itemCost1 = 4
itemCost2 = 24
itemCost3 = 12
itemCost4 = 3
#SECTION I: Numbers Application
#IN ORDER TO GET FULL CREDIT YOU MUST HAVE THE COMPUTER CALCULATE RESULTS USING THE VARIABLE NAMES AND MATH OPERATORS!!!

#1. What would the total price be if the user bought all four items? Calculate using the variables from the first box. Place result in variable called total1 and print the result.
total1 = itemCost1 + itemCost2 + itemCost3 + itemCost4 
print(total1)
#2. What would the total price be if the user bought only items 1 and 2? Calculate using the variables from the first box. Place result in variable called total2 and print the result.
total2 = itemCost1 + itemCost2 
print(total2)
#3. What would be the total price if the user bought only items 2 and 4? Calculate using the variables from the first box. Place result in variable called total3 and print the result.
total3 = itemCost2 + itemCost4
print(total3)
#4. Imagine there was a fifth item that the user wants to now buy. The price is equal to the price of item2 divided by the price of item4. What is the price of item5? Place result in variable called itemCost5 and print the result.
itemCost5 = itemCost2 / itemCost4 
print(itemCost5)
#5. What is the new total price of the user's groceries? Calculate using the variables from the first box. Place result in variable called total5 and print it.
total5 = (total1 + itemCost5)
print(total5)
#6. What is the price if the user buys items 3 and 5? Place result in variable called total6 and print it.
total6 = total3 + total5 
print(total6)
#7. What is the total price if the user buys 4 of item 1? MUST USE MULTIPLICATION Place result in variable called total7 and print it.
total7 = (itemCost1) *4
print(total7)
#8. What is the total price if the user buys 3 of item 4 at half of the original price of item 4? Place result in variable called total8 and print it.
total8 =(itemCost4/ 2) *3
primt = total8
#9. What is the total price if the user buys 4 of item 2 plus 2 of item 4 at 5 times the original price? Place  result in variable called total9 and print it.
total9 = (itemCost2) * 2 + (itemCost4 *2) *5
print(total9)

'''
YOU SHOULD WRITE OUT WHAT THE ANSWER SHOULD BE IN ORDER TO CHECK THAT YOU GOT THE RIGHT ANSWER

SECTION II: Do not complete until we have covered Lists and Boolean Expressions
'''

#10. a)-f) Using a Boolean expressions (so not calculating in your heads), determine the following:
#a) Is total1 greater than total2? Place result in a variable bool_a and print it
bool_a = total1 > total2
print(bool_a)
#b) Is total3 less than total5? Place result in a variable bool_b and print it
bool_b = total3 < total5
print(bool_b)
#c) Is total2 greater than or equal to total6? Place result in a variable bool_c and print it
bool_c = total2 >= total6 
print(bool_c)
#d) Is total5 less than or equal to total7? Place result in a variable bool_d and print it
bool_d = total5 <= total7
print(bool_d)
#e) Is total6 equal to total8? Place result in a variable bool_e and print it
bool_e = total6 == total8
print(bool_e)
#f) Is total9 not equal to total5? Place result in a variable bool_f and print it
bool_f = total9 != total5
print(bool_f)
#11. a) Create a list called price_list and place all four prices of the original items into it. Then print the list.
price_list = [itemCost1, itemCost2, itemCost3, itemCost4]
print(price_list)
#b) Now print the cost of the first item using your list
print(price_list[0])
#c) Now print the cost of the last two items in the list
print(price_list[2], price_list[3])
#d) Now remove the cost of the most expensive item in the list price_list using the remove() function. Print the list.
price_list.remove(24)
print(price_list)
#e) Using the len() function, print the length of price_list
print(len(price_list))
#f) Add the price of item 5 from problem 4 to the end of price_list using the append() function and then print the list.
price_list.append(itemCost5)
print(price_list)
#Bonus: Print all of the results from problems 1-10 in a nice format using words and f-string notation. '
print(f" ")