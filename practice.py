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
    
def get_numbers_ticket(min_num, max_num, quantity):
    if not (min_num >= 1 and max_num <= 1000 and min_num < max_num):
        return []     
    if not (0 < quantity <= max_num - min_num +1):
        return []
    return sorted(random.sample(range(min_num, max_num+1), quantity))
    
def normalize_phone(phone_number):
    numb = phone_number.strip()
    pattern = r"[^+\d]"
    replacement = r""
    formatted_phone = re.sub(pattern, replacement, numb)
    if formatted_phone.startswith("+"):
       return formatted_phone
    if formatted_phone.startswith("38"):
       return "+" + formatted_phone 
    return "+38" + formatted_phone
 

