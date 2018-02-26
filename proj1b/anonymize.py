# Marcy Held
# SI 507, Project 1
# 26 Jan 2017


# NOTE: mbox-anon-key.txt, mbox-anon.txt, mbox-short.txt, and mbox.txt omitted for security reasons

import re
import random

# 1) Find the email addresses in the text file/
#    Find the email address in the line
# 2) Search to see if that email address already has an ID
# 2b) If no, assign a unique random number ID to the email address
#     surrounded by %%ID_HERE%%
# 3) After all of the email address have been changed, write the
#    text of the modified 'mbox.txt' file to a new file called 'mbox-anon.txt'
# 4) Write the mapping from anon ID to email address to another file
#    called 'mbox-anon-key.txt' (will hold all of the email/ID pairs)
mBox_infile = open('mbox.txt', 'r')

#Collect all parts of mbox.txt that have:
# 1) non-whitespace char(s),
# 2) followed directly by an @ symbol,
# 3) followed directly by some other non-whitespace char(s)
catchAll = []
for line in mBox_infile.readlines():
    catchAll = catchAll + re.findall('\S+@\S+', line)
mBox_infile.close()

# Get rid of the message IDs!
# Go through the list catchAll to find all items that
# DO NOT begin with a number
# (or, find all items that begin with any letter) and add
# them to the validEmails list
validEmails = []
for item in catchAll:
    if re.search('^[A-Za-z]', item) and re.search('[A-Za-z]$', item):
        validEmails.append(item)
    elif re.search('^<[A-Za-z]', item) and re.search('[A-Za-z]>$', item):
        validEmails.append(item[1:-1])

# Assign an anonymous ID number to each of the emails in validEmails list
anon_keys = {}
for email in validEmails:
    if email not in anon_keys:
        randomNum = random.randrange(10000, 99999)
        randomKey = '%%' + str(randomNum) + '%%'
        while randomKey in anon_keys.values():
            randomNum = random.random(10000, 99999)
            randomKey = '%%' + str(randomNum) + '%%'
        anon_keys[email] = randomKey

# Create 'mbox-anon.txt' file that re-writes the 'mbox.txt' file but
# replaces each email address with its anonymous ID

mBox_infile2 = open('mbox.txt')
mBox_outfile = open('mbox-anon.txt', 'w')

for line in mBox_infile2:
    newline = line
    for email in anon_keys.keys():
        if email in line:
            newline = newline.replace(email, anon_keys[email])
    mBox_outfile.write(newline)

mBox_infile.close()
mBox_outfile.close()

# Write all emails and IDs to the 'mbox-anon-key.txt' file
mBox_keysfile = open('mbox-anon-key.txt', 'w')

for email in anon_keys.keys():
    emailID = anon_keys[email].strip('%')
    mBox_keysfile.write(emailID + "=" + email + '\n')

mBox_keysfile.close()
