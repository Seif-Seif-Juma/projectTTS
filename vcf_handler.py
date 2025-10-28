import vobject

def parse_vcf(file_path):
    contacts = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for contact in vobject.readComponents(f.read()):
            try:
                name = str(contact.fn.value)
                # Get the first telephone number
                tel = str(contact.tel.value)
                contacts.append({
                    'name': name,
                    'phone': tel
                })
            except AttributeError:
                continue
    return contacts