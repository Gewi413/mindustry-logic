#!/usr/bin/env python

import pyperclip
from sys import argv

def main():
    if len(argv) < 3:
        print(f'Usage: {argv[0]} <schem name> <creator> <resources,amounts>')
        return

    name = argv[1]
    creator = argv[2]
    resources = argv[3:]
    
    item_names = 'copper lead metaglass graphite sand coal titanium thorium scrap silicon plastanium phase-fabric surge-alloy spore-pod blast-compound pyratite'.split(' ')
    items = '               '.split(' ')
    
    modifiers = [2.5, 2.25, 1.5, 1]
    out = [''] * len(modifiers)

    for res in resources:
        if ',' not in res:
            print(f'Invalid resource: "{res}". Split the amount with comma.')
            continue
        item, amount = res.split(',')
        if item not in item_names:
            print(f'Invalid resource: "{res}". Use one of {item_names}.')
            continue
        try:
            amount = float(amount)
        except:
            print(f'Invalid resource: "{res}". Specify a correct number.')
            continue
        icon = items[item_names.index(item)]
        sign = '' if amount < 0 else ''
        for i in range(len(modifiers)):
            actual = abs(amount) * modifiers[i]
            out[i] += f'\\n{sign}[white]{icon}[] {actual: .2f}'

    template = f"""
print "[sky]{name}[]\\n[slate]by {creator}[lightgray]\\n"
sensor ts1 @this @timescale
sensor ts2 @this @timescale
sensor ts3 @this @timescale
op max ts ts1 ts2
op max ts ts ts3
jump odd greaterThanEq ts 2.5
jump pod greaterThanEq ts 2.25
jump od greaterThanEq ts 1.5
jump normal always x false
odd:
    print "{out[0]}\\nwith [white]"
    jump print always x false
pod:
    print "{out[1]}\\nwith [white]"
    jump print always x false
od:
    print "{out[2]}\\nwith [white]"
    jump print always x false
normal:
    print "{out[3]}\\nwithout [white]"
print:
    printflush message1"""
    pyperclip.copy(template)

if __name__ == '__main__':
    main()
