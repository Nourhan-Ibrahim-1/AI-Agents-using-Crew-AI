import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_jobs_from_wuzzuf(pages=1, query="AI"):
    base_url = "https://wuzzuf.net/search/jobs/?a=spbg&q="
    jobs_data = []

    for page in range(pages):
        url = f"{base_url}{query}&start={page}"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")

        job_cards = soup.find_all("div", {"class": "css-1gatmva e1v1l3u10"})  # قالب كروت الوظائف

        for job in job_cards:
            title = job.find("h2", {"class": "css-m604qf"}).text.strip() if job.find("h2", {"class": "css-m604qf"}) else "N/A"
            company = job.find("a", {"class": "css-17s97q8"}).text.strip() if job.find("a", {"class": "css-17s97q8"}) else "N/A"
            location = job.find("span", {"class": "css-5wys0k"}).text.strip() if job.find("span", {"class": "css-5wys0k"}) else "N/A"

            jobs_data.append({
                "title": title,
                "company": company,
                "location": location
            })

    return pd.DataFrame(jobs_data)


df = get_jobs_from_wuzzuf(pages=2, query="machine learning")
print(df.head())
df.to_csv("wuzzuf_ai_jobs.csv", index=False)
