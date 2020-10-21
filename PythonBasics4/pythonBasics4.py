# Python Activity
#
# Fill in the code for the functions below.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code.

# # Part A.
def array_2_dict(emails, contacts):
    if len(emails) < 1:
        return contacts
    x = 0
    for i in contacts:
        contacts[i] = emails[x]
        x += 1
    return contacts

# # Part B.
def array2d_2_dict(contact_info, contacts):
    if len(contact_info) < 1:
        return contacts
    if len(contact_info[0]) < 1:
        return contacts
    x = 0
    for i in contacts:
        contacts[i] = {"email": contact_info[x][0] , "phone": contact_info[x][1]}
        x += 1
    return contacts

# # Part C.
def dict_2_array(contacts):
    contactList = [[],[],[]]
    email = contactList[0]
    phone = contactList[1]
    name = contactList[2]
    x = 0

    for i in contacts:
        name.append(i)
        email.append(contacts[i].get("email"))
        phone.append(contacts[i].get("phone"))


    return contactList
