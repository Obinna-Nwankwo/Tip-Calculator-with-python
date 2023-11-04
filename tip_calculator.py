#Docs on calculation with python
#you can do alot of thing using python 


print("Welcome to The New Tip Calculator!\n")#--->the (print) prints out the statement

BILL  =  float(input("What is your totla bill? :\n"))#--->the (\n) print it in a new line 
TIP  =  int(input("What percentage tip would you like to be given? :\n"))#---> the (float) allows you to input a floatiog point number like 0.0000 or 000.0
PEOPLE  =  int(input("How many people to split the bill? :\n"))#---> the (int) allows you to  input normal number like 1 to 1000 infinit

TIP_PERCENT  =  (TIP/100) * BILL # --> this normal maths calculation in school
TOTLA_TIP  =  BILL +  TIP_PERCENT

BILL_PER  =  TOTLA_TIP / PEOPLE

TOTLA  =  "{:.2f}".format(BILL_PER) # --> the ("{:.2f}".format) is using to round a decimal number and you spacify it by :.3 or any number you want to round it too.

print(f"Each Person Should Pay: ${TOTLA}") #---> the (f) is called f-strings using in concatenation two or more bool or int even strings 