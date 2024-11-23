#moshkel iman
import math
def main():
    number=tedad_emtehan()
    weight_score=weight_score(number)
    numeric_score=compute_score(weight_score)
    result=to_ch(math.ceil(numeric_score))
    return result

def tedad_emtehan():
    number=intput()
    return int(number)

def weight_score(number):
    weight_score =[]
    for i in range(number):
       weight,score= input().split()
        weight=int(weight)
        weight_score.append((weight,score))
    return weight_score

def compute_score(weight_score):
    sum=0
    total_weight=0
    for weight,score in weight_score:
        sum+= weight * to_numeral(score)
        total_weight+=weight
    numeric_score=sum / total_weight
    return numeric_score

def to_numeral(ch_score):
    score={'A':5,'B':4,'C':3,'D':2,'E':1,'F':0}
    return score[ch_score]

def to_ch(num,score):
    score={5:'A',4:'B',3:'C',2:'D',1:'E',0:'F'}
    return score[num_score]



if __name__ == '__main__':
    print(main())
