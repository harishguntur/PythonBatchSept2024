#!/usr/bin/pyhton3
#a=p(1+rt)

#Varaiable initializtion
principal_balance = int(input("enter principal balance:"))
intrest_rate = float(input("enter annual interest rate:"))
time = int(input("enter time:"))

#Calculating simple interest

final_amount = principal_balance*(1+((intrest_rate/100)*time))
print("final amount:",round(final_amount,2))
