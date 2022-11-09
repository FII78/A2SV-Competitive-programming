   dic={}
        arr=[]
        pt1= 0
        pt2 = 0
        
        dic = Couter
       
        for idx,value in enumerate(s):
            pt2 = max(pt2, dic[value])
            if pt2 == idx:
                arr.append(pt2 + 1 - pt1)
                pt1 = idx + 1
        
        return arr
