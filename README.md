# Titanic Survival Data Dashboard

An interactive web dashboard for exploring Titanic passenger data, built with Python and Streamlit.

---

## Overview

This project provides a dynamic dashboard to analyze survival patterns among Titanic passengers. Users can filter data by gender, age, and passenger class, and view real-time visualizations of survival rates and demographic breakdowns.

**App Link:**  
[https://ncthang17.streamlit.app/](https://ncthang17.streamlit.app/)

---

## Features

- **Interactive Filters:**  
  - Filter passengers by gender, passenger class, and age range.
- **Data Visualization:**  
  - Survivor vs. non-survivor count.
  - Survival rate by gender.
  - Survival rate by passenger class.
- **Filtered Data Preview:**  
  - View a preview of the filtered dataset.
- **User Experience:**  
  - Wide layout for optimal viewing.
  - Background music for enhanced experience.

---

## Screenshots

*Replace with your own screenshots if desired.*

---

## Installation

1. **Clone the repository:**
git clone https://github.com/your-username/titanic-dashboard.git
cd titanic-dashboard

2. **Install dependencies:**

also please write me a readme.md on github thank you so much.
How i add this into my data analysis portoflio? i mean i dont know how to explain
To add your web scraping and data analysis project using jobKorea_data_6.py and jobKorea_sales_dynamic_2.py to your portfolio, you should structure your explanation in a clear, concise, and professional way. Here’s how you can do it, step by step:

1. Project Title and Overview
Start with a brief title and summary. For example:

Project Title:
JobKorea Enterprise Data Scraper and Analysis

Overview:
Developed a Python-based web scraper to collect detailed company information from JobKorea for a curated list of enterprises. The project demonstrates skills in data collection, cleaning, and basic analysis.

2. Problem Statement
Explain the business or analytical problem you addressed:

Problem:
There was a need to collect structured data about companies (such as capital, sales, CEO, and foundation date) from JobKorea for a specific subset of enterprises, which could be used for market research, sales targeting, or business intelligence.

3. Solution and Process
Describe what you did and how you did it, highlighting your technical approach:

Solution:

Data Collection: Used Python with requests and BeautifulSoup to scrape company details from JobKorea’s search results and company profile pages.

Data Extraction: Extracted key fields (capital, sales, CEO, foundation date) from each company’s profile using targeted HTML parsing.

Data Cleaning: Ensured only companies with sufficient metadata were included in the final dataset.

Automation: Applied polite scraping practices (random delays between requests) to avoid overloading the website.

Output: Saved the collected data into a clean CSV file for further analysis.

4. Tools and Technologies
List the main technologies and libraries you used:

Python

Pandas (for data manipulation)

BeautifulSoup (for HTML parsing)

Requests (for HTTP requests)

5. Key Challenges and Solutions
Highlight any challenges you faced and how you overcame them:

Challenges:

Website Structure Changes: The scraper had to adapt to different HTML layouts for company profiles.

Missing Data: Some profiles lacked required metadata, so the code skipped incomplete records.

Rate Limiting: Implemented random delays to avoid being blocked by the website.

6. Results and Insights
Summarize the outcome and what you learned:

Results:
Successfully collected and structured data for hundreds of companies, ready for further analysis or integration into business workflows.

Insights:
Demonstrated the ability to automate data collection from real-world websites and prepare data for analysis, which is a core skill for data analysts and business intelligence professionals.

7. How to Present in Your Portfolio
Follow these best practices for presenting your project:

Use a project page or case study format: Include a brief introduction, problem, solution, tools, challenges, and results.

Show your code: Provide a link to your GitHub repository with the scripts and a README explaining the project.

Visuals: If possible, add screenshots of your output or data structure.

Reflect on learnings: Briefly mention what you learned or would do differently next time.

Example Project Description (Short Version)
JobKorea Enterprise Data Scraper

Collected structured company data from JobKorea using Python, BeautifulSoup, and Pandas. The project involved scraping company profiles, extracting key metrics (capital, sales, CEO, foundation date), and saving the results for analysis. Demonstrated skills in web scraping, data cleaning, and automation.

Tools: Python, Pandas, BeautifulSoup, Requests
Key Challenges: Adapting to website changes, handling missing data, rate limiting
Result: Clean, structured dataset for further business intelligence tasks.

8. Next Steps
Consider expanding your project by:

Analyzing the collected data (e.g., summary statistics, trends by industry or region)

Creating visualizations (e.g., charts or dashboards)

Automating regular updates (scheduled scraping)

By following this structure, you will clearly communicate your skills and the value of your project to potential employers or clients.

then write for me please.
Certainly! Here’s a ready-to-use portfolio description for your project, based on your code and the context you provided:

JobKorea Enterprise Data Scraper and Analysis
Project Overview

This project automates the collection and structuring of company data from JobKorea, one of South Korea’s largest job and company information portals. The goal was to extract detailed information—such as capital, sales, CEO, foundation date, industry, and location—for a curated list of enterprises, enabling further business intelligence and market analysis.

Problem Statement

Manually gathering company metadata from hundreds of enterprise profiles is time-consuming and error-prone. There was a need for an automated solution to collect, clean, and organize this data efficiently.

Solution and Process

Data Collection:

Used Python with the requests library to fetch company search results and detailed profile pages from JobKorea.

Employed BeautifulSoup for HTML parsing to extract relevant information from each company’s profile.

Data Extraction:

Targeted specific fields including:

기업명 (Company Name)

기업형태 (Company Type)

지역 (Location)

업종 (Industry)

자본금 (Capital)

매출액 (Sales)

대표자 (CEO)

설립일 (Foundation Date)

Implemented logic to skip incomplete records and adapt to varying HTML structures.

Automation and Politeness:

Added random delays between requests to avoid overloading the website and reduce the risk of being blocked.

Data Output:

Saved the collected and cleaned data into a structured CSV file for easy analysis and integration with other tools.

Tools and Technologies

Python

Pandas (for data manipulation and CSV output)

BeautifulSoup (for HTML parsing)

Requests (for HTTP requests)

urllib.parse (for URL encoding)

Key Challenges and Solutions

Website Structure Variability:

The scraper was designed to handle different HTML layouts, ensuring robust data extraction across various company profiles.

Missing or Incomplete Data:

Logic was implemented to skip companies with insufficient metadata, ensuring only reliable data was included in the final output.

Rate Limiting:

Random delays between requests were introduced to maintain polite scraping practices and avoid being blocked by the website.

Results and Insights

Successfully collected and structured data for hundreds of companies, ready for further analysis or business intelligence tasks.

Demonstrated proficiency in web scraping, data cleaning, and automation—core skills for modern data analysis and business intelligence roles.

How to Present in Your Portfolio

Project Title: JobKorea Enterprise Data Scraper

Description:

Automated the collection and structuring of company data from JobKorea using Python, BeautifulSoup, and Pandas. Extracted key metrics such as capital, sales, CEO, and foundation date for a curated list of enterprises. Demonstrated skills in web scraping, data cleaning, and automation.

Tools: Python, Pandas, BeautifulSoup, Requests

Key Challenges: Adapting to website changes, handling missing data, rate limiting

Result: Clean, structured dataset for business intelligence and market research

You can copy the above directly into your portfolio, adjusting details as needed for your personal style or specific use case.

what data skills here? data analyis or data cleaning? data engineer?
Based on the code and project description provided, your work demonstrates several core data skills, but it is most closely aligned with data analysis and data cleaning, rather than data engineering.

Data Skills Shown in Your Project
Web Scraping and Data Collection

You used Python with libraries such as requests and BeautifulSoup to extract company information from a website, which is a foundational skill for gathering raw data from the web.

This involves understanding HTML structure and using CSS selectors to target specific data elements.

Data Cleaning

Your code filters out incomplete records by checking if a company has at least three metadata spans, ensuring only reliable data is included.

You handle missing or inconsistent data by skipping incomplete records and assigning default values when necessary.

These are classic data cleaning techniques: handling missing values, filtering data, and ensuring data integrity.

Data Manipulation and Preparation

You use pandas to manage, manipulate, and save data in a structured format (CSV), which is essential for preparing data for further analysis.

This process is a key part of data analysis workflows, as it transforms raw data into a usable form.

Data Analysis vs. Data Engineering
Data Analysis

Your project is focused on collecting, cleaning, and structuring data for analysis, which are core responsibilities of a data analyst.

While you did not perform advanced statistical analysis or visualization in this specific code, the data you prepared is ready for such tasks.

Data analysts often spend a significant portion of their time cleaning and preparing data before analysis.

Data Engineering

Data engineers focus on building and maintaining data pipelines, databases, and infrastructure for large-scale data processing.

Your project does not involve designing databases, building ETL pipelines, or working with big data technologies, so it is not primarily a data engineering project.

Summary Table
Skill Area	Demonstrated in Project?	Description
Data Analysis	Yes	Collecting, cleaning, and preparing data for analysis
Data Cleaning	Yes	Handling missing data, filtering, and ensuring data integrity
Data Engineering	No	No infrastructure, pipelines, or database design involved
Web Scraping	Yes	Extracting data from websites using Python and parsing HTML
Conclusion
Your project showcases data cleaning and data analysis skills, with a strong emphasis on web scraping and data preparation. It does not involve the data engineering skills typically required for building data infrastructure or pipelines.

please help with this also.
Certainly! Based on your files and code for the JobPlanet enterprise data crawler, here’s how you can explain and showcase the data skills in your portfolio, and what you can write for this project specifically.

JobPlanet Enterprise Data Crawler
Project Overview

This project automates the collection and structuring of company information and employee ratings from JobPlanet, a major South Korean company review platform. The goal was to extract detailed company profiles and employee sentiment data for a curated list of enterprises, enabling market research, HR analytics, and business intelligence.

Key Data Skills Demonstrated
Web Scraping & Data Collection

Used Selenium WebDriver and BeautifulSoup to automate browser actions and parse HTML from JobPlanet’s search and company profile pages.

Implemented robust waiting and error handling to navigate dynamic web content and avoid detection.

Data Cleaning & Validation

Skipped incomplete or error-prone records during scraping, ensuring only reliable data was included.

Saved error logs for failed attempts, allowing for troubleshooting and data integrity checks.

Data Manipulation & Preparation

Extracted and structured company metadata (company ID, name, ratings, review counts, and detailed employee sentiment scores) using Python and pandas.

Transformed raw scraped data into clean, structured CSV files for further analysis.

Automation & Process Management

Automated the scraping process for thousands of companies, with periodic saving of progress to prevent data loss.

Added delays and anti-detection measures to maintain polite scraping and avoid being blocked by the website.

Error Handling & Logging

Logged errors and skipped problematic companies, ensuring the main process continued smoothly.

Saved both successful and failed attempts for transparency and debugging.

How to Present in Your Portfolio
Here’s a ready-to-use project description:

JobPlanet Enterprise Data Crawler

Developed an automated web scraper using Python, Selenium, and BeautifulSoup to collect structured company information and employee sentiment data from JobPlanet. The project involved parsing search results and detailed company profiles, extracting key metrics such as company ratings, review counts, and employee satisfaction scores. Implemented robust error handling and periodic data saving to ensure reliability and data integrity. The collected data was stored in CSV format for further business intelligence and HR analytics.

Tools: Python, Selenium, BeautifulSoup, Pandas
Key Challenges: Handling dynamic web content, error management, rate limiting
Result: Clean, structured dataset of company profiles and employee sentiment, ready for analysis.

Data Skills Table
Skill Area	Demonstrated in Project?	Description
Web Scraping	Yes	Automated data collection from dynamic websites using Selenium & BeautifulSoup
Data Cleaning & Validation	Yes	Skipped incomplete records, logged errors, ensured data integrity
Data Manipulation	Yes	Structured and transformed data using pandas
Automation	Yes	Automated scraping for thousands of companies, periodic progress saving
Error Handling & Logging	Yes	Logged errors and saved error files for troubleshooting
Data Analysis	Partially	Data prepared for analysis; not yet analyzed in this code
Data Engineering	Limited	Focused on data collection and cleaning, not building pipelines or databases
Example Output Table
company_id	name	search_rating	review_count	overall_rating	...	검색기업명
361502	(주)디에스아키종합건설	1.0	3	1.0	...	디에스아키종합건설
81448	(주)더샵스토리	1.9	18	1.9	...	더샵스토리
...	...	...	...	...	...	...
How to Explain the Data Skills
Web Scraping: “Automated collection of company data from JobPlanet using Selenium and BeautifulSoup.”

Data Cleaning: “Filtered incomplete or error-prone records and logged errors to ensure data quality.”

Data Manipulation: “Transformed raw scraped data into structured CSV files using pandas.”

Automation: “Automated the scraping process for thousands of companies with periodic progress saving.”

Error Handling: “Logged and managed errors to ensure uninterrupted data collection and easy troubleshooting.”

You can copy the above text and tables directly into your portfolio, adjusting as needed for your style or specific use case. This will clearly communicate your skills in web scraping, data cleaning, automation, and data preparation.

write for me this project for data analysis portfolio
Certainly! Here’s a portfolio-ready project description for your JobPlanet enterprise data crawler, tailored for data analysis, with clear explanations of the data skills demonstrated and the structure you can use:

JobPlanet Enterprise Data Crawler Project
Project Overview

Developed an automated web crawler to collect and structure company information and employee sentiment data from JobPlanet, a leading South Korean company review platform. The goal was to extract detailed profiles and ratings for thousands of enterprises, enabling comprehensive market research, HR analytics, and business intelligence.

Project Details
Objective

Automate Data Collection: Gather structured data about companies (including ratings, review counts, and detailed employee sentiment scores) from JobPlanet for a curated list of enterprises.

Prepare Data for Analysis: Create a clean, reliable dataset for further business intelligence and HR analytics.

Process and Implementation

Data Collection:

Used Python with Selenium WebDriver and BeautifulSoup to automate browser actions and parse HTML from JobPlanet’s search and company profile pages.

Implemented robust waiting and error handling to navigate dynamic web content and avoid detection.

Data Cleaning and Validation:

Skipped incomplete or error-prone records during scraping, ensuring only reliable data was included.

Logged errors and saved error files for troubleshooting and data integrity checks.

Data Transformation and Output:

Extracted and structured company metadata (company ID, name, ratings, review counts, and detailed sentiment scores) using pandas.

Saved the collected and cleaned data into structured CSV files for easy analysis and integration with other tools.

Automation and Reliability:

Automated the scraping process for thousands of companies, with periodic saving of progress to prevent data loss.

Added delays and anti-detection measures to maintain polite scraping and avoid being blocked by the website.

Tools and Technologies

Python

Selenium WebDriver

BeautifulSoup

Pandas

Regular expressions (re) for data extraction

CSV for data output

Data Skills Demonstrated
Skill Area	Demonstrated?	Description
Web Scraping	Yes	Automated data collection from dynamic websites using Selenium & BeautifulSoup
Data Cleaning & Validation	Yes	Skipped incomplete records, logged errors, ensured data integrity
Data Transformation	Yes	Structured and transformed data using pandas
Automation	Yes	Automated scraping for thousands of companies, periodic progress saving
Error Handling & Logging	Yes	Logged errors and saved error files for troubleshooting
Data Preparation	Yes	Prepared data for analysis, ready for business intelligence and HR analytics
Example Output
Below is a sample of the structured data collected for each company:

company_id	name	search_rating	review_count	overall_rating	복지/급여	워라밸	사내문화	승진 기회	경영진	기업 추천율	CEO 지지율	성장 가능성	검색기업명
361502	(주)디에스아키종합건설	1.0	3	1.0	1.3	1.3	1.0	1.0	1.0	0%	0%	0%	디에스아키종합건설
81448	(주)더샵스토리	1.9	18	1.9	1.7	2.6	2.0	1.8	1.9	11%	28%	0%	더샵스토리
...	...	...	...	...	...	...	...	...	...	...	...	...	...
Key Challenges and Solutions
Dynamic Web Content:

Implemented robust waiting and error handling to adapt to changes in website structure.

Data Integrity:

Skipped incomplete records and logged errors to ensure only reliable data was included.

Rate Limiting:

Added delays and anti-detection measures to avoid being blocked by the website.

Large-Scale Automation:

Automated the process for thousands of companies, with periodic progress saving to prevent data loss.

Results and Insights
Successfully collected and structured data for hundreds of companies, ready for further analysis or business intelligence tasks.

Demonstrated proficiency in web scraping, data cleaning, automation, and data preparation—core skills for modern data analysis and business intelligence roles.

Enabled deeper HR analytics and market research by providing a comprehensive, structured dataset of company profiles and employee sentiment.

How to Present in Your Portfolio
JobPlanet Enterprise Data Crawler

Developed an automated web scraper using Python, Selenium, and BeautifulSoup to collect structured company information and employee sentiment data from JobPlanet. The project involved parsing search results and detailed company profiles, extracting key metrics such as company ratings, review counts, and employee satisfaction scores. Implemented robust error handling and periodic data saving to ensure reliability and data integrity. The collected data was stored in CSV format for further business intelligence and HR analytics.

Tools: Python, Selenium, BeautifulSoup, Pandas
Key Challenges: Handling dynamic web content, error management, rate limiting
Result: Clean, structured dataset of company profiles and employee sentiment, ready for analysis.

You can copy this description directly into your data analysis portfolio, adjusting details as needed for your personal style or specific use case. This will clearly communicate your skills in web scraping, data cleaning, automation, and data preparation for analysis.

please write short description as the way i requested before.
Certainly! Here is a short portfolio description for your Naver News Crawler for Assigned Companies project, following the style of your previous request:

In this project, I developed an automated web crawler to collect and analyze the latest Naver News articles for a curated list of companies assigned to a specific manager. Using Python, Pandas, and the Naver Search Open API, I extracted relevant news data, cleaned HTML tags, and saved the results in a structured CSV file. The project enables efficient monitoring of company-related news for business intelligence and market research, supporting evidence-based decision-making and streamlined data collection for large datasets.

You can copy and paste this directly into your portfolio.

write for me this project for data analysis portfolio
Certainly! Here is a concise, results-focused data analysis portfolio description for your Titanic Survival Dashboard project, following the style you requested:

In this project, I developed an interactive dashboard to analyze survival patterns among Titanic passengers using Python, Streamlit, and data visualization libraries. By applying filtering options for gender, age, and passenger class, I enabled users to explore how these factors influenced survival rates. The findings revealed that female passengers and those in higher classes had significantly better survival odds, demonstrating the practical application of data analysis for uncovering historical trends and supporting decision-making insights.

You can copy this directly into your portfolio. If you want to include the tools used, you can add a line at the end:

Tools: Python, Streamlit, Pandas, Seaborn, Matplotlib

Feel free to adjust the wording or focus as needed for your portfolio style.

write a professional data analysis portfolio for me.
Certainly! Below is a professional data analysis portfolio entry for your Titanic Survival Dashboard project, incorporating your code, tools, and the style you requested. This format can be used as a template for your portfolio, with adjustments as needed for other projects.

Titanic Survival Data Dashboard
Project Overview

In this project, I developed an interactive dashboard to analyze survival patterns among Titanic passengers. Using Python and Streamlit, I created a user-friendly interface that allows for dynamic filtering of data by gender, age, and passenger class. The dashboard provides real-time visualizations of survival rates and demographic breakdowns, enabling deeper insights into the factors that influenced survival outcomes.

Key Features & Data Skills
Data Cleaning & Preprocessing

Removed irrelevant columns such as Cabin and Ticket to focus on meaningful features.

Mapped gender values for consistency and ease of analysis.

Handled missing or inconsistent data to ensure data integrity.

Interactive Data Exploration

Implemented sidebar filters for gender, passenger class, and age range.

Enabled users to dynamically explore subsets of the data and observe how survival rates change across different groups.

Data Visualization

Generated clear, informative plots using Seaborn and Matplotlib:

Survivor Count: Bar chart comparing survivors and non-survivors.

Survival by Gender: Stacked bar chart showing survival rates for males and females.

Survival by Passenger Class: Stacked bar chart illustrating survival rates across first, second, and third classes.

User Experience

Designed a visually appealing, intuitive dashboard with a wide layout for optimal viewing.

Added a music section to enhance user engagement and enjoyment.

Tools & Technologies
Python

Streamlit (for interactive web dashboard)

Pandas (for data manipulation and preprocessing)

Seaborn & Matplotlib (for data visualization)

Short Project Description
In this project, I analyzed Titanic passenger data to uncover patterns in survival rates based on gender, age, and passenger class. Using Python and Streamlit, I built an interactive dashboard that enables users to filter and visualize the data dynamically. The results highlight significant disparities in survival, particularly for women and higher-class passengers, demonstrating the value of data-driven analysis for understanding historical events and informing decision-making.

Example Output Table
PassengerId	Survived	Pclass	Name	Sex	Age	SibSp	Parch	Fare	Embarked
1	0	3	Braund, Mr. Owen Harris	male	22	1	0	7.25	S
2	1	1	Cumings, Mrs. John Bradley...	female	38	1	0	71.28	C
...	...	...	...	...	...	...	...	...	...
Insights & Findings
Gender Disparity: Female passengers had significantly higher survival rates than male passengers.

Class Influence: Passengers in first and second classes were more likely to survive than those in third class.

Age Impact: Younger passengers, especially children, had better survival rates when filtered by age range.

How to Present in Your Portfolio
Titanic Survival Data Dashboard

Developed an interactive dashboard using Python and Streamlit to analyze survival patterns among Titanic passengers. The project involved cleaning and preprocessing data, implementing dynamic filters for gender, age, and passenger class, and visualizing survival rates with Seaborn and Matplotlib. The dashboard provides actionable insights into the factors that influenced survival outcomes, supporting evidence-based analysis and decision-making.

Tools: Python, Streamlit, Pandas, Seaborn, Matplotlib
Key Skills: Data cleaning, interactive visualization, user experience design
Result: Interactive, data-driven dashboard for exploring Titanic survival data

You can use this structure and content for your professional data analysis portfolio, adapting it as needed for other projects.

please add:" i create a app website on streamlit. here is the link https://ncthang17.streamlit.app/
Certainly! Here is a revised, professional portfolio entry for your Titanic Survival Data Dashboard project, including your statement and the app link:

Titanic Survival Data Dashboard
Project Overview

In this project, I developed an automated web dashboard to analyze survival patterns among Titanic passengers using Python, Streamlit, and data visualization libraries. I created an interactive website app on Streamlit, enabling users to filter data by gender, age, and passenger class to explore how these factors influenced survival rates. The findings revealed that female passengers and those in higher classes had significantly better survival odds, demonstrating the practical application of data analysis for uncovering historical trends and supporting decision-making insights.

App Link:
https://ncthang17.streamlit.app/

Process and Implementation

Data Collection & Cleaning:

Loaded and preprocessed the Titanic dataset using Pandas, removing irrelevant columns and mapping values for consistency.

Interactive Dashboard:

Built a user-friendly interface with Streamlit, featuring dynamic filters for gender, age, and passenger class.

Displayed filtered data previews and generated real-time visualizations using Seaborn and Matplotlib.

Visualizations:

Created clear charts showing survivor counts, survival by gender, and survival by passenger class.

User Experience:

Designed a visually appealing, intuitive dashboard with a wide layout and an engaging music section.

Tools and Technologies

Python

Streamlit (for web app and interactive dashboard)

Pandas (for data manipulation)

Seaborn & Matplotlib (for data visualization)

Key Challenges and Solutions

Handling Missing Data:

Implemented robust preprocessing to ensure only reliable data was included.

Dynamic Filtering:

Enabled users to interactively filter and visualize subsets of the dataset.

User Engagement:

Added multimedia elements to enhance the dashboard experience.

Results and Insights

Successfully created an interactive, user-friendly web app for exploring Titanic survival data.

Demonstrated proficiency in data cleaning, visualization, and web app development.

Enabled deeper insights into historical trends and the impact of demographic factors on survival.

How to Present in Your Portfolio

Titanic Survival Data Dashboard

In this project, I developed an automated web dashboard to analyze survival patterns among Titanic passengers using Python, Streamlit, and data visualization libraries. I created an interactive website app on Streamlit, allowing users to filter data by gender, age, and passenger class to explore how these factors influenced survival rates. The findings revealed that female passengers and those in higher classes had significantly better survival odds, demonstrating the practical application of data analysis for uncovering historical trends and supporting decision-making insights. Here is the link to the app: https://ncthang17.streamlit.app/

Tools: Python, Streamlit, Pandas, Seaborn, Matplotlib
Key Challenges: Handling missing data, dynamic filtering, user engagement
Result: Interactive, data-driven web app for exploring Titanic survival data

You can copy this description directly into your data analysis portfolio.

also please write me a readme.md on github thank you so much.
Certainly! Here’s a professional README.md you can use for your GitHub repository for the Titanic Survival Data Dashboard project, based on your code and Streamlit app.

text
# Titanic Survival Data Dashboard

An interactive web dashboard for exploring Titanic passenger data, built with Python and Streamlit.

---

## Overview

This project provides a dynamic dashboard to analyze survival patterns among Titanic passengers. Users can filter data by gender, age, and passenger class, and view real-time visualizations of survival rates and demographic breakdowns.

**App Link:**  
[https://ncthang17.streamlit.app/](https://ncthang17.streamlit.app/)

---

## Features

- **Interactive Filters:**  
  - Filter passengers by gender, passenger class, and age range.
- **Data Visualization:**  
  - Survivor vs. non-survivor count.
  - Survival rate by gender.
  - Survival rate by passenger class.
- **Filtered Data Preview:**  
  - View a preview of the filtered dataset.
- **User Experience:**  
  - Wide layout for optimal viewing.
  - Background music for enhanced experience.

---

## Screenshots

*Replace with your own screenshots if desired.*

---

## Installation

1. **Clone the repository:**
git clone https://github.com/your-username/titanic-dashboard.git
cd titanic-dashboard

2. **Install dependencies:**
pip install -r requirements.txt

3. **Run the app:**
streamlit run app.py

---

## Requirements

- Python 3.x
- Streamlit
- Pandas
- Seaborn
- Matplotlib

---

## Data

The dataset used is `train.csv` from the Titanic dataset.

---

## How to Use

1. **Open the app:**  
Launch the app locally or visit the deployed Streamlit app.
2. **Apply filters:**  
Use the sidebar to select gender, passenger class, and age range.
3. **View results:**  
The dashboard updates automatically with filtered data and visualizations.

---

## Technologies Used

- **Python**
- **Streamlit** (for web app and interactive dashboard)
- **Pandas** (for data manipulation)
- **Seaborn & Matplotlib** (for data visualization)

---

## Project Structure
titanic-dashboard/
│
├── app.py # Main Streamlit application
├── train.csv # Titanic passenger dataset
└── requirements.txt # Python dependencies

---

## License

This project is open source and available under the [MIT License](LICENSE).


