def getVals():
    annual_salary = float(input("What is your annual salary?"))
    sal_pct = float(input("Salary Percentage to Save (as a decimal): "))
    total_cost = float(input("Total home cost: "))
    r = .04
    portion_saved = 0
    months = 0
    portion_down_payment = .25
    down_pymt_amt = total_cost * portion_down_payment
    monthly_salary = float((annual_salary/12))
    new_amt = portion_saved*r/12
    
    print("Mnthly add: %d, Down Pymt: %f" % (monthly_salary_add, down_pymt_amt))
    
    while(portion_saved < down_pymt_amt):
        monthly_salary_add = (portion_saved * r) + (monthly_salary * sal_pct)

        portion_saved += monthly_salary_add
        months +=1
        print("saved: %d, months: %d" % (portion_saved, months))
        
    print("Number of months: %d" % months)
    
getVals()