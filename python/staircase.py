#  There's a staircase with N steps, and you can climb 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

# For example, if N is 4, then there are 5 unique ways:

#     1, 1, 1, 1
#     2, 1, 1
#     1, 2, 1
#     1, 1, 2
#     2, 2

# What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time. Generalize your function to take in X. 
def stairs(num_of_setps, possible_steps, steps_so_far, answers_found)->list:
    sum_of_steps_so_far=0
    if steps_so_far!=[]:
        sum_of_steps_so_far=sum(steps_so_far)
    if sum_of_steps_so_far==num_of_setps:
        return steps_so_far
    if sum_of_steps_so_far>num_of_setps:
        return []
    else:
        for step in possible_steps:
            answers_found.append(stairs(num_of_setps=num_of_setps, possible_steps=possible_steps, steps_so_far=steps_so_far+[step], answers_found=answers_found))
    return answers_found
    
def start_function(possible_steps, num_of_steps, steps_so_far=[])->list[list]:
    result=[]
    for step in possible_steps:
        result.append(stairs(num_of_setps=num_of_steps,possible_steps=possible_steps, steps_so_far=steps_so_far+[step], answers_found=[]))
    return list(filter(lambda x: x!=[],result))

def test():
    pass

if __name__=='__main__':
    print(start_function(possible_steps=[1,2],num_of_steps=4,steps_so_far=[]))
