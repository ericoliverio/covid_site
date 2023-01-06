# Tracking Covid-19 Cases in Erie County, NY By ZIP Code
This project started as I found the Covid-19 dashboard run by Erie County hard to read and not conveying the information I found most important (where are cases trending upwards? How do the current new cases compare to other ZIP codes?). Contains the only source for ZIP code-level Covid-19 data for Erie county collected over the period of two years. Featured on, and used by The Buffalo News. 

![Me](https://user-images.githubusercontent.com/25538281/211057268-0c637f6e-25ad-42c2-af6c-0e86bfa13caa.png)

https://buffalonews.com/news/local/covid-19-spread-in-erie-county-threatens-thanksgiving-dinner-officials-warn/article_1f3413ce-21e9-11eb-8406-df96f190525b.html

1) update_erie.command - Run this to scrape daily total number of Covid-19 cases by ZIP code for Erie County and save results in erie_total.csv

Data is scraped daily from the Erie County Department of Health Deshboard at:
http://erieny.maps.arcgis.com/apps/opsdashboard/index.html#/dd7f1c0c352e4192ab162a1dfadc58e1
(Data on population, sq. milage, and approximate coordinates of each ZIP code are acquired from the same website)

![Screen Shot 2023-01-06 at 11 06 34 AM](https://user-images.githubusercontent.com/25538281/211050942-7b6dee64-ab77-4ef2-8f8b-2b53172db097.png)

2) erie_total.csv - Daily total Covid-19 cases per ZIP code since June 2020. Also contains population, area (sq. milage), and coordinates for each zip code. I have manually assigned a neighborhood name to each ZIP code.

3) read_erie.py - Run this to calculate the number of new cases per day per zip code, as well as the average daily new cases. Results are saved in erie_diff.csv and diff_avg.csv. Displays a sorted bar chart of the ZIP codes with the largest increase in cases.

![New Cases Sorted](https://user-images.githubusercontent.com/25538281/211052127-2f6597ec-e3ec-4788-9112-ec78294528e7.png)

4) erie_diff.csv - Reported daily new cases per ZIP code since June (current day cases - previous day cases for erie_total.csv)

5) diff_avg.csv - Average daily new cases per ZIP code since June (7-10 day average / Depends on frequency of updates)

6) tall_avg.csv, total_tall.csv - Reformatted daily new case and daily new average case data for use in Tableau visualization. Also calculated the growth factor, and number of cases in each ZIP code per 100,000 residents.
https://public.tableau.com/app/profile/eric.oliverio/viz/AverageDailyCasesPerPop/Dashboard1 
 ![Screen Shot 2023-01-06 at 11 07 35 AM](https://user-images.githubusercontent.com/25538281/211051076-518894b5-563c-45fd-8a63-d530f8003d45.png)

# Reports
Contains attempts at other forms of spatial/map visualizations using the python folium package.

7) erie_covid.html - scrollable/zoomable map with a heat map showing density of cases.
![Screen Shot 2023-01-06 at 11 17 30 AM](https://user-images.githubusercontent.com/25538281/211052967-1a5aa233-1410-418f-b778-f725a22a2e11.png)

8) erie.mv - Shows the spread and change in density of new Covid-19 cases over a series of months.
  ![Screen Shot 2023-01-06 at 11 19 46 AM](https://user-images.githubusercontent.com/25538281/211053200-6e30234c-065d-4b4e-aa66-08bfe24c1670.png)
  
9) erie_demographics.csv - Contains race demographic information collected from the U.S. Census Bureau. Use to determine how Covid-19 affected minorities in the city, especially in the East and West sides following reopeing.

# Notes
Early data indicated that ZIP codes with older demographics/retirment homes had higher instances of Covid-19 in the earlier days of the pandemic. A Freedom of Information request was sent to Erie County to gain access to all their Covid-19 case data over the entire pandemic. The request was denied, appealed, and denied again.


![Screen Shot 2023-01-06 at 11 31 45 AM](https://user-images.githubusercontent.com/25538281/211055850-3908f71f-9aa5-4494-9a2d-06a987e2a98f.png)


(Outdated)

* daily_report.csv - Provides data for erie_folium.py to create website  
* active_cases.csv - Active cases by municipalities in Erie County (avaiable in website data, but never updated. Current data is old)
* munc_erie.csv - Daily total Covid-19 cases per municipality since 11/11/2020
* erie_summary.csv - County total positives, deaths, testing totals and percentages since 11/6/2020
