# 使用LR对手写数字分类
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_digits
from sklearn.linear_model import LogisticRegression
# 加载数据
digits = load_digits()
data = digits.data
# 分割数据，将25%的数据作为测试集，其余作为训练集
train_x, test_x, train_y, test_y = train_test_split(
    data, digits.target, test_size=0.25, random_state=33)
# 采用Z-Score规范化（）
# 生成一个规划化的转换器
ss = preprocessing.StandardScaler()
# 将训练集数据进行规划化
train_ss_x = ss.fit_transform(train_x)
# 将测试集数据进行规范化
test_ss_x = ss.transform(test_x)
# 创建LR分类器
lr = LogisticRegression()
lr.fit(train_ss_x, train_y)
predict_y = lr.predict(test_ss_x)
print('LR准确率: %0.4lf' % accuracy_score(test_y, predict_y))
