# covid_site

1) update_erie.command 
Reads ZIP code covid data from the Erie County Department of Health website: 
http://erieny.maps.arcgis.com/apps/opsdashboard/index.html#/dd7f1c0c352e4192ab162a1dfadc58e1

  updates:
  erie_total.csv # Daily totals of Covid in each ZIP code every day since June
  
2) read_erie.py
Uses erie_total.csv to calculate metrics and create reports/visualization (bar graphs, top ZIP codes)
  
  updates:
  erie_diff.csv # Daily cases per zip code
  diff_avg.csv # 7 day average of daily cases per zip code
  
  daily_report.csv #(not used)
  
