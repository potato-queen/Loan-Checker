#Loan Qualification checker

"""
income yearly
existing loans
mountly budget
emergency fund
"""
while True:
    print("This is an automatic Loan eligibility checker ")
    print("")

    age=int(input("Enter your age: "))
    if age>20:
        credit_score=int(input("Enter your credit score: "))
        if credit_score>580:
            income=int(input("Enter your yearly income : "))
            if income>10000:
                income_monthly=income/12
                print("Your monthly income is ",income_monthly)
                print("")
            
                existing_emergency=int(input("Enter your already existing emergency fund amt:"))
                if existing_emergency<10000:
                    emergency=int(input("Enter your emergency fund for that month [50,100,500,other]:"))
                    fin_emergency=existing_emergency+emergency
                    left_income=income_monthly-fin_emergency
                else:
                    left_income=income_monthly
                print("Total amt of money left for you to use : ",left_income)
                print("")

                Food_amt=int(input("Enter the amount you have aloted for your monthly food and hygine : "))
                left_income-=Food_amt
                print("")
                utilities=int(input("Enter the amt you have alloted for your monthly utilities: "))
                left_income-=utilities

                print("10%"+"of the income left will be stored for your free spending:")
                spending=left_income%10
                left_income-=spending
    
                y=input("Do you have any previous loans[y/n]: ")
                if y.lower()=='y':
                    num=int(input("Enter the number of pre existing loans: "))
                    if num<5:
                        d={}
                        for i in range(1,num+1):
                            cost=int(input("Enter the total loan amt: "))
                            paid=int(input("Enter the amt paid: "))
                            t=[cost,paid]
                            d[i]=t
                        print("")
                        print("This the list of all the previous loans taken and the amounts paid.")
                        for i in d:
                            print(i+":"+d[i])
                        if len(d)>3:
                            print("You have more than 3 loans at a time.")
                            print("Payment risk.")
                            print("Application Denied.")
                            break
                        print("Assuming that 25%"+" of the money is not used and the rest is alloted for the repayment for the above loans: ")
                        not_used=(left_income/100)*25
                        left_income-=not_used
                        print("The money that will be alloted for the above loans= ",left_income/len(d))
                        print("")
                        print("The amount of money being used for paying these loans: ",left_income)
                    else:
                        print("One cannot have more than 10 loans at a given point.")#just an example
                        break
                if left_income>10000:
                    print("Loan approved")
                    if credit_score>740:
                        print("Premeuim loan accessible")
                        print("Talk to the bank.")
                        break
                else:
                    print("Not approved:Due to insufficent balance.")
                    break
            else:
                print("Not approved: Due to income defficiencies.")
                break
        else:
            print("Not approved:Due to insufficent credit score [more than 580]")
            break
    else:
        print("Not approved:Minimun age requirement not met[21].")
        break