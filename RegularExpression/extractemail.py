import re
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
text_with_emails = """Contact us at trainer@smartcliff.in or 
gayathrimanoj@smartcliff.in
"""
emails_found = re.findall(email_pattern, text_with_emails)
if emails_found:
    print("Email addresses found:", emails_found)
else:
    print("No email addresses found")
