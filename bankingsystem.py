#project on simple banking system
class banking_system:
    print("welcome to banking system")
    print("please login to continue")
    def login(self):
        details={5667:"Anu.P",6362:"Vinu.K",6543:"Arun.K.S",6776:"Athira.P.K",5778:"Akshay.P.M"}
        accnt_nmbr=int(input("enter the last four digit of your account number"))
        if accnt_nmbr in details.keys():
            print("hi",details[accnt_nmbr], "enter your pin to complete login")
        else:
            print("invalid account number please check the number you have entered")
            exit()
        login_details={"Anu.P":531,"Vinu.K":622,"Arun.K.S":638,"Athira.P.K":647,"Akshay.P.M":548}
        pin=int(input("enter your 3 digit pin number"))
        if login_details[details[accnt_nmbr]]==pin:
            print("login successful")
        else:
            print("invalid pin")
            exit()
        print("""choose one option from below:
            \n a=check balance\n
               \nb=deposit\n
              \n c=withdraw\n
               \nd=logout\n""")
        option=input("choose an option from a,b,c,d")
        amount_details={531:1000,622:500,638:500,647:1000,548:2000}
        try:
            if option=="a":
                print(details[accnt_nmbr],"your available balance is", amount_details[login_details[details[accnt_nmbr]]])
            elif option=="b":
                deposit_amount=float(input("enter an amount to deposit"))
                amount_details[login_details[details[accnt_nmbr]]]=amount_details[login_details[details[accnt_nmbr]]]+deposit_amount
                print("amount deposited successfully; your current balance is",amount_details[login_details[details[accnt_nmbr]]])
            elif option=="c":
                withdraw_amount=float(input("enter an amount to withdraw"))
                if amount_details[login_details[details[accnt_nmbr]]]>withdraw_amount:
                    amount_details[login_details[details[accnt_nmbr]]]=amount_details[login_details[details[accnt_nmbr]]]-withdraw_amount
                    print("withdrawal was successsful.your current balance is",amount_details[login_details[details[accnt_nmbr]]])
                else:
                    print("insufficient balance")
            elif option=="d":
                print("loged out successfully;login again to continue")
            else:
                raise SyntaxError
        except:
            print("something went wrong:please try again")
        finally:
            print("thankyou for choosing us;see you again")


c1=banking_system()
c1.login()




