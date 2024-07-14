"""
CP1404/CP5632 Practical
Emails
Estimate: 40 minutes
Actual:   45 minutes
"""


def main():
    email_to_name = {}

    while True:
        email = input("Email: ").strip()
        if email == "":
            break

        extracted_name = extract_name_from_email(email)
        correct = input(f"Is your name {extracted_name}? (Y/n) ").strip().lower()

        if correct in ['', 'y', 'yes']:
            email_to_name[email] = extracted_name
        else:
            name = input("Name: ").strip()
            email_to_name[email] = name

    print()

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def extract_name_from_email(email):
    name_part = email.split('@')[0]
    name_parts = name_part.split('.')
    name = ' '.join(name_parts).title()
    return name


main()
