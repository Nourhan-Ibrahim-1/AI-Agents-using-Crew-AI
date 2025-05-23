class DataExtractionAgent:
    def extract(self, jobs):
       
        cleaned_jobs = []
        for job in jobs:
            if "AI" in job["title"] or "Machine Learning" in job["title"]:
                cleaned_jobs.append({
                    "title": job["title"],
                    "company": job["company"],
                    "location": job["location"]
                })
        return cleaned_jobs
