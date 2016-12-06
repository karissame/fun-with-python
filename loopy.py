print "Welcome to the python function workshop. There are many activities to choose from."
print "Select your desired activity and uncomment that section then run. I added a double hash for the actual comments so you can do this easily. Have fun!"

# #Problem 1- Using a for loop and the range function, print out the numbers between 1 and 10 inclusive, one on a line.
#
# for i in range(1, 11):
#     print i
#
# #Problem 2-Same as the previous problem, except you will prompt the user for the number to start on and the number to end on.
#
# for i in range(int(raw_input("Start from number ")),int(raw_input("End at number "))+1):
#     print i
#
# #Problem 3-Print each odd number between 1 and 10 inclusive.
# print "\nPrinting odd numbers"
# for i in range(1,11):
#     if i%2:
#         print i
#
# #Problem 4-Print a square of * characters whose dimensions are determined by the user
# n = int(raw_input("How big should our square be? "))
# for i in range(1,n+1):
#     for n in range(n, n+1):
#         print "*" * n
#
# #Problem 5-Given a height and width, input by the user, print a box consisting of * characters as its border
# w = int(raw_input("How wide should our rectangle be? "))
# h = int(raw_input("How tall should our rectangle be? "))
# for w in range(w, w+1):
#     print "*" * w
# for h in range(1,h-1):
#     print "*" + " " * (w-2) + "*"
# for w in range(w, w+1):
#     print "*" * w
#
# #Problem 6-Print a Triangle with user given height
# h = int(raw_input("How tall should our Triangle be? "))
# base= h + (h-1)
# for i in range(1,h+1):
#     print base - (i + (i-1))
#     print " " * (base - (i + (i-1))/2) + "*" * (i + i - 1) + " " * (base - (i + (i-1))/2)
#
# #Problem 7-Vertical List of all Multiplication values 1 - 10
# for v in range (1,11):
#     for k in range (1,11):
#         print v,"X",k,"=",v*k
#
# #BONUS Problem 1- Print a Banner around user string
# print "Let's make a banner"
# bannerText = raw_input('Input a short message ')
# while len(bannerText) > 60:
#     print "You're message is too long."
#     bannerText = raw_input('Input a short message ')
#
# print "*" * (len(bannerText)+4)
# print "* ",bannerText," *"
# print "*" * (len(bannerText)+4)
#
# #BONUS Problem 2- Print the first 100 Triangle numbers
#
# for n in range (1,101):
#     print n*(n+1)/2
#
# #BONUS Problem 3- Factor a number. List factors for a given number.
# #IMPORTANT! I went beyond the req and only list the prime factors =D
# numToFactor = int(raw_input("Provide a number and I will give you its factors "))
# def isPrime(Number):
#     return 2 in [Number,2**Number%Number]
#
# for i in range (1,numToFactor + 1):
#     if numToFactor%i == 0:
#         if isPrime(i):
#             print i
