#code wars

def string_clean(s):
    
    result = ""
    for char in s:
        if char < '0' or char > '9': 
            result += char  
    return result