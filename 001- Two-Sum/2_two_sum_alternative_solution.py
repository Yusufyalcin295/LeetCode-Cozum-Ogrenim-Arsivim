from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Değer : İndeks şeklinde saklayacağımız boş bir sözlük
        seen = {} 
        
        for i, n in enumerate(nums):
            diff = target - n
            # Aradığımız fark sözlükte var mı?
            if diff in seen:
                # Varsa, o sayının indeksi ve şu anki indeks cevaptır
                return [seen[diff], i]
            # Yoksa, şu anki sayıyı ve indeksini sözlüğe ekle
            seen[n] = i 
#