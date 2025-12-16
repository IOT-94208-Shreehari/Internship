l1 = [105,110,108,112,115,116,114]

#three day rolling avg 
rolling_avg = [
   round(sum(l1[i:i+3]) / 3,2)
    for i in range(len(l1) - 2)
]
print(rolling_avg)
