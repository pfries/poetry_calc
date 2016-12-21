#!/usr/bin/env python
import re
import editdistance

phonemes = {}

feet = {
    'iamb': [0,1],
    'trochee': [1,0],
    'dactyl': [1,0,0],
    'anapest': [0,0,1],
    'spondee': [1,1]
}

metrical_lines = {
    'iambic pentameter': [feet['iamb'] * 5],
    'dactylic hexameter': [feet['dactyl'] * 6]
}

def parse_line(line):
    pwords = []
    for word in line:
        phoneme = phonemes[word.replace('.','').upper()]
        stress = re.findall(r'\d', phoneme)
        pword = {
            'word': word,
            'stress': stress,
            'syllables': len(stress)
        }
        pwords.append(pword)
    stresses = [p['stress'] for p in pwords]
    flat = flatten(stresses)
    ip = flatten(metrical_lines['iambic pentameter'])
    dh = flatten(metrical_lines['dactylic hexameter'])
    print(flat)
    print(ip)
    print(editdistance.eval(flat,ip))
    print(dh)
    print(editdistance.eval(flat,dh))
    

def flatten(line):
    return ''.join([str(item) for sublist in line for item in sublist])
    

if __name__ == '__main__':
    with open('cmu.dict', 'r') as dict:
        for d in dict:
            (word, phoneme) = d.split(' ', 1)
            phonemes[word] = phoneme

    from optparse import OptionParser
    parser = OptionParser()
    _,line = parser.parse_args()
    parse_line(line)
