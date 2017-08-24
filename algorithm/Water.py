#! /usr/bin/env python
#from operator import

# Utility function to return GCD of 'a'  and 'b'.
def gcd(m, n):
    if n == 0:
        return m
    return gcd(n, m%n)

def pour(fromCap, toCap, d):
    """
    fromCap -- Capacity of jug from which
              water is poured
    toCap   -- Capacity of jug to which
              water is poured
    d       -- Amount to be measured
    """

    # Initialize current amount of water
    # in source and destination jugs
    from_tmp = fromCap
    to_tmp = 0
    #Initialize count of steps required
    step = 1                                       # Needed to fill "from" Jug
    #Break the loop when either of the two
    # jugs has d litre water
    while (from_tmp != d and to_tmp != d):
        # Find the maximum amount that can be
        # poured
        temp = min(from_tmp, toCap - to_tmp)
        print "step %s and the tmp value %s" % (step, temp)
        # Pour "temp" litres from "from" to "to"
        to_tmp   += temp
        from_tmp -= temp
        # Increment count of steps
        step+=1
        if (from_tmp == d or to_tmp == d):
            break
        # If first jug becomes empty, fill it
        if (from_tmp == 0):
            from_tmp = fromCap
            step+=1
        # If second jug becomes full, empty it
        if (to_tmp == toCap):
            to_tmp = 0
            step += 1
    print "The value of %s" % step
    return step


# Returns count of minimum steps needed to
# measure d litre
def minSteps( m,  n,  d):
    #import ipdb; ipdb.set_trace()
    # To make sure that m is smaller than n
    if (m > n):
        m, n = n, m
    # For d > n we cant measure the water
    # using the jugs
    if (d > n):
        return -1
    # If gcd of n and m does not divide d
    # then solution is not possible
    if (d % gcd(n, m)) !=0:
        return -1
    # Return minimum two cases:
    # a) Water of n litre jug is poured into
    #    m litre jug
    # b) Vice versa of "a"

    return min(pour(n, m, d),pour(m, n, d))

if __name__ == '__main__':
    n = 3; m = 5; d = 4
    print ("Minimum number of steps required is %d",
           minSteps(m, n, d))