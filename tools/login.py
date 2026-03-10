from .base import post
# from utils.email import is_valid_email

import validators

def validate_credentials(payload):
    email = (payload.get('email'))
    password = (payload.get('password'))

    if not validators.email(email):
        return f"{email} is not a valid email please try again"

    if ( len(password) < 6):
        return "Password must be at least 6 characters"
    
    return True
    
def validate_tool(email, password):

    payload = {
        "email" : email,
        "password" : password
    }

    valid = validate_credentials(payload)

    if(valid == True):
        return post("/login", payload)
    
    return valid