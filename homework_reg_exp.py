import csv
from pprint import pprint
import re

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
    # pprint(contacts_list)

header = contacts_list[0]
contacts_list = contacts_list[1:]


for contact in contacts_list:
    full_name = " ".join(contact[:3]).split()
    while len(full_name) < 3:
        full_name.append('')
    contact[0], contact[1], contact[2] = full_name[:3]
    # print(full_name)

    phone = contact[5]
    pattern = r"(\+7|8)?\s*\(?(\d{3})\)?\s*-?\s*(\d{3})\s*-?\s*(\d{2})\s*-?\s*(\d{2})(\s*\(?(доб\.\s*\d+)?\)?)?"
    substr = r"+7(\2)\3-\4-\5"
    phone_pattern = re.compile (pattern)
    if phone:
        formatted_phone = (phone_pattern. sub(substr, phone)).strip()
        # print (formatted_phone)
    
    contact_dict = {}
    key = (contact[0], contact[1])
    if key not in contact_dict:
        contact_dict[key] = contact
    else:
        for i in range(len(contact)):
            if not contact_dict[key][i] and contact[i]:
                contact_dict[key][i] = contact[i]

    # print (contact_dict)

final_contacts_list = [header] + list(contact_dict.values())


with open("phonebook_raw.csv", "w", encoding="utf-8", newline='') as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(final_contacts_list)


