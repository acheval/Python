def is_phone_number(text):
    if len(text) != 12:  # check length of string
        return False
    for i in range(0, 3):  # check area code
        if not text[i].isdecimal():
            return False
    if text[3] != "-":  # check hyphen after area code
        return False
    for i in range(4, 7):  # check for 3 more numeric characters
        if not text[i].isdecimal():
            return False
    if text[7] != "-":  # check for second hyphen
        return False
    for i in range(8, 12):  # check the last four characters for numbers
        if not text[i].isdecimal():
            return False
    return True


message = "Call me at 415-555-1011 tomorrow. 415-555-9999 is my office."
for i in range(len(message)):
    chunk = message[i : i + 12] # loop through 12 characters each iteration
    if is_phone_number(chunk):
        print("Phone number found: " + chunk)
print("Done")

print("415-555-4242 is a phone number:")
print(is_phone_number("415-555-4242"))
print("Moshi-Moshi is a phone number:")
print(is_phone_number("Moshi-Moshi"))
