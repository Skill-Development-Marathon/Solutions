def ss(candies, extraCandies):
    max_candy = max(candies)

    li = []
    for candy in candies:
        if candy + extraCandies >= max_candy:
            li.append(True)
        else:
            li.append(False)
    return li

ss([2,3,5,1,3],3)