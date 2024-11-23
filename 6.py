#dor dor havaii
def main():

    n,m=number_of_cities_airlines()
    cities=vorod_cities(n)
    airlines=vorod_air_lines(m)
    print_dest(cities,airlines)


def print_dest(cities,airliens):
    for city in cities:
        dest=airliens.get(city,[])
        if dest:
            print(len(dest))
            for dest in dest
                print(dest)
        else:
            print(0)


def vorod_cities(n):
    cities=[input() for _ in range(n)]
    return cities

def vorod_number_of_cities_airlines():
    n,m=input().split()
    n= int(n)
    m= int(m)
    return n,m






if __name__ == '__main__':
    main()
