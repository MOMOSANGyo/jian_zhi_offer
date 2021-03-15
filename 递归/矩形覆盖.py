# -*- coding:utf-8 -*-
# -*- coding:utf-8 -*-
# 一共有n个方块，要么是在n-1方块的情况下竖着加1个，要么是在n-2个方块的情况下横着加两个
class Solution:
    def rectCover(self, number):
        # write code here
        results=list(range(number+1))
        for i in range(number+1):
            if i <=2:
                results[i]=i
            else:
                results[i]=results[i-2]+results[i-1]
        return results[-1]





if __name__ == '__main__':
    ss = Solution()
    print(ss.rectCover(4))