from __future__ import division
counter = 0;
# need the extra space for ensuring we aren't getting any partials
term = ' paris '
with open('AlltheWeb_2001', 'r') as file2001:
    for line in file2001:
        if term in line:
            counter += 1
            print 'found'

print '---------------' 
print 'found ' + term + ":"
print counter
print 'times... ' 
print '---------------' 
print 'percent is: ' 
# divide by 1257942 -- the total lines of the 2001 file
print counter / 1257942
print '---------------' 

