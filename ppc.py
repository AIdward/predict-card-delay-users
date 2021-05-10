def missing_plot(df):
    missing = df.isnull().sum()
    missing = missing[missing > 0] 
    missing.sort_values(inplace=True) 
    return missing.plot.bar(figsize = (12,6))


def null(df):
    return df.isnull().sum()[df.isnull().sum().values > 0]