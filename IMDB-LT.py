import pandas as pd

# 读取IMDB数据集
df = pd.read_csv('IMDB Dataset.csv')

# 统计正向情绪和负向情绪的数量
positive_count = df[df['sentiment'] == 'positive'].shape[0]
negative_count = df[df['sentiment'] == 'negavtive'].shape[0]

# 构建不平衡数据集
head_samples = df[df['sentiment'] == 'positive'].head(100)
tail_samples = df[df['sentiment'] == 'negative'].tail(1)

# 计算剩余样本的数量，使得正向样本数量与负向样本数量比例为100:1
remaining_ratio = 100
remaining_positive_count = remaining_ratio * tail_samples.shape[0]
remaining_negative_count = tail_samples.shape[0]

# 从正向情绪样本中选择剩余样本
remaining_positive_samples = df[df['sentiment'] == 'positive'].sample(remaining_positive_count)

# 从负向情绪样本中选择剩余样本
remaining_negative_samples = df[df['sentiment'] == 'negative'].sample(remaining_negative_count)

# 合并样本
imbalanced_dataset = pd.concat([head_samples, remaining_positive_samples, remaining_negative_samples, tail_samples])

# 打印不平衡数据集的情绪分布
print(imbalanced_dataset['sentiment'].value_counts())

# 保存不平衡数据集到新的CSV文件
imbalanced_dataset.to_csv('IMDB-LT.csv', index=False)