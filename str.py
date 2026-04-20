# strings are immutable
letter = '''Dear <name>,
You are selected!
<date>'''

print(letter.replace("<name>","harry").replace("<date>","23 April 2026"))

str = "jhjbf shb d hs d oihsdio   jsoiod hiohdduifh   shifh   sjd ij idsjioj   "
print(str)

if(str.find("  ")>0):
    print("Double space found")
    print(str.replace("  ", "0XXXXX0"))
else: print("no double space")

print(str)