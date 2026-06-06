from feature_fetcher import get_customer_feature

df = get_customer_feature(100002)
print("Shape:", df.shape)
print(df.head())