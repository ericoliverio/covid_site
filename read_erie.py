import pandas as pd
import matplotlib.pyplot as plt
import numpy as mp
import matplotlib.ticker as ticker


df = pd.read_csv("/Users/ericoliverio/Desktop/erie_total.csv")

#LIST OF METRICS
#	TOTAL CASES
#	CASES BY POP
#	DAILY CASES (AVG/PER POP?)
#	GF

#CREATES ERIE_DAILY.CSV TO CREATE FOLIUM MAP

#FUNCTIONS
#	TOP TEN BARCHART
#	T-S DAILY CASES BY ZIP 
#	FOLIUM MAP

#----

demog = df.iloc[:,0:6]
df_sep = df.drop(df.iloc[:, 0:6], axis=1)

df_pos =df_sep.copy()

df_pos.insert(0,column='Name',value=df['Name'])



#PER POP
df_pop = 100*df_sep.div(df.iloc[:,1],axis = 0)
df_pop.insert(0,column='Name',value=df['Name'])

#DIFF
diff = df_sep.diff(axis = 1) 

diff.insert(0, column='Name', value=df['Name'])
diff.fillna(0,inplace=True)
print(diff.sort_values(df.columns[-1],ascending=False))
#ROLLING AVG DIFF
diff_t = diff.T
new_header = diff_t.iloc[0] #grab the first row for the header
diff_t = diff_t[1:] #take the data less the header row
diff_t.columns = new_header

window = 7


rol = diff_t.rolling(window).sum()/window
rol = rol.T

rol.fillna(0,inplace=True)
rol.reset_index(inplace=True)

#GF
rol_sep = rol.drop(rol.iloc[:,0:1],axis=1)

window1 = 5
gf = rol_sep.pct_change()
rol_gf = gf.rolling(window1).sum()/window1

rol_gf.fillna(0,inplace=True)
rol_gf.insert(0, column='Name', value=df['Name'])

#------
#64 total
def top_ten(df_test,date1=df.columns[-1],num=10,title1=''):
	df_sort = df_test.sort_values(date1, ascending = False)
	df10 = df_sort.iloc[0:num,:]

	#PLOT
	df10.plot.barh(y=date1,x='Name',alpha=0.7)
	date2 = df.columns[-2]

	ax = plt.gca()
	ax.invert_yaxis()
	
	#ax.xaxis.grid(b=True,linestyle='--',alpha=0.8)
	
	ax.spines['top'].set_visible(False)
	ax.spines['right'].set_visible(False)
	#ax.spines['bottom'].set_visible(False)
	ax.spines['left'].set_visible(False)
	#plt.yticks(fontsize=15)

	plt.ylabel('')
	plt.legend('')
	#ax.get_xaxis().set_ticks([])
	plt.title(str(title1)+' '+str(date2)+' - '+str(date1),size=15)

	for i, v in enumerate(df10[date1]):
		ax.text(v + 0.0, i + 0, str(str(v)), color='black',size=15)
		print()

	plt.show()
	#END PLOT

print('Difference and rolling average saved...')
diff.to_csv("/Users/ericoliverio/Desktop/erie_diff.csv",index=False)
rol.to_csv("/Users/ericoliverio/Desktop/diff_avg.csv",index=False)

#Create daily report.csv for folium map
num1 = -1

report = demog.copy()

report['Total Cases'] = df.iloc[:,num1]
#report['pop'] = df_pop.iloc[:,num1]
report['Daily Cases'] = diff.iloc[:,num1]
#report['avg Daily Cases'] = rol.iloc[:,num1]
report['GF'] = rol_gf.iloc[:,num1]

#report.to_csv("/Users/ericoliverio/Desktop/daily_report.csv",index=False)
#print('Report made')

#MM/DD/YY if DD < 10
top_ten(diff,title1='New Cases')

#---- TS PLOTTING



def ts(df_test,df_avg,name):
	
	plt.figure(figsize=(15,10))	
	
	rol1 = df_test.T
	new_header = rol1.iloc[0] #grab the first row for the header
	rol1 = rol1[1:] #take the data less the header row
	rol1.columns = new_header

	rol2 = df_avg.T
	new_header = rol2.iloc[0] #grab the first row for the header
	rol2 = rol2[1:] #take the data less the header row
	rol2.columns = new_header	


	plt.bar(rol1.index,rol1[name],label='actual cases',alpha=0.7)
	plt.bar(rol2.index,rol2[name],color='indianred',label='average',alpha=0.5)
	plt.title(str(name))
	ax=plt.gca()
	plt.legend()
	ax.xaxis.set_major_locator(ticker.MultipleLocator(3))

	plt.show()

#ts(diff,rol,'Main (allen to park)')
