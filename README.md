this is a python programme to execute a simple banking system.
for that a class named banking system has created.
This class contain one method named login which guide the user to login to the bank.
if the user completed login successfully a chart which contain 4 otions a,b,c,d used for view balance,deposit,withdraw,logout respectively will be displayed.
user can choose any one of them and that will guide for further activities.
after that a thanking message is displayed.

to execute the programme properly,3 dictionaries have been created named details , login details,amount details.
1 st dictionary details contains keys as last 4 digit of the account number and values as name of the user
the programme ask the user to input last 4 digit of account number. 
the if statement following will check whether the account number included in details of the bank.
if yes programme will move to next stage otherwise will get exit.
the next dictionary login details contain name of the user as key and 3 digit pin number as values.
if the first stage was successful user will get a message to enter 3 digit pin to complete login.
if there is any mismatch between account number , user name,pin the programme will stop running after giving a message invalid pin
other wise the programme will move on to the next stage
next,the user get a chart which contain 4 options a,b,c,d .
user any can choose any one of the option.choosing option other than this will follow an error message and advise to try again
if use r choose otion a , available balance eill be displayed.for that a dictionary named amount details has created which have user pin as keys and available balance as values.
from these 3 dictionaries a link between the account number , name of the user,user pin,available balance has created automatically
if thr user choose option b it will help the user to deposit money.
for that the programme ask the user to enter an amount that he wish to deposit
the programme will add the amount to existing balance.and will give a message that amonut deposited successfully also will provide the current balance.
if the user choose option d that will help the user to withdraw money.
the user will get a messsage to enter the amount to withdraw
then the programme will cross check whether the amount entered by the user exceeds the available balance
if so a message of insufficient balance will be provide
otherwise the programme will deduct the amount entered by the user from exsting balance and the new balance will be displayed with a message that withdrawing money was successful.
if the user choose option d that will help the user to logout from the bank.
whatever option was chosen by the user; after completing the process a thanking message for the user will be provided.
to handle this try block, except block, and finally block have been created.
try block will execute the 4 options such as view balance,deposit,withdra,logout and
if any error occure except block will catch it and display an error message.
after that finally block will provide a thanking message.
an object named c1 has created to execute the programme.

