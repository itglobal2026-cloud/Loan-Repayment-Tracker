
import os
from datetime import datetime
file="Record.txt"
principle_amount=61060
insta=0

if os.path.exists(file):
    with open(file, "r") as f:
        lines = f.readlines()
        if lines:
            last_line = lines[-1].strip().split("|")
            insta = int(last_line[0].split()[1]) 
            principle_amount = int(last_line[-1].split("Rs.")[1])

def store(amount):
    global principle_amount,insta
    principle_amount=principle_amount-amount
    global insta
    insta+=1

    data=open (file,'a')
    date=datetime.now().strftime("%d-%m-%y")
    data.write(f"Installment {insta} | Date:{date} | paid:Rs.{amount} | Outstanding amount:Rs.{principle_amount}\n")
    data.close()
    print(f"Installment {insta}|{amount} paid | Outstanding amount rs.{principle_amount}\n")

def currentoutstanding(outstanding):
    print(f"Your Current outstanding amount:rs.{outstanding}\n")


while True:
    try:
        print("\t\tGold Loan Repayment Records")
        print("1.Repayment\n2.Outstanding Amount\n3.Exit")
        user=int(input('Enter choice (1 - 3):'))
        if user==1:
            payment=int(input("Enter the amount:"))
            store(payment)
        elif user==2:
            currentoutstanding(principle_amount)
        elif user==3:
            print("Exiting... Your records are safe")
            break
        else:
            print("Invalid Choice! Try again...\n")   
    except Exception:
        print("Invalid input! Try again...\n") 
    except KeyboardInterrupt:
        print("Exiting...\n")
        break

