from datetime  import datetime
import random
import re

def get_days_from_today(date):
    try:
        now = datetime.today()
        cur_date = now.date()
        time_from_str = datetime.strptime(date, "%Y-%m-%d").date()
        difference = time_from_str.toordinal() - cur_date.toordinal() 
        return difference
    except ValueError:
        print("Рядок дати у форматі 'РРРР-ММ-ДД'")
    
def get_numbers_ticket(min, max, quantity):
    list_items = []
    if min > 0 and max <= 1000:
        num = []     
        while len(num) < quantity:            
            number = random.randint(min, max)
            if number not in num:                
                num.append(number)        
        list_items = num
        return list_items
    else:
        return list_items
    
def normalize_phone(phone_number):
    numb = phone_number.strip()
    pattern = r"[^+\d]"
    replacement = r""
    formatted_phone = re.sub(pattern, replacement, numb)
    if formatted_phone.startswith("38"):
        formatted_phone = "+" + formatted_phone
    elif not formatted_phone.startswith("+38"):
        formatted_phone = "+38" + formatted_phone       
    
    return formatted_phone
 

