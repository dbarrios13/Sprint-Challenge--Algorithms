#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
 I would have to say that this pseudocode would be a O(2^n) because if n results to be a positive integer the while loop will never stop because in the condition n will always be greater than a resulting in a endless loop. 

b)
 this one was a bit harder to analyze. from my understanding
    1: 1
    2: n + 1
    3: n
    4: n + 1
    5: 2^n
    6: n
    Above are the calculations that I was able to come up with, hopefully correct. adding them up
    you get 2^n + 4n + 3 now we can short this down to 2^n + n by removing the constants. that being said the runtime could be either O(2^n), which is a horrible runtime or it could be O(n log n) which is a bad runtime. Best case scenario O(n) depending on n

c)
 Best case the runtime would be O(1) because of the if statement and worst case the runtime would be O(n) because it will run n number of times until it reaches 0
## Exercise II

For this scenario there are a lot of factors to consider. First thing would be in order to determine the value of f based on the number of stories the building has we would have to decide if we are taking a certain fraction of the n-stories and using that to calculate f. The scenario itself for me, is difficult for me to come up with a solution just because how can we say the egg won't break at a certain floor depending on the stories. In other word, let says we take a fraction of the stories and use that to determine f. For example,

n = stories the building has
then we decide to use 1/3 of the stories to find f
 
import math

def finding_f (n):
    if n == 1:
        print('the eggs won't break')
    else:
        f = math.floor(n * 1/3)
        print(f'If an egg is dropped on {f} or below it won't break') 
        
so unless we have access to data statistics that we can use to determine how to factor the floor which would be the highest to drop the egg from then I can not think right now of another way to determine the floor unless with set a certain number to calculate. 