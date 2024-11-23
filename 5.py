#bad tartib
import string

def main():
    input_str="ye character aji!b #minevism 1919"
    input_str=remove_space(input_str)
    sort (input_str)


def sort(input_str):
    alephba=[]
    digits=[]
    other=[]
    for ch in input_str:
        if ch in string.ascii_letters:
            alephba.append(ch)
        elif ch in string.digits:
            digits.append(ch)
        else:
            other.append(ch)


    print(''.join(other)+''join(soted(digits))+''join(sorted(alephba, key=lambda s:s.lower())))


def remove_space(input_str):