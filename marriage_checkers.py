from datetime import datetime

def bigamy(individuals, families):
    """ 
    User Story 11
    Marriage should not occur during marriage to another spouse.
    
    returns: a list of warning strings.
    """
    warnings = []
    # Find of someone is married once
    # Then check if they dont have any other active marriage(married before today).
    # Ignore active marriages with dead(death before today) spouses.
    for indi_id in individuals:
        individual = individuals[indi_id]
        count = 0
        for fam_id in individual.spouse:
            if is_married(individuals, families, fam_id):
                count += 1
        
        if count > 1:
            warnings.append(f'{individual.name} has more than 1 active marriages!')
    
    return warnings

def is_married(individuals, families, family_id):
    """
    Checks if the spouses of a given family are presently married.

    They are not married if divorce date is present and is before today
    and if one of the spouses is not alive.

    returns: a boolean
    """
    family = families[family_id]
    divorce_date = family.divorced
    if divorce_date and divorce_date < datetime.now():
        return False
    
    # if one of the partners has passed away, they are not married.
    if not is_alive(individuals, family.hid) or not is_alive(individuals, family.wid):
        return False

    return True

def is_alive(individuals, individual_id):
    """
    Checks if the individual with the given id is alive.
    """
    return individuals[individual_id].alive

def first_cousins_married(individuals, families):
    """
    User Story 19
    Searches and warns if first cousins are married
    in the given families and individuals.

    returns: a list of warning strings
    """
    warnings = []

    for fam_id in families:
        family = families[fam_id]
        parents_child_at = set()

        if not family.hid or not family.wid:
            continue

        husband = individuals[family.hid]
        wife = individuals[family.wid]

        # add grand_parents to the variable
        h_parents_famc = get_parents_famc(individuals, families, family.hid)
        w_parents_famc = get_parents_famc(individuals, families, family.wid)

        if h_parents_famc.intersection(w_parents_famc):
            warnings.append(f'{husband.name} is married to his first cousin {wife.name}!')
    
    return warnings
        

def get_parents_famc(individuals, families, indi_id):
    """
    Find grand parents of the given person.
    """
    if not indi_id:
        return set()
        
    individual = individuals[indi_id]
    parents_famc = set()

    
    if not individual.child:
        return set()
    
    for famc in individual.child:
        family = families[famc]
        father = individuals[family.hid]
        mother = individuals[family.wid]

        if father.child:
            parents_famc.update(father.child)
        if mother.child:
            parents_famc.update(mother.child)
    
    
    return parents_famc