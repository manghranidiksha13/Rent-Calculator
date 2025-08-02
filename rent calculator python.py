Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #rent calculator in python - @codingwithsagar
... 
... ## Inputs we need from the user
... # Total rent
... # Total food ordered for snacking
... # Electricity units spend
... # Charge per unit 
... # Persons living in room/flat
... 
... ## Output
... # Total amount you've to pay is
... 
... rent = int(input("Enter your hostel/flat rent = "))
... food = int(input("Enter the amount of food ordered = "))
... electricity_spend = int(input("Enter the total of electricity spend = "))
... charge_per_unit = int(input("Enter the charge per unit = "))
... persons = int(input("Enter the number of persons living in room/flat = "))
... 
... total_bill = electricity_spend * charge_per_unit
... 
... output = (food + rent + total_bill) // persons
... 
... print("Each person will pay = ", output)
SyntaxError: multiple statements found while compiling a single statement
>>> 
= RESTART: C:/Users/DELL/AppData/Local/Programs/Python/Python313/rent calculator.py
Enter your hostel/flat rent = 4000
Enter the amount of food ordered = 3000
Enter the total of electricity spend = 100
Enter the charge per unit = 10
Enter the number of persons living in room/flat = 3
Each person will pay =  2666
