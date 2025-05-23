from agents.web_search_agent import WebSearchAgent
from agents.data_extraction_agent import DataExtractionAgent
from agents.trend_analysis_agent import TrendAnalysisAgent
from agents.report_writer_agent import ReportWriterAgent

def main():
    search_agent = WebSearchAgent()
    extraction_agent = DataExtractionAgent()
    trend_agent = TrendAnalysisAgent()
    report_agent = ReportWriterAgent()

    jobs = search_agent.search_jobs()
    extracted = extraction_agent.extract(jobs)
    trends = trend_agent.analyze(extracted)
    report_agent.run(trends)

if __name__ == "__main__":
    main()
