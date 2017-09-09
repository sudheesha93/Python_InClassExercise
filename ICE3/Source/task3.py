mylist=[{'course':1,'LastGPA':90,'CurrentGPA':80},
        {'course':1,'LastGPA':95,'CurrentGPA':85},
        {'course':1,'LastGPA':100,'CurrentGPA':100}]

def sum_v1_v2_into_v(mylist):
    for d in mylist:
        v1 = d.pop('LastGPA')
        v2 = d.pop('CurrentGPA')
        d['LastGPA and CurrentGPA'] = (v1 + v2)/2
    print(mylist)

sum_v1_v2_into_v(mylist)