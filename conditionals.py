# set up a variable, check its value, and choose path to follow based on that condition
temperature = int(input("input a value between 0 and 100: "))

#compare that number with the following conditions: 

if (temperature <= 4):
    #water is frozen
    print("water's state is soldi (ice)")
elif (temperature <100):
    #water is liquid 
    print("water's state is liquid")
else:
    #water is boiling so it's steam
    print("water is vapor")
