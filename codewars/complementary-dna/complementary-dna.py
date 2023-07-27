def DNA_strand(dna):
    # code here
    comp = ''
    
    for char in dna:
        if char == 'A': comp += 'T'
        elif char == 'T': comp += 'A'
        elif char == 'G': comp += 'C'
        else: comp += 'G'
        
    return comp