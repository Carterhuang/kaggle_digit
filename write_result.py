with open('result.csv', 'w') as result:
    result.write('ImageId,Label\n')

    for i in xrange(28000):
        result.write('%s,%s\n'%(str(i+1), "1"))
