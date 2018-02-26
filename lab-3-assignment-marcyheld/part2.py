import re

lbfile = open('littlebrother.txt')
# count = 0
# for line in lbfile.readlines():
#     if re.search('http:', line):
#         count += 1
# print (count)

# count = 0
# for line in lbfile.readlines():
#     if re.search('\S*[0-9]\S*', line):
#         count += 1
# print (count)

count = 0
for line in lbfile.readlines():
    if re.search('\d*[0-9]\d*', line):
        count += 1
print (count)
