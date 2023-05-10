
## Regex expressions

The code uses regular expressions to extract phone numbers and email addresses from a given string, and replace the email addresses with a specified replacement string.

The code starts by importing the 're module', which provides support for regular expressions in Python.

The function, extract_phone_numbers(), takes a string as input and extracts all the phone numbers in it using a regular expression pattern. The pattern \d{3}\D{0,3}\d{3}\D{0,3}\d{4} matches any sequence of 10 digits that may be separated by up to 3 non-digit characters.

The function, extract_email_addresses(), also takes a string as input and extracts all the email addresses in it using a regular expression pattern. The pattern \b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b matches any sequence of characters that resemble a valid email address.

The function, replace_email_addresses(), takes a string and a replacement string as input, and replaces all the email addresses in the string with the replacement string using the re.sub() function.

The code then defines a string variable called "string" that contains an example string to work with.

The code then calls the extract_phone_numbers() function and extract_email_addresses() function with the "string" variable, and stores the results in "phone_numbers" and "email_addresses" variables, respectively.

Finally, the code calls the replace_email_addresses() function with the "string" variable and the replacement string "[REDACTED]", and stores the result in the "new_string" variable.

The code then prints the phone numbers, email addresses, original string, and new string for demonstration purposes.