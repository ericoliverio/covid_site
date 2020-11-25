# Tracking Covid-19 Cases in Erie County, NY By ZIP Code

1) erie_total.csv - Daily total Covid-19 cases per ZIP code since June 2020. 

Data is scraped daily from the Erie County Department of Health Deshboard at:
http://erieny.maps.arcgis.com/apps/opsdashboard/index.html#/dd7f1c0c352e4192ab162a1dfadc58e1

(Data on population, sq. milage, and approximate coordinates of each ZIP code are acquired from the same website)

2) erie_diff.csv - Reported new cases per ZIP code since June (current day cases - previous day cases for erie_total.csv)
3) diff_avg.csv - Average daily cases per ZIP code since June (7-10 day average / Depends on frequency of updates)

4) munc_erie.csv - Daily total Covid-19 cases per municipality since 11/11/2020
5) erie_summary.csv - County total positives, deaths, testing totals and percentages since 11/6/2020
 
(Outdated)
5) daily_report.csv - Provides data for erie_folium.py to create website  
6) active_cases.csv - Active cases by municipalities in Erie County (avaiable in website data, but never updated. Current data is old)
  
update_erie.command: Reads ZIP code covid data from the Erie County Department of Health website
read_erie.py: Uses erie_total.csv to calculate metrics and create reports/visualization (bar graphs, top ZIP codes)
erie_folium.py: Not used
