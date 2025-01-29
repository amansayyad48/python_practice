normal = ["Aman", "Ruchi"]
sample_dict = {"physics": 82, "math": 56, "history": 75}
print(min(sample_dict, key=sample_dict.get))
print(sample_dict)
print(sample_dict.pop("physics"))
print(sample_dict)
sample_dict.update({"physics": 92})
print(sample_dict)
# marks = dict.fromkeys(normal, sample_dict)
marks = dict()
for i in normal:
    marks.update({i: sample_dict})
print(marks)

