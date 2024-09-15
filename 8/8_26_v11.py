def main(decimal_string):
    num = int(decimal_string)
    
    V1 = (num >> 0) & 0x3F 
    V3 = (num >> 12) & 0xFF
    V4 = (num >> 20) & 0xF

    result = [
        ('V1', str(V1)),
        ('V3', str(V3)),
        ('V4', str(V4)),
    ]

    return result

print(main('7142254'))  
print(main('11398097')) 
print(main('14473554'))  
print(main('16283683')) 
