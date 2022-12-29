year =int(input("Enter a year and check year is leap or not : "))
if year%4==0 :
    if year%100==0 :
        if year%400==0 :
            print("year is leap")
        else:
            print("year is not leap")       
    else:
        print("year is leap")
else:
    print("year is not leap")            
