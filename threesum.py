class threeSum:
    # Find all sets of 3 ints that add to 0
    def function(self, nums):
        answer = []
        nums.sort()

        for i in range(len(nums)):
            # Remove duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # a + b  = -c, define our -c
            c = nums[i] * (-1)

            a = i + 1
            b = len(nums) - 1

            while(a < b):
                if((nums[a] + nums[b]) == c):
                    answer.append([nums[c], nums[a], nums[b]])
                    a = a + 1
                    # Skip past duplicates
                    while a<b and nums[a] == nums[a-1]:
                        a = a + 1
                elif((nums[a] + nums[b]) < c):
                    # Sum is too small, need to slide a value up
                    a = a + 1
                else:
                    # Sum too large, slide b down
                    b = b - 1
            
        return answer

