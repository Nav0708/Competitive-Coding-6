# Time Complexity : O(n!)
# Space Complexity : Auxiliary O(n) : for visited set
#Did this code successfully run on Leetcode : Yes
#Any problem you faced while coding this : No
# Three line explanation of solution in plain english:
#1. We use backtracking to generate all permutations of numbers from 1 to n.
#2. Check if the current number meets the condition of i % index == 0 or index % i == 0 which is beautiful.
#3. Visited set is used to track the numbers used and count the permutations until the index reaches n i.e all numbers are filled.

class Solution(object):
    def countArrangement(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.c=0
        visited=set()
        def helper(start,visited,n):
            #once the depth of the n is reached, i.e all the numbers are processed we have a permuation
            if start==n+1:
                #increment the count for getting a permutation and return
               self.c+=1
               return
            #the for loop runs from 1 to n+1 since perm starts from 1
            # to check if the start index can be placed in the given ith index
            for i in range(1,n+1):
                print(i,start,visited)
                #if the start index is beautiful(satisfies the condition) and is not in the visited set then add in visited and procede with next value in n
                if i not in visited and (start%i==0 or i%start==0):
                    visited.add(i)
                    #repeat for all the elements in n if it could be placed in the ith index
                    helper(start+1,visited,n)
                    #once the recursion is done remove the visited set to try other posibilites
                    visited.remove(i)
        #a start index from 1 and a set visited to avoid duplicates
        helper(1,visited,n)
        return self.c
        

        