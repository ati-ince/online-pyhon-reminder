## lambda, map and filter 

# MAP
def square(num):
    return num**2

nums = [1,2,3,4,5]
result = map(square, nums)

print(list(result))

def filt(num):
    return num%2 == 0

fresult = filter(filt, nums)

print(list(fresult))   

result2 = map(lambda num:num**2, nums)
print(list(result2))

fn = lambda x:x%2

print(fn(2), fn(3))