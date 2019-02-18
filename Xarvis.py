import sys
sys.path.append('/mymodule/')
import mymodule
from mymodule.mathy import *

print(responses[0])
print(responses[1])
while True:
    print()
    text=input("What do you want me to perform?\n")
    for word in text.split(' '):
        if word.upper() in operations.keys():
            try:
                l=extract_from_text(text)
                r=operations[word.upper()](l[0],l[1])
                print(r)
            except:
                print("something wrong,do it again")
            finally:
                break
        elif word.upper() in commands.keys():
            commands[word.upper()]()
            break
    else:
        sorry()
    
