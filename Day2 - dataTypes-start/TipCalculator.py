
print("Welcome to the tip calculator")
bill = input("what was the total bill? $")
tip_percentage = input("what percentage of tip would you like to give? ")
no_ofPeople = input("how many people are sharing the bill? ")

tip = int(tip_percentage) / 100

new_bill = (float(bill) * float(tip) + float(bill))



eachPerson = round(new_bill / int(no_ofPeople),2)
print(f"Each Person Should Pay ${eachPerson} " )

