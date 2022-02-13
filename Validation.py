import re
import requests
import email_validator



def domainvalidate(email):
    domain = email.split('@')[1]
    if (domain == "u.northwestern.edu"):
        return 0;
    else:
        return 1

print(domainvalidate("ashleylee@u.northwestern.edu"))

def addressvalidate(email):
    return 0