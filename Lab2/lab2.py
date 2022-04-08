#Standard Library Lab

from re import A


def prob1(L):
    return "Min: {}, Max: {}, Average: {}".format(min(L), max(L), sum(L)/len(L))

def prob2():
    #int
    a = 1
    b=a
    a+=1
    print("Int mutable:",b==a)

    #string
    s1 = "hello"
    s2 = s1
    s1 = "hi"
    print("String mutable:",s1==s2)

    #list
    l1 = ['hi','hello','goodbye']
    l2=l1
    l2[0]='hey'
    print("List mutable:", l2==l1)

    #tuple
    t1 = (1,2)
    t2=t1
    t1+=(1,)
    print("Tuple mutable:",t2==t1)

    #set
    set1 = set([1,2,3,1])
    set2 = set1
    set1.add(4)
    print("Set mutable:",s2==s1)

    return

def main():
    #Problem 1
    print("\nProblem 1:")
    new_list = [1,2,3,4,5,6,7]
    answers = prob1(new_list)
    print(answers)
    
    #Problem 2
    print("\nProblem 2:")
    prob2()

if __name__ == "__main__":
    main()