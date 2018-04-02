"""

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

"""

class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        
        if not s or not numRows:
            return s
        
        if numRows == 1:
            return s
        
        lines = [""] * numRows
        
        for i in range(len(s)):
            index = i % (2*(numRows-1))
            if index < numRows:
                lines[index] += s[i]
            else:
                lines[2*numRows-index-2] += s[i]
            
        return "".join(lines)