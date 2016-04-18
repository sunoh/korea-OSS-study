s ='sadfasdgjlsdkjfeijx'

count = 0

for letter in s:
    if letter in 'aeiou':
        count +=1

print "Number of vowels: " + str(count)

