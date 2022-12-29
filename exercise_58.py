import re
import email.utils

n = int(input())

necesarios = r"^([a-zA-Z][a-zA-Z0-9\_\-\.]+)\@[a-zA-Z]+\.[a-zA-Z]{1,3}$"

for _ in range(n):
    nombre, correo = email.utils.parseaddr(input())
    if re.search(necesarios, correo):
        print(email.utils.formataddr((nombre, correo)))