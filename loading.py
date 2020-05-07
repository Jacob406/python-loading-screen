import time

stars = []
task_complete = False

while task_complete == False:
    time.sleep(0.25)
    print("\n" * 49)
    
    if len(stars) <= 2:
        stars.append(".")
        print("loading" + str(''.join(stars)))        

    else:
        del stars[:]
        print("loading " + str(''.join(stars)))
        
        
        


    
  

    

    
