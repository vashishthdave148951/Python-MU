#extracting emails from text
import re
text_with_email = "Contact us at [EMAIL_ADDRESS] or [EMAIL_ADDRESS] for help."
pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
extracted_emails = re.findall(pattern, text_with_email)
print("1. Extracted Emails:")
if extracted_emails:
    for email in extracted_emails:
        print(f"   - {email}")
else:
    print("   No emails found") 