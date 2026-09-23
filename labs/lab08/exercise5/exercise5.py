main_course = input()
drink = input()
dessert = input()
if main_course == "Chicken":
    main_course_price = 10
elif main_course == "Beef":
    main_course_price = 12
else:
    main_course_price = 11
if drink == "Soft Drink":
    drink_price = 2
else:
    drink_price = 3
if dessert == "Ice Cream":
    dessert_price = 4
else:
    dessert_price = 5

bill = (main_course_price + drink_price + dessert_price) 
final_bill = bill * 0.1 + bill
print(f"{final_bill:.2f}")
