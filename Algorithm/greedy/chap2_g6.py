def solution(food_times, k):
    minus= k//len(food_times)
    index=k%len(food_times)
    plus_index=0
    for i in food_times:
        i-=minus
    for j in food_times:
        if j <=0:
            plus_index=1-j+plus_index
            
    answer=food_times[index+plus_index-1]
    return answer

    