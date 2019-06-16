#
# @lc app=leetcode.cn id=155 lang=python3
#
# [155] 最小栈
#

class MinStack:
    #漫画最小栈 https://zhuanlan.zhihu.com/p/31958400
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack=[]
        #按顺序记录最小栈中最小元素，备胎。配合完成取最小值时间复杂度为O（1）
        self.tmp=[]
        self.index=-1
        self.tmpIndex=-1
        self.min=-2**31

    def push(self, x: int) -> None:
        #小于最小值则下标入备胎栈   
        self.index+=1
        if x <= self.min or not self.stack:
            self.min=x
            # self.tmpIndex+=1
            self.tmp.append(self.index)
        self.stack.append(x)
    def pop(self) -> None:
        if self.stack[self.index]==self.min:
            self.tmp.pop()
            # self.tmpIndex-=1
        self.stack.pop()
        self.index-=1
    def top(self) -> int:
        return self.stack[self.index]

    def getMin(self) -> int:
        return self.stack[self.tmp[len(self.tmp)-1]]


# # # Your MinStack object will be instantiated and called as such:
if __name__=="__main__":
    obj = MinStack()
    obj.push(-2)
    obj.pop()
    obj.push(1)
    obj.push(3)
    print(obj.top())
    print(obj.top())
    print(obj.top())
    print(obj.getMin())
    print(obj.getMin())
    print(obj.getMin())



    # obj.push(2)
    
    # print(obj.getMin())
    # obj.pop()
    # print(obj.getMin())
    
    # obj.pop()
    # param_3 = obj.top()
    # param_4 = obj.getMin()
    # print(param_3)
    # print(param_4)

