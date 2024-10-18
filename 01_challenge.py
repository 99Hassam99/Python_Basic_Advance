# write a python func to find all the prime factors.
# input: integer value
# Output: list of prime factors
# get_prime_factors(630) = [2,3,3,5,7]
# 2x3x3x5x7 = 630
# [13] = 13

# from factors import get_prime_factors
def get_prime_factors(number):
    factors=[]
    divisor=2
    while divisor<=number:
        if number% divisor==0:
            factors.append(divisor)
            number=number//divisor
        else:
            divisor+=1
    return factors

# print(get_prime_factors(630))
# print(get_prime_factors(13))