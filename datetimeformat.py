# #sketch
# #dd/mm/yyyy


from datetime import datetime
import urllib.request



# bday = "09/10/1986"
# format = "%m/%d/%Y"
# req_format = datetime.strptime(bday, format).date()

# print(req_format)


bdays = ["12/24/2002", "6/20/2021", "03/02/2022"]
bdays_new = []

for b in bdays:
    format = "%m/%d/%Y"
    req_format = datetime.strptime(b, format).date()
    bdays_new.append(req_format)
    print(type(req_format))

print(bdays_new)

##On why datetime objects print weird from lists/dicts: https://stackoverflow.com/questions/311627/how-to-print-a-date-in-a-regular-format


# for key, value in a_dict.items():
#     print(key, type(value))