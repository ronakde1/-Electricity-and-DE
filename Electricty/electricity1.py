#attempt1: text based
#says the resitance current for a series circuit
#then allows for parallel
#then allows for ac and gives RMS current for a given frequency
components=[]
voltage=0
resistance=0
num=int(input("Input number of components "))
for i in range(num):
    print(f"Enter component {i+1}")
    temporary=input()
    components.append(temporary)
    
for i in components:
    if str(i)[0] == "V":
        voltage+=int(i[1:])#Adds everything to a value except the V
    if str(i)[0] == "R":
        resistance+=int(i[1:])#Adds everything to a value except the R
print(f"Total current in circuit is {voltage/resistance}")


