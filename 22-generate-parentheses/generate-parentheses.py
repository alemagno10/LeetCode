class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res,curr = [],[]

        def backTracking(openP, closeP):
            if openP == closeP == 0:
                res.append("".join(curr))
                return
            
            if openP > 0 or openP == closeP:
                curr.append("(")
                backTracking(openP-1, closeP)
                curr.pop()
            
            if openP != closeP:
                curr.append(")")
                backTracking(openP, closeP-1)
                curr.pop()

        backTracking(n,n)
        return res










# 1 - ( 
# 2 - (()) and ()()

# if n > 1:
#     two options "(" or ")"


# par_remaing 3,3 
#     if close == open == 0:
#         res.append(curr)

#     if close = open or close == 0: 
#         just open
#     elif open == 0:   
#         just close
#     else:
#         open & close

#             ( 2,3
#     (( 1,3          () 2,2 
# ((( 0,3  (() 1,2  ()( 1,2  ()() 1,1

# 2^(2*n)