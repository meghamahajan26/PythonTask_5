
def convert_date_format(date_str, current_format, desired_format):
    from datetime import datetime
    
    date_obj = datetime.strptime(date_str, current_format)
   
    return date_obj.strftime(desired_format)


date_str = "2024-10-15" 
current_format = "%Y-%m-%d" 
desired_format = "%d-%m-%Y" 

formatted_date = convert_date_format(date_str, current_format, desired_format)
print("Formatted Date:", formatted_date)
