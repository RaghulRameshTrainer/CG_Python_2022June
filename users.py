from encaps_ex import Account

a1=Account('Raghul','Ramesh',1000)
print(a1.getBalance())
print("Username:",a1.username)
print("Password:",a1.password)
a1.setBalance(1000)
print(a1.getBalance())
print("Direct call balance:",a1._Account__balance)