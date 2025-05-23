from collections import Counter

class TrendAnalysisAgent:
    def analyze(self, jobs):
        titles = [job["title"] for job in jobs]
        locations = [job["location"] for job in jobs]

        top_roles = Counter(titles).most_common(10)
        location_dist = Counter(locations).most_common()

        return {
            "top_roles": top_roles,
            "location_distribution": location_dist
        }
