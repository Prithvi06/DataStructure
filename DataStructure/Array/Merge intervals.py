def merge(intervals):
        intervals =  sorted(intervals, key=lambda x:x[0])
        print(intervals)
        ret = []
        for i in intervals:
            newInterval = i
            #compare with the last one in ret
            if ret:
                if ret[-1][1] >= i[0]:
                    #merge and then replace the last one in ret
                    newInterval = ret.pop()
                    if i[1] > newInterval[1]:
                        newInterval[1] = i[1]
            ret.append(newInterval)
        return ret

print(merge([[2,6],[2,3],[7,9],[2,5]]))