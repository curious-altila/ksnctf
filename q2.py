import string

rot13 = string.maketrans(
     "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz",
     "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")

print string.translate("jxuiushujfqiifxhqiuyiskshsqnwdgxadmyjnezaarjupgcmii ",rot13)


