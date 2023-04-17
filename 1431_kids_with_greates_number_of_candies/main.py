from typing import List

def kidsWithCandies(candies: List[int], extraCandies: int) -> List[bool]:
    result = [] 
    for candies_rec in candies:
        result.append(candies_rec + extraCandies == max(candies))

    return result

def kidsWithCandies_V2(candies: List[int], extraCandies: int) -> List[bool]:
    max_candies = max(candies)
    return [True if rec+extraCandies>=max_candies else False for rec in candies]



if __name__ == "__main__":
    print(kidsWithCandies([2,3,5,1,3], 3))
    print(kidsWithCandies([4,2,1,1,2], 1))
    print(kidsWithCandies([12,1,12], 10))