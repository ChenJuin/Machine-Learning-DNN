import pandas as pd
import random

# 读取IMDB数据集
df = pd.read_csv('IMDB Dataset.csv')

# 获取类别列表
categories = df['sentiment'].unique()

# 定义标签翻转概率
flip_probability = 0.2 / (len(categories) - 1)

# 遍历每个样本，随机翻转标签
noisy_labels = []
for index, row in df.iterrows():
    sentiment = row['sentiment']
    
    # 随机选择是否翻转标签
    if random.random() < flip_probability:
        # 随机选择一个不同于当前标签的新标签
        new_sentiment = random.choice([category for category in categories if category != sentiment])
        noisy_labels.append(new_sentiment)
    else:
        noisy_labels.append(sentiment)

# 创建带有噪声标签的数据集
noisy_dataset = df.copy()
noisy_dataset['sentiment'] = noisy_labels

# 打印噪声标签数据集的情绪分布
print(noisy_dataset['sentiment'].value_counts())

# 保存噪声标签数据集到新的CSV文件
noisy_dataset.to_csv('IMDB-NY.csv', index=False)