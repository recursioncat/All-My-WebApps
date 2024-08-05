def calculator(name1, name2):
    name=name1+name2
    new_name=name.lower()
    t=new_name.count('t')
    r=new_name.count('r')
    u=new_name.count('u')
    e=new_name.count('e')
    tens=t+r+u+e
    l=new_name.count('l')
    o=new_name.count('o')
    v=new_name.count('v')
    e=new_name.count('e')
    ones=l+o+v+e
    percentage=tens*10+ones
    if(percentage <10 or percentage>90  ):
        print(f"your love score is {percentage}%, you go together like coke and mentos")
    else:
        print(f"your love score is {percentage}%")
    
    return percentage
