from typing import Dict


def get_valid_passport_count(filename: str) -> int:
    
    f = open(filename, 'r')
    passports = [x.replace('\n', ' ') for x in f.read().split('\n\n')]
    valid_count = 0

    for i in range(len(passports)):
        dick = {}

        for elem in passports[i].split():
            dick[elem.split(':')[0]] = elem.split(':')[1]

        passports[i] = dick

    for p in passports:
        if is_valid(p):
            valid_count += 1

    return valid_count


def is_valid(passport: Dict[str, str]) -> bool:

    if len(passport) < 7 or (len(passport) == 7 and 'cid' in passport):
        return False

    fields = [
              'byr',
              'iyr',
              'eyr',
              'hgt',
              'hcl',
              'ecl',
              'pid'
              ]

    conditions = [
                  check_birth_year(passport[fields[0]]),
                  check_issue_year(passport[fields[1]]),
                  check_expir_year(passport[fields[2]]),
                  check_height(passport[fields[3]]),
                  check_hair_color(passport[fields[4]]),
                  check_eye_color(passport[fields[5]]),
                  check_passport_id(passport[fields[6]]),
                  ]
   
    return all(conditions)


def check_birth_year(byr: str) -> bool:
    # byr (Birth Year) - four digits; 1920 <= x <= 2002.
    return byr.isdecimal() and 1920 <= int(byr) <= 2002


def check_issue_year(iyr: str) -> bool:
    # iyr (Issue Year) - four digits; 2010 <= x <= 2020.
    return iyr.isdecimal() and 2010 <= int(iyr) <= 2020


def check_expir_year(eyr: str) -> bool:
    # eyr (Expiration Year) - four digits; 2020 <= x <= 2030.
    return eyr.isdecimal() and 2020 <= int(eyr) <= 2030


def check_height(hgt: str) -> bool:
    # hgt (Height) - a number followed by either cm or in:
    # If cm, the number must be at least 150 and at most 193.
    # If in, the number must be at least 59 and at most 76.

    if hgt[-2:] == 'cm' and hgt[:-2].isdecimal():
        return 150 <= int(hgt[:-2]) <= 193
    if hgt[-2:] == 'in' and hgt[:-2].isdecimal():
        return 59 <= int(hgt[:-2]) <= 76

    return False


def check_hair_color(hcl: str) -> bool:
    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.

    hex_values = "0123456789abcdef"

    for c in hcl[1:]:
        if c.lower() not in hex_values:
            return False

    return hcl[0] == '#' and len(hcl) == 7


def check_eye_color(ecl: str) -> bool:
    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    return ecl in [
                   "amb",
                   "blu",
                   "brn",
                   "gry",
                   "grn",
                   "hzl",
                   "oth"
                   ] 


def check_passport_id(pid: str) -> bool:
    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    return pid.isdecimal() and len(pid) == 9


print(get_valid_passport_count('input.txt'))
