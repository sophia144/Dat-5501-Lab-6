#compound interest calculator that takes initial savings amount, years of saving, number of compounding periods and the annual interest rate
#for each year of savings it returns the total savings for that year
#it also prints out how many years it would take for the savings amount to double

def comp_int_calculator():
    initial_saving = float(input("Enter your initial amount of savings: "))
    years = int(input("Enter the number of years you're saving for (whole numbers only): "))
    interest_rate = float(input("Enter the annual interest rate (decimal): "))
    time = 0 
    running_total = initial_saving
    for time in range(0, years):
        print(f"Year {time}: £{running_total}")
        time += 1
        running_total = running_total * (1 + interest_rate)

#number of years it takes for the savings to double
def savings_double_calc():
    initial_savings =  float(input("Enter your initial amount of savings: "))
    interest_rate = float(input("Enter the annual interest rate (decimal): "))
    doubled_savings = initial_savings * 2
    years_to_double = None
    #INCOMPLETE
