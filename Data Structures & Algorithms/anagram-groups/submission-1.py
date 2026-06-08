class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapp = {} #mapping char count of each string into an array and using the array as key in hashmap

        #make a new list for each string
        for each in strs : 
            #the list we will use. Changes for every word
            arr = [0] * 26
            
            #go through all the characters in each word 
            for chars in each: 
                #ord char - ord "a" effectively finds which number in the alphabet each character is. 
                arr[ord(chars)-ord("a")] += 1

            if tuple(arr) in mapp:
                mapp[tuple(arr)].append(each)
            else:
                mapp[tuple(arr)] = [each]
        
        return list(mapp.values())