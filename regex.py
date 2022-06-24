import re
'''
match
search
findall
sub
split
compile , finditer
'''


mystr="pet:cat i love cat pet:dog i love dog"

# matches=re.match('Pet:.{3}',mystr,re.I)
# print(matches.group())
# matches=re.search('pet:...',mystr)
# print(matches)
# matches=re.findall('pet:.{3}',mystr)
# print(matches)

#print(re.sub('love','like',mystr))
#print(re.split(':',mystr))

mystring='''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

~!@#$%^&*()_+{}|

484-545-3455
343.564.4355
434_555_2325
434 453 7732

https://www.google.com
http://www.google.com
https://google.com
https://www.google.co.in

raghulramesh@outlook.com
raghul_ramesh@yahoo.com
raghul.ramesh@gmail.com
rameshramesh@hotmail.co.in

Ha HaHa

#Write a regex pattern to match the valid mobile number
+91-9833738399
9833738399
98337383999  
983373839    
8833738399
7833738399
6833738399
5833738399  
4833738399  
3833738399  
2833738399  
1833738399  
'''
pattern=re.compile(r'(\+91\-)?\b[6-9]\d{9}\b')
#pattern=re.compile(r'.')
#pattern=re.compile(r'\d{3}[\-\.\s]\d{3}[\-\.\s]\d{4}')
#pattern=re.compile(r'https?://(www\.)?google\.com?(\.in)?')
#pattern=re.compile(r'(\w+\.)?\w+@\w+\.com?(\.in)?')
#pattern=re.compile(r'\bHa\b')

matches=pattern.finditer(mystring)
for x in matches:
    print(x.group())

# str2="raghulramesh@outlook.com"
# #pattern=re.compile(r'(\w+):(\w+)')
# res=re.findall(r'(\w+)@(\w+)(\.\w+)',str2)
# print(res[0][1])

#=====================================================================
