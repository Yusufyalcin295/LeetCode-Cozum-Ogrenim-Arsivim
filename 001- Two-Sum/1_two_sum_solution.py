# Soru Linki: https://leetcode.com/problems/two-sum/
# Konu: Two Sum (Easy)

from typing import List 


#İç içe iki dögü kuruyoruz ilk sayıyı alıp geri kalan tüm sayılarla toplayıp 
#hedefimize eşitse indeksleri dödürüyoruz değilse ikinci sayıyla aynı işlemleri yapıyoruz bulana kadar
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]

#