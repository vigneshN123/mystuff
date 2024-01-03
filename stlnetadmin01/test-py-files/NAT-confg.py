from pprint import pprint

with open('NAT-confg.txt', 'r') as f:
    fdata = f.read()

fdata = fdata.splitlines()

pprint(fdata)
new_text = []

for i in fdata:
   # pprint(i)
   list_words = i.split(" ")
   #print(list_words)
   list_words[7] = int(list_words[7]) + 10
   list_words[9] = int(list_words[9]) + 10
   list_words[7] = str(list_words[7])
   list_words[9] = str(list_words[9])
   new_string = " ".join(list_words)
   new_text.append(new_string)

new_text = "\n".join(new_text[0:])
print(new_text)




