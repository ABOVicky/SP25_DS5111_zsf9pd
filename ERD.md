# Lab 08: ERD Design for Gainers Data Pipeline

##  Purpose
This ERD models the process of transforming raw gainer CSV data (collected by cron from Yahoo and WSJ) into structured intermediate and final tables for analysis. The end goal is to answer business-relevant questions using SQL transformations in Snowflake.

---

##  Use Cases

1. **Recurring Symbols**
   Identify which stock symbols appear multiple times during the week across gainer lists, and from which sources (Yahoo, WSJ).

2. **Price Distribution**
   Analyze the price distribution of all gainer stocks during the week by segmenting them into price ranges.

---

## Methods
- Raw data comes from timestamped CSVs collected via cron jobs (e.g., `yahoo_gainers_2025-04-01_09-31.csv`).
- CSVs are loaded into a **raw_gainers** table with fields:
  - `symbol`, `price`, `source`, `scrape_time`
- SQL in DBT transforms this data into:
  - An **intermediate table** that aggregates gainers by symbol and source.
  - A **histogram table** that buckets prices by defined ranges.
- These intermediate tables are then used to create **final summary tables**.

---

## Summary
This ERD successfully outlines the data transformation process from raw gainer CSVs to meaningful, queryable tables for analysis. It supports key use cases like identifying frequently appearing symbols and understanding price distribution patterns across the week. While the current structure answers core questions, additional tables incorporating volume, candlestick trends, or cross-source overlaps (Yahoo vs WSJ) could enrich future analysis. Overall, the model provides a clear and scalable foundation to support deeper insights into daily stock gainer activity.


---

## ER Diagram (Mermaid.js)

```mermaid
erDiagram
    raw_gainers {
        string symbol
        float price
        string source
        datetime scrape_time
    }

    gainers_summary {
        string symbol
        int appearances
        datetime first_seen
        datetime last_seen
        string sources
    }

    price_distribution {
        string price_range
        int count
    }

    raw_gainers ||--o{ gainers_summary : aggregates
    raw_gainers ||--o{ price_distribution : buckets
