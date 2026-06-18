def maskify(s: str) -> str:
    if len(s) <= 4:
        return s
    return "#" * (len(s) - 4) + s[-4:]
print(maskify("4556364607935616")) 
print(maskify("Skippy"))            
print(maskify("1"))           
print(maskify(""))     



def accum(s: str) -> str:
    return "-".join(
        n.upper() + n.lower() * i
        for i, n in enumerate(s))