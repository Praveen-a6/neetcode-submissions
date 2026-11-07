class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_so_far = -1
        
        # Traverse the array from right to left
        for i in range(len(arr) - 1, -1, -1):
            current = arr[i]
            arr[i] = max_so_far
            max_so_far = max(max_so_far, current)
            
        return arr