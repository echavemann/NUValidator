import re
import requests
import email_validator



def domainvalidate(email):
    domain = email.split('@')[1]
    if (domain == "u.northwestern.edu"):
        return 0;
    else:
        return 1


def addressvalidate(email):
    response = requests.get (
        "https://isitarealemail.com/api/email/validate",
        params = {'email' : email})
    status = response.json()['status']
    
    if status == 'valid':
        return 0
    elif status == 'invalid':
        return 1
    else:
        return 2



def emailvalidate(email):
    if "@" in email:
        check1 = domainvalidate(email)
        if check1 == 0:
            check2 = addressvalidate(email)
            if check2 == 0:
                print ("Email verified!")
                return 0
            
    print("Verification Failed.")
    return 1