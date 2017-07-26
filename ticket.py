speed = 40
isBirthday = False

if isBirthday:
    if speed < 31 + 5:
        print("No Ticket")
        
    elif speed > 30  and speed < 51 + 5:
        print("Small Ticket")

    else:
        print("Big Ticket")
else:
    if speed < 31:
        print("No Ticket")
        
    elif speed > 30 and speed < 51:
        print("Small Ticket")

    else:
        print("Big Ticket")
