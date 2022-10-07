# generate password which is tough to breakk

import random

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbols = "@#$%&*/\?"

Use_for = lower_case + upper_case + number + symbols
password_length = 10

password = "".join(random.sample(Use_for, password_length))
print("Here is your password: " , password)