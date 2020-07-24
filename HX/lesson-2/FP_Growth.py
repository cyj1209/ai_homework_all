from pyspark.ml.fpm import FPGrowth

# df = spark.createDataFrame([
#     (0, [1, 2, 5]),
#     (1, [1, 2, 3, 5]),
#     (2, [1, 2])
# ], ["id", "items"])

df = [
    ('牛奶', '面包', '尿布'),
    ('可乐', '面包', '尿布', '啤酒'),
    ('牛奶', '尿布', '啤酒', '鸡蛋'),
    ('面包', '牛奶', '尿布', '啤酒'),
    ('面包', '牛奶', '尿布', '可乐')]

fpGrowth = FPGrowth( minSupport=0.5, minConfidence=0.6)
model = fpGrowth.fit(df)

# Display frequent itemsets.
model.freqItemsets.show()

# Display generated association rules.
model.associationRules.show()

# transform examines the input items against all the association rules and summarize the
# consequents as prediction
model.transform(df).show()