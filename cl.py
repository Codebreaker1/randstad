x1=input('x1 ')
x2=input('x2 ')
y1=input('y1 ')
y2=input('y2 ')

xmax=max(x1,x2)
xmin=min(x1,x2)
ymax=max(y1,y2)
ymin=min(y1,y2)

if xmax >=ymin & ymax>=xmin:
    print 'the axis overlaps'
else:
    print 'It does not overlap'

