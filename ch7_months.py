months = "JanFebMarAprMayJunJulAugSepOctNovDec"

n = int(input("Enter a month number: "))

start_index = 3*(n - 1)
print(months[start_index:start_index + 3])
