# literal
import string
def most_common_str(s:str)->str:
    
    if not any(not c.isspace() for c in s):
        raise ValueError("Value Error")


    pos_by_char = {ch: 1 for i, ch in enumerate(string.ascii_lowercase)}
    for ch in s:
        for chDict in pos_by_char:
            if ch == chDict:
                pos_by_char[chDict] += 1
    return max(pos_by_char, key=pos_by_char.get)

print(most_common_str("\n\t"))

      