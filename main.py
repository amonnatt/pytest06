from function import display_month

c = "y"
while c == "y":
    input_number = input("Number : ")
    # if input_number.isdigit():
    #     if type(input_number) == float:
    #         input_number = float(input_number)
    #     else:
    #         input_number = int(input_number)
    # else:
    #     input_number = str(input_number)
    try:
        try:
            input_number = int(input_number)
        except:
            input_number = float(input_number)
    except:
        input_number = str(input_number)

    result = display_month(input_number)
    print(result)
    c = input("(y/n) :")


# python main.py
