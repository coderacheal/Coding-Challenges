# return masked string
def maskify(cc):
    
    masked_string = []
    
    if len(cc) < 4:
        return cc
    else:
        for hash in cc[:-4]:
            hash = '#'
            masked_string.append(hash)
        for char in cc[-4:]:
            masked_string.append(char)
            
        hashed = ''.join(masked_string)
            
        print(hashed)
    return hashed
