import re

#  message = "Call me tomorrow at 345-234-5636 or at 122-446-6276"

# phone_num_regex  = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# match_object = phone_num_regex.search(message)
# print(match_object.group())
# print(phone_num_regex.findall(message))

# phone_num_regex  = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
# match_object = phone_num_regex.search(message)
# print(match_object.group(1))
# print(match_object.group(2))

# message = "Call me tomorrow at (345) 234-5636 or at (122) 446-6276"
# phone_num_regex  = re.compile(r'\(\d\d\d\) \d\d\d-\d\d\d\d')
# match_object = phone_num_regex.search(message)
# print(match_object.group())
# print(phone_num_regex.findall(message))

# bat_regex = re.compile(r'Bat(man|woman|copter|bat|mobile)')
# mo = bat_regex.search('Batmobile lost a wheel')
# print(mo.group())
# mo = bat_regex.search('Batmotorcycle lost a wheel')
# print(mo == None)

# bat_regex = re.compile(r'Bat(wo)?man')
# mo = bat_regex.search('Batwoman is cool')
# print(mo.group())

# phone_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# mo = phone_regex.search("Call me tomorrow at 234-5636")
# print(mo == None)
# phone_regex_better = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
# mo = phone_regex_better.search("Call me tomorrow at 234-5636")
# print(mo.group())

# bat_regex = re.compile(r'Bat(wo)*man')
# mo = bat_regex.search('Batwowowowoman is cool')
# print(mo.group())

# bat_regex = re.compile(r'Bat(wo)+man')
# mo = bat_regex.search('The tales of Batman')
# print(mo == None)
# mo = bat_regex.search('The tales of Batwoman')
# print(mo.group())

# ha_regex = re.compile(r'(Ha){3}')
# print(ha_regex.search('HaHaHa heyyyy').group())

# phone_regex = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(, )?){3}')
# mo = phone_regex.search('My phone numbers are 432-354-7848, 092-2345, 081-910-5467')
# print(mo.group())               

ha_regex = re.compile(r'(Ha){3,5}')
print(ha_regex.search('HaHaHa heyyyy').group())
print(ha_regex.search('HaHaHaHa heyyyy').group())
print(ha_regex.search('HaHaHaHaHa heyyyy').group())
