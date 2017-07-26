strawberries = 30
isWeekEnd = True
'''
if isWeekEnd:
    if strawberries > 39:
        print("Fun")
    else:
        print("Not Fun")
else:
    if strawberries > 39 and strawberries < 61:
        print("Fun")
    else:
        print("Not Fun")
'''

if (isWeekEnd and strawberries < 39) or (strawberries < 39 and strawberries > 61):
    print("Not Fun!")
else:
    print("Fun!")
