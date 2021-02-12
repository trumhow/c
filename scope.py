# f = open('abc.txt', encoding='utf8')
# try:
#     for line in f:
#         print(line)
# finally:
#     f.close()


with open('abc.txt', encoding='utf8') as f:
    for line in f:
        print(line)
