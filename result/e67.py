'''题目：输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组。'''

array_ = [2, 1, 56, 23, 64]
print(array_)



m = max(array_)
m_i = array_.index(m)

array_[m_i], array_[0] = array_[0], array_[m_i]

n = min(array_)
n_i = array_.index(n)

array_[n_i], array_[-1] = array_[-1], array_[n_i]


print(array_)
