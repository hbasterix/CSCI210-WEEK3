def rle_compress(s: str) -> str:
    s = ''.join(ch for ch in s if ch.isalpha())   # keep only letters
    out = []
    i, n = 0, len(s)
    while i < n:
        j = i + 1
        while j < n and s[j] == s[i]:
            j += 1
        out.append(s[i] + str(j - i))  # char + run length
        i = j
    return ''.join(out)

print(rle_compress("AaaaA"))  # A1a3A1
