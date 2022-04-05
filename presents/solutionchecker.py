
check=True
while check:
    x=input('Give solution: ')

    try:
        x = int(x)
        if x== 574280:
            print('Correct!, now you can open the plottwist')
            check=False
        elif x>574280:
            print('your answer is too big')
        elif x<574280:
            print('your answer is too small')
    except:
        pass
plottwist=True
while plottwist:
    x=input('Give second solution: ')

    try:
        x = int(x)
        if x==151951:
            print('Correct!')
            plottwist=False
        elif x>151951:
            print('your solution  a little to much')
        elif x<151951:
            print('try harder, that\'s not enough')
    except:
        pass