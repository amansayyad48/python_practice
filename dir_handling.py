import os

dir = "C:\ICB_Files\Goal_2024"
word = "Message"

for file in os.listdir(dir):
    cur_path = os.path.join(dir, file)

    if os.path.isfile(cur_path):
        # print(cur_path)
        with open(cur_path, "r") as fp:
            file = fp.readlines()
            # print(file)
            for line in file:
                if word in line:
                    print(f"{word} is present in file {cur_path}")
