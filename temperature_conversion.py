def conversion_temperature():
    temp_celsius=float(input("enter temperature in celsius"))
    temp_fahrenheit=float(input("enter temperature in fahrenheit"))
    c_f=(temp_celsius*9/5)+32
    f_c=(temp_fahrenheit-32)*5/9
    print("temperature of" , temp_celsius, "convertes to fahrenheit as", c_f)
    print("temperature of", temp_fahrenheit," convertes to degree as", f_c )