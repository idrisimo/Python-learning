# Starting number
count = 0

# checks if count is multiple of 3. if so answer will be 0
def m3(count):
   return count % 3

# checks if count is multiple of 5. if so answer will be 0
def m5(count):
   return count % 5

# main body of code.
# Count increases by 1
# each loop and checks
# if there are any multiples or either 3, 5, or 3 and 5
while count < 100:
    count += 1
    if m5(count) > 0:
        if m3(count) > 0:
            print(count)
        elif m3(count) == 0:
            print("Fizz")
    elif m5(count) == 0 and m3(count) > 0:
        print("Buzz")
    elif m5(count) == 0 and m3(count) == 0:
        print("FizzBuzz")
