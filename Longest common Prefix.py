class Solution:
    def longestCommonPrefix(self, string_list: List[str]) -> str:
        if len(string_list) == 0:#check for empty
            return ""#If empty return quotes
        
        length = [len(str) for str in string_list]#use string comprehension to take the length of string in the list
        max_length = max(length)
        result = ""
        
        for i in range(1, max_length+1):#for item in the range of strings we have
            common_string = string_list[0][:i]#assign the common portion of the string from initial character to the iterator
            for s in string_list:#iterate through the string list
                if s[:i] != common_string:#Check to what degree they are in common up to the iterator
                    return result
            result = common_string
        return result
