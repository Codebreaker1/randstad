from collections import deque
import datetime
import time



Keys = [i for i in range(7)]     # Total Entries
sites = ['www.google.com', 'www.yahoo.com', 'www.goal.com','www.google.com','www.mozilla.com',
         'www.amazon.com', 'www.Ebay.com', ]


size=5
dq=deque()
seen=dict()

print('_'*30)
# checking sites and updated time with max limit of 5
for i, key in enumerate(Keys):

    web=sites[key]
    if web in seen:
        temp=({web:currentDT.strftime("%Y-%m-%d %H:%M:%S")})
        seen.update(temp)
        continue
    else:
        if len(dq)<size:
            currentDT = datetime.datetime.now()

            dq.appendleft(sites[key])
            seen.update({sites[key]:currentDT.strftime("%Y-%m-%d %H:%M:%S")})
        else:
            dq.pop()
            dq.appendleft(sites[key])
            seen.update({sites[key]: currentDT.strftime("%Y-%m-%d %H:%M:%S")})

    #print seen
    #print web


print dq
print seen
#print sites[1] in seen