def groupAnagrams(strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        myDic = {} 
        i = 0
        temp = ""
      
        for i in range(len(strs)):
            temp = "".join(sorted(strs[i]))
            if temp in myDic: 
                 myDic[temp].append(strs[i])
            else:
                 myDic[temp] =  [ strs[i] ]
        return myDic.values()


       
            
                
                
     

arr = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(arr) )