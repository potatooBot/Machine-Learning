import numpy as np
import math
def gradient_descent(x,y):
    n=len(x)
    iteration=10000
    m_curr=b_curr=0
    learning_rate=0.00024
    cost_result=0
    for i in range(iteration):
        y_predict=m_curr*x +b_curr
        cost=(1/n)*sum([val**2 for val in (y-y_predict)])
        md=-(2/n)*sum(x*(y-y_predict))
        bd=-(2/n)*sum(y-y_predict)
        m_curr=m_curr-learning_rate*md
        b_curr=b_curr-learning_rate*bd
        # print("m {}, b{} ,cost {},iteration {}".format(m_curr,b_curr,cost,i))
        if(math.isclose(cost,cost_result,rel_tol=1e-20)):
            print("Cost Almost Matched with Iteration and m is :{} and b is {}",iteration,m_curr,b_curr)
            break
        else:
            cost_result=cost
            
          

x=np.array([92,56,88,70,80,49,65,35,66,67])
y=np.array([98,68,81,80,83,52,66,30,68,73])
gradient_descent(x,y)

