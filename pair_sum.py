#Function to find all the pairs that sum upto n

def pairsum (lis,n):
	if (len(lis)<2): print("Error")
	pair = {(x,y) for x in lis for y in lis if (x + y == n)}
	return (pair)

l = [1, 2, 3, 4, 5, 6, 7,-3, -2, -1, 0]
n = 1
ans = pairsum(l,n)
if (ans == set()):print ("No Pair Found")
else:print(ans)
