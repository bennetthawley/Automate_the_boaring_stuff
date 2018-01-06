#! python3

import re
import pyperclip

# TODO: Create a regex for phone numbers
phone_regex = re.compile(r'''
# 415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345

((\d\d\d)|(\(\d\d\d\)))?    # area code (optional)
(\s|-)                      # first separator
\d\d\d                      # first 3 digits
-                           # separator
\d\d\d\d                    # last 4 digits
(ext(\.)?\s|x)              # extension word-part (optional)
(\d{2,5})?                  # extension number-part (optional)
''', re.VERBOSE)

# TODO: Create a regex for email addresses
email_regex = re.compile(r'''

''', re.VERBOSE)

# TODO: Get the text off the clipboard

# TODO: Extract the email/phone from this text

# TODO: Copy the extracted email/phone to the clipboard
