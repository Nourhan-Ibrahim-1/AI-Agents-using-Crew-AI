import pandas as pd

class WebSearchAgent:
    def search_jobs(self):
        df = pd.read_csv("wuzzuf_ai_jobs.csv")
        jobs = df.to_dict(orient="records")
        return jobs
