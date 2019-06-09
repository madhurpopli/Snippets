# coalesce two columns
df['a'] = df.a.combine_first(df.b)
