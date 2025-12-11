class Solution:
    def intToRoman(self, num):
        # Mapping of values to Roman numerals, including subtractive forms
        val_to_roman = [
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I')
        ]
        
        res = ""
        for value, roman in val_to_roman:
            # Append as many times as we can subtract
            while num >= value:
                res += roman
                num -= value
        
        return res
        