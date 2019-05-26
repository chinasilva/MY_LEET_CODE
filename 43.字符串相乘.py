#
# @lc app=leetcode.cn id=43 lang=python3
#
# [43] 字符串相乘
#
# https://leetcode-cn.com/problems/multiply-strings/description/
#
# algorithms
# Medium (38.72%)
# Total Accepted:    16.4K
# Total Submissions: 42.2K
# Testcase Example:  '"2"\n"3"'
#
# 给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。
# 
# 示例 1:
# 
# 输入: num1 = "2", num2 = "3"
# 输出: "6"
# 
# 示例 2:
# 
# 输入: num1 = "123", num2 = "456"
# 输出: "56088"
# 
# 说明：
# 
# 
# num1 和 num2 的长度小于110。
# num1 和 num2 只包含数字 0-9。
# num1 和 num2 均不以零开头，除非是数字 0 本身。
# 不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。
# 
# 
#
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        ret=  self.karatsuba(num1,num2) 
        return str(ret)
    
    #大数乘法  使用分治思路进行计算
    # 参考算法： https://blog.csdn.net/u010983881/article/details/77503519

    """Function to multiply 2 numbers in a more efficient manner than the grade school algorithm"""
    def karatsuba(self,x,y):
        if len(str(x)) == 1 or len(str(y)) == 1:
            return int(x)*int(y)
        else:
            n = max(len(str(x)),len(str(y)))
            nby2 = n // 2
            
            a = int(x) // 10**(nby2)
            b = int(x)  % 10**(nby2)
            c = int(y) // 10**(nby2)
            d = int(y)  % 10**(nby2)
            
            ac = self.karatsuba(a,c)
            bd = self.karatsuba(b,d)
            ad_plus_bc = self.karatsuba(a+b,c+d) - ac - bd
            
                # this little trick, writing n as 2*nby2 takes care of both even and odd n
            prod = ac * 10**(2*nby2) + (ad_plus_bc * 10**nby2) + bd
            return prod

if __name__ == "__main__":
    s = Solution()
    num1="123"
    num2="456"
    print(s.multiply(num1,num2))