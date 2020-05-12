import vobject

# read data from csv
persons = []
line = 0
with open('contacts.csv', encoding='utf-8') as f:
    process = True
    while(process):
        line = line + 1
        try:
            contact = f.readline()
            if(contact==''): break
            persons.append(contact.split(','))
        except:
            print(line)

print('Give file name')
file_name = input()
# create person
for item in persons[2:]:
    try:
        person = {'n': f'{item[0]}', 'fn': f'{item[0]}', 'tel': f'{item[34]}'}

        # create vCard
        vcard = vobject.readOne('\n'.join([f'{k}:{v}' for k, v in person.items()]))
        vcard.name = 'VCARD'
        vcard.useBegin = True

        with open(f'{file_name}.vcf', 'a', newline='') as f:
            f.write(vcard.serialize())
    except:
        print(f'error in line: {item}')