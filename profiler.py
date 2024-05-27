from ydata_profiling import ProfileReport

def generate_profile_report(df):
    pr = ProfileReport(df.to_pandas(), explorative=True)
    return pr
