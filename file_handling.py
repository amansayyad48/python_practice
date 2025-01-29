with open(r"C:\DATA\Trail_ascii.txt", 'r') as fp:
    lines = fp.readlines()
    print(lines)
    word = "1F2A3B"

# with open("C:\DATA\Trail_ascii_new.txt", "w") as fp2:
#     count = 0
#     for i in lines:
#         print(i)
#         if i==4:
#             continue
#         else:
#             fp2.write(i)
count = 1
for line in lines:
    if word in line:
        print(word, " available in file")
        print(f"{word} available in line no.{count}")
        print(f"{word} available in line {line}")
        count += 1
    else:
        print(f"{word} not available in line no.{lines.index(line)}")
        count += 1
        # break
