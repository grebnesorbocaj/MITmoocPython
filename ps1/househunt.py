

portion_down_payment = 0.25
current_savings = 0
r = 0.04

annual_salary  = float(input("How much do you earn per year? "))
portion_saved = float(input("What percent of your salary do you save? \n(Enter as decimal, where 1 = 100%, .1 = 10%, .01 = 1%) "))
total_cost = float(input("How much does the house cost? "))
semi_annual_raise = float(input("What's your semi annual raise? Enter as decimal (.1 = 10%) "))
down = total_cost*portion_down_payment
i = 1
current_savings = (annual_salary*portion_saved)/12

while(current_savings < down):
	invest = current_savings*r/12
	current_savings = current_savings + (annual_salary*portion_saved)/12 + invest
	i=i+1
	if(i%6 == 0):
		annual_salary = annual_salary*(1+semi_annual_raise)

print("%s months to save enough for ya house" %(i))

