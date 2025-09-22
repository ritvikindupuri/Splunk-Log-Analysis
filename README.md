# Splunk SIEM: SOC Analyst Threat Hunt & Log Analysis

This project demonstrates a comprehensive security analysis within a Splunk Cloud environment built from scratch. Acting as a SOC Tier-1 Analyst, I ingested and analyzed over 100,000 events from the "Buttercup Games" e-commerce dataset to perform two distinct investigations: a security-focused **threat hunt** for a potential brute-force attack and an operations-focused **web traffic analysis**.

---
## Investigation 1: Threat Hunting for Brute-Force Activity

The primary security objective was to identify unauthorized access attempts against critical infrastructure within the simulated environment.

### Methodology
I used Splunk's Search Processing Language (SPL) to systematically filter the log data. The hunt began with broad queries and was progressively narrowed down using host, source, and keyword filters to isolate suspicious events. The investigation focused on identifying patterns of failed logins, a key indicator of a brute-force attack.

### Findings & Visualization
The investigation successfully identified over **100 failed SSH login attempts** for the `root` account targeting the `mail.sv` host. The `secure.log` was isolated as the primary data source. By creating a timechart visualization, I was able to observe the pattern of failed attempts over time, confirming a concentrated brute-force attempt.

<img src="./assets/Failed Login attempts overtime.jpg" width="800" alt="Timechart showing a spike in failed login attempts">
*<p align="center">Figure 1: Visualizing the brute-force attack timeline with a spike in failed root logins.</p>*

---
## Investigation 2: Web Traffic & Operational Analysis

To demonstrate versatility, I conducted a secondary analysis on the web access logs from the same dataset. This involved identifying operational issues and potential sources of malicious web scanning.

### HTTP Error Analysis
By filtering for HTTP 4xx/5xx status codes, I was able to identify which pages were generating "Not Found" errors and which user agents (clients/bots) were responsible for the highest volume of these errors. This type of analysis is crucial for both identifying broken links and detecting scanners looking for vulnerabilities.

<img src="./assets/HTTP 404 Errors.jpg" width="800" alt="Chart of HTTP 404 errors by page">
*<p align="center">Figure 2: Identifying the most common pages resulting in a 404 "Not Found" error.</p>*

<br>

<img src="./assets/Top User Agents Generating HTTP Errors.jpg" width="800" alt="Chart of top user agents causing errors">
*<p align="center">Figure 3: Isolating the top user agents responsible for generating HTTP errors.</p>*

### Business Intelligence
The same SIEM data can be pivoted to provide business insights. I queried the dataset for vendor sales logs to identify trends and top-performing vendors within the e-commerce platform.

<img src="./assets/Event Log of vendor sales.jpg" width="800" alt="Table showing a log of vendor sales events">
*<p align="center">Figure 4: Using Splunk to analyze and display raw vendor sales transaction data.</p>*

---
## 🚀 Skills & Technologies Demonstrated

* **SIEM Administration:** Splunk Cloud configuration, data ingestion, and index management.
* **Splunk Processing Language (SPL):** Writing complex queries for searching, filtering, and correlating log data.
* **Threat Hunting:** Proactively searching for indicators of compromise (IoCs) and attacker TTPs.
* **Log Analysis:** Parsing and interpreting diverse log sources (e.g., `secure.log`, web access logs).
* **Incident Investigation:** Following a methodical process to identify and analyze a security event.
* **Data Visualization:** Creating charts and dashboards in Splunk to generate actionable insights.
