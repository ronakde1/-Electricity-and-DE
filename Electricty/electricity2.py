voltage=0
resistance=0
#components=input("please input the components in sequential order and put | between series components ")
components="R10|V10|PR10PR10R10|PR20PR15PR10R5"
components_circuit = components.split("|")

print(components_circuit)

for i in components_circuit:
    
    if str(i)[0] == "V":
        voltage+=int(i[1:])
    if str(i)[0] == "R":
        resistance+=int(i[1:])
    if i[0] == "P":
        array=i[1:].split("P") #Removes the first P and splits it into an array with each element where it used to be a P (so "PaPbPc"=[a,b,c]).i[1:] keeps everything in the list from element 1
        array2=[]
        array3=[]
        for i in array:#[R20R30,R40]
            array2=i[1:].split("R") #[R20R30]->[20,30]
            temp=0
            for a in array2: 
                temp+=int(a) #20+30

            temp=temp**(-1) 
            array3.append(temp)
        temp=0
        for i in array3:
            temp+=i
        resistance+=temp**(-1)

print(f"Total resistance in circuit is {resistance}")
print(f"Total current in circuit is {voltage/resistance}")
print(f"Total power dissapated in circuit is {(voltage**2)/resistance}")


#---------------------------------------------------------------------------------------
    #if i[0]=="R":
        #temp=int(i[1:])
        #temp=temp**(-1)
        #array2.append(temp)
#for i in array2:
    #resistance+=i
#--------------------------
#print(components_circuit)

#print(type(2))
#if type(2)== "<class 'int'>":
    #print("hi")
#-----------------------