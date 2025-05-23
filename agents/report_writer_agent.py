class ReportWriterAgent:
    def run(self, trends):
        with open("ai_ml_report.md", "w", encoding="utf-8") as f:
            f.write("# Top AI/ML Jobs in MENA - 23 May 2025\n\n")

            f.write("## Top 10 AI/ML Roles\n")
            for role, count in trends["top_roles"]:
                f.write(f"- {role}: {count} postings\n")

            f.write("\n## Job Location Distribution\n")
            for location, count in trends["location_distribution"]:
                f.write(f"- {location}: {count} postings\n")
