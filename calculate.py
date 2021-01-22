def calculate(days):
    pay = 200
    
    if days > 14 < 30:
        pay += 50
    elif days > 30 < 60:
        pay += 80
    elif days > 60:
        pay += 100
        
return pay*days