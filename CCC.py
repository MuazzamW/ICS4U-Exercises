def S1_2016():
    s1 = sorted(input())
    s2 = sorted(input())

    if(len(s1) == len(s2)):
        if s1 is s2 and ('*' not in s1) and ('*' not in s2):
            print('A')
        else:
            for c in s1:
                if c in s2:
                    s1.remove(c)
                    s2.remove(c)
            if(len(s1)==len(s2)):
                print('A')
    else:
        print('N')
    
    
S1_2016()