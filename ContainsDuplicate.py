def containsDuplicate(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    myDic = {}

    for i in range(len(nums)):
        if nums[i] in myDic:
            myDic[nums[i]] = myDic.get(nums[i]) + 1
        else:
            myDic[nums[i]] = 1
    
    for key, value in myDic.items():
        print(key, value)