# Tracking Covid-19 Cases in Erie County, NY By ZIP Code
This project started as I found the COVID-19 dashboard run by Erie County hard to read and not conveying the information I found most important (where are cases trending upwards? How do the current new cases compare to other zip codes?)

1) update_erie.command - Run this to scrape daily covid-19 data by ZIP code for Erie County and save results in erie_total.csv

Data is scraped daily from the Erie County Department of Health Deshboard at:
http://erieny.maps.arcgis.com/apps/opsdashboard/index.html#/dd7f1c0c352e4192ab162a1dfadc58e1
(Data on population, sq. milage, and approximate coordinates of each ZIP code are acquired from the same website)

![Screen Shot 2023-01-06 at 11 06 34 AM](https://user-images.githubusercontent.com/25538281/211050942-7b6dee64-ab77-4ef2-8f8b-2b53172db097.png)

2) erie_total.csv - Daily total Covid-19 cases per ZIP code since June 2020. Also contains population, area (square feet), and coordinates for each zip code.

3) read_erie.py - Run this to calculate the number of new cases per day per zip code, as well as the average daily new cases. Results are saved in erie_diff.csv and diff_avg.csv. Will display a sorted bar chart of the zip codes with the largest increase in cases.
![New Cases Sorted](https://user-images.githubusercontent.com/25538281/211050666-d70a17a3-cb1e-491a-a151-26fc269c1a23.png)

4) erie_diff.csv - Reported daily new cases per ZIP code since June (current day cases - previous day cases for erie_total.csv)

5) diff_avg.csv - Average daily new cases per ZIP code since June (7-10 day average / Depends on frequency of updates)

6) tall_avg.csv, total_tall.csv - reformatted daily new case and daily new average case data for use in Tableau visualization.
 ![Screen Shot 2023-01-06 at 11 07 35 AM](https://user-images.githubusercontent.com/25538281/211051076-518894b5-563c-45fd-8a63-d530f8003d45.png)

(Outdated)

7) daily_report.csv - Provides data for erie_folium.py to create website  
8) active_cases.csv - Active cases by municipalities in Erie County (avaiable in website data, but never updated. Current data is old)
9) munc_erie.csv - Daily total Covid-19 cases per municipality since 11/11/2020
10) erie_summary.csv - County total positives, deaths, testing totals and percentages since 11/6/2020
