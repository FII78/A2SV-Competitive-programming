    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
#         9 12 5 10 14 3 10
#         elem < 10 < elem
#         9 5 3 10 12 14
#         relative order should be maintained


        left = 0
        right = -1
        output = [pivot] * len(nums)
       
        
        for idx,num in enumerate(nums):
            if num < pivot:
                output[left] = num
                left += 1
            
            if nums[~idx] > pivot:
                output[right] = nums[~idx]
                right -= 1
                
        return output
