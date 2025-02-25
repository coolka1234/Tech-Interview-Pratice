# There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

# You are giving candies to these children subjected to the following requirements:

#     Each child must have at least one candy.
#     Children with a higher rating get more candies than their neighbors.

# Return the minimum number of candies you need to have to distribute the candies to the children.

def distribute_candy(children_ratings)->int:
    if(len(children_ratings)==1):
        return 1
    prev_child=0
    prev_child_reward=0
    total_candies=0
    first_child=False
    i=0
    for child, i in enumerate(children_ratings, i):
        current_handout=0
        if first_child:
            if(children_ratings[0]>children_ratings[1]):
                current_handout=2
                total_candies+=2
        if i+1<len(children_ratings):
            if child>prev_child and child>children_ratings[i+1]:
               total_candies+=prev_child_reward+1
               current_handout=prev_child_reward+1
            else:
                total_candies+=1
                current_handout=1
        elif child>prev_child:
            total_candies+=prev_child_reward+1
            current_handout=prev_child_reward+1
        else:
            total_candies+=1
            current_handout=1
        prev_child_reward=current_handout
        print(f"{i} handout {current_handout}")
    return total_candies
            
        

if __name__=='__main__':
    children_ratings=[1, 0, 2]
    print(distribute_candy(children_ratings=children_ratings))

 
