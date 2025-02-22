class mergeSortedArrays():
    def merge(nums1, m, nums2, n):
        i = m - 1  # Pointer for nums1
        j = n - 1  # Pointer for nums2
        k = m + n - 1  # Pointer for the merged result

        # Merge from the end
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # Copy remaining elements from nums2 if any
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

    if __name__ == "__main__":
        nums1 = [1, 2, 3, 0, 0, 0]
        m = 3
        nums2 = [2, 5, 6]
        n = 3
        print(merge(nums1, m, nums2, n))


