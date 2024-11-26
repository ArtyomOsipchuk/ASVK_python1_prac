with open("~/text", "rb") as f:
    ff = f.read()
with open("~/text", "wb") as f:
    n = len(ff)
    f.write(ff[n//2:])
    f.write(ff[:n//2])
