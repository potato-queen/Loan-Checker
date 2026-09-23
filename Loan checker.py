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
    if age>80:
        print("Congrats on living so long but unfortunatly we have to reject your loan.")
        break
    elif age>20:
        credit_score=int(input("Enter your credit score: "))
        if 900>credit_score>580:
            income=int(input("Enter your yearly income : "))
            if income>10000:

                left_income=income/12
                print("Your monthly income is ",left_income)
                print("")

                if left_income<10000:
                    print("Denied: Insufficient Funds")
                    break
                else:
                    Food_amt=int(input("Enter your monthly food and hygine bill: "))
                    left_income-=Food_amt
                    print("")
                    utilities=int(input("Enter your monthly utilities bill: "))
                    left_income-=utilities

                    if left_income<0:
                        print("Not approved: Insuffecient balance")
                        break
                    else:
                        print("10%"+" of the income left will be stored for your free spending")
                        spending=left_income%10
                        left_income-=spending
                        print("Money left for spending i.e (10%):",spending)

                        print()

                        y=input("Do you have any previous loans[y/n]: ")
                        print()
                        if y.lower()=='y':
                            num=int(input("Enter the number of pre existing loans: "))
                            if num<5:
                                cost=int(input("Enter the total loan amt: "))
                                paid=int(input("Enter the amt paid: "))
                                print("")
                                if num>3:
                                    print("You have more than 3 loans at a time.")
                                    print("Payment risk.")
                                    print("Application Denied.")
                                    break
                                print("Assuming that 25%"+" of the money is not used and the rest is alloted for the repayment for all the loans: ")
                                not_used=(left_income/100)*25
                                left_income-=not_used
                                print("The money that will be alloted for all your loans= ",left_income)
                                print()
                            else:
                                print("One cannot have more than 5 loans at a given point.")#just an example
                                break
                        if left_income>10000:
                            print("Loan approved")
                            if credit_score>740:
                                print("Premeuim loan accessible")
                                print("Talk to the bank.")
                                break
                        elif 10000>left_income>1000:
                            print("Approved for a mid range loan.")
                        else:
                            print("Not approved:Due to insufficent balance.")
                            break
            else:
                print("Not approved: Due to income defficiencies.")
                break
        elif credit_score>900:
            print("Score not possible ")
        else:
            print("Not approved:Due to insufficent credit score [more than 580]")
            break
    else:
        print("Not approved:Minimun age requirement not met[21].")
        break