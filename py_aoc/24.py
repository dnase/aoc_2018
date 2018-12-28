from util import get_data
import re

class army:
    def __init__(self, units, hp, immunity, weakness, ap, damage, initiative):
        self.alignment = ''
        self.units = units
        self.hp = hp
        self.immunity = immunity
        self.weakness = weakness
        self.ap = ap
        self.damage = damage
        self.initiative = initiative

def parsefunc(s):
    return s.strip()

def get_army(line):
    parts = line.split(' ')
    units = int(parts[0])
    hp = int(parts[4])
    immunity = []
    weakness = []
    if '(' in line:
        immune_clause = line[line.index('(') + 1:line.index(')')]
        immune_parts = immune_clause.split(' ')
        for i, p in enumerate(immune_parts):
            if p == 'immune':
                for im in immune_parts[i:]:
                    if ',' in im:
                        immunity.append(im[:-1])
                    elif ';' in im:
                        immunity.append(im[:-1])
                        break
                    elif im == 'to':
                        pass
                    else:
                        immunity.append(im)
                        break
            if p == 'weak':
                for we in immune_parts[i:]:
                    if ',' in we:
                        weakness.append(we[:-1])
                    elif ';' in we:
                        weakness.append(we[:-1])
                        break
                    elif we == 'to':
                        pass
                    else:
                        weakness.append(we)
                        break
    doesidx = parts.index('does')
    ap = int(parts[doesidx + 1])
    damage = parts[doesidx + 2]
    initiative = int(parts[doesidx + 6])
    return army(units, hp, immunity, weakness, ap, damage, initiative)

def get_armies(seq):
    armies = {}
    for i, l in enumerate(seq):
        if 'Immune System' in l or 'Infection' in l:
            a = l[:-1]
            j = 1
            armies[a] = []
            line = seq[i + j]
            while 'units' in line:
                armies[a].append(get_army(seq[i + j]))
                j += 1
                try:
                    line = seq[i + j]
                except:
                    line = ''
    return armies

def target_selection(armies):
    targets = {}
    for armyname, a in armies.items():
        if armyname == 'Immune System':
            enemyarmy = armies['Infection']
        elif armyname == 'Infection':
            enemyarmy = armies['Immune System']
        order = sorted(a, key=lambda g: g.units * g.ap)
        for group in order:
            group.alignment = armyname
            priority = filter(lambda g: group.damage not in g.immunity, enemyarmy)
            if len(priority) > 0:
                weak = filter(lambda g: group.damage in g.weakness, priority)
                if len(weak) > 0:
                    targets[group] = max(weak, key=lambda g: g.units * g.ap)
                else:
                    targets[group] = max(priority, key=lambda g: g.units * g.ap)
            else:
                targets[group] = max(enemyarmy, key=lambda g: g.units * g.ap)
    return targets

def combat(targets):
    for group, target in targets:
        if target.units < 1:
            target.units = 0
            pass
        else:
            if group.damage in target.immunity:
                pass
            elif group.damage in target.weakness:
                #print (((group.ap * 2) / target.hp) - (group.ap % target.hp))
                target.units -= abs((((group.ap * group.units) * 2) / target.hp) - (((group.ap * group.units) * 2) % target.hp))
            else:
                #print (((group.ap * group.units) / target.hp) - ((group.ap * group.units) % target.hp))
                target.units -= abs(((group.ap * group.units) / target.hp) - ((group.ap * group.units) % target.hp))
    return targets


def part1(seq):
    armies = get_armies(seq)
    targets = target_selection(armies)
    t = sorted(targets.items(), key=lambda (k, v): k.initiative)
    infection = sum([g.units for g, _ in t if g.alignment == 'Infection'])
    immune_system = sum([g.units for g, _ in t if g.alignment == 'Immune System'])
    while infection > 0 and immune_system > 0:
        t = combat(t)
        infection = sum([g.units for _, g in t if g.alignment == 'Infection'])
        immune_system = sum([g.units for _, g in t if g.alignment == 'Immune System'])
    temp = [(ta.units, ta.alignment) for _, ta in t]
    print temp
    return immune_system


def part2():
    return True

seq = get_data(24, parsefunc)

print("P1: ", part1(seq))
print("P2: ", part2())
