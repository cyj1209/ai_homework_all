from efficient_apriori import apriori

transactions = [
    ('牛奶', '面包', '尿布'),
    ('可乐', '面包', '尿布', '啤酒'),
    ('牛奶', '尿布', '啤酒', '鸡蛋'),
    ('面包', '牛奶', '尿布', '啤酒'),
    ('面包', '牛奶', '尿布', '可乐')]
itemsets, rules = apriori(transactions, min_support=0.5, min_confidence=1)
print(itemsets, '\n', rules)
