 

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas import DatetimeIndex
pd.options.mode.chained_assignment = None
import statsmodels.api as sm
from statsmodels.tsa.api import VAR

class c:		

	 

    #Input data and country of interest. Function outputs chart of cofficients that are significant(99%).

	def country(data,country):
		print('VAR Analysis of COVID-19 in',  country)
		df1= data.loc[lambda df: df['location'] == country, :]
		df2= df1[['new_cases','new_deaths']]+0.0000001 #round up zeros slightly ahead of logs
		    
		#Get logs of variables
		df2.index = pd.DatetimeIndex(df1.index).to_period('D')
		df2_log = np.log(df2).diff().dropna()
		#Run VAR model with 14 day lags
		model = VAR(df2_log)
		results = model.fit(maxlags=14,trend='nc')
		#Save results to the summary dataframe
		i=results.pvalues.index
		df_coef= pd.DataFrame(columns=(['new_cases','new_deaths']),index=i) 
		df_coef['new_cases']= results.coefs[:,0].reshape(28,1) 
		df_coef['new_deaths']= results.coefs[:,1].reshape(28,1)
		df_p= pd.DataFrame(results.pvalues)
		df_p.columns = (['new_cases_pvalues', 'new_deaths_pvalues']) 
		#Use catchall dataframe for both sets of plots below
		summary= pd.concat([df_coef,df_p],axis=1,sort=False) 
		    
		#New_cases 
		summary_nc =summary[['new_cases', 'new_cases_pvalues']] 
		mask_nc = (summary_nc['new_cases_pvalues'] > 0.01)
		summary_nc['new_cases'][mask_nc] = 0
		#Plot new cases versus old cases and old deaths(up to and inclduing 14 days)
		my_range=range(0,len(summary_nc.index))
		plt.figure(figsize=(15,5))
		plt.stem(summary_nc['new_cases'], markerfmt=' ')
		plt.xticks(my_range,summary_nc.index,rotation=90)
		plt.title("Link between current COVID-19 cases and past cases and deaths", loc='center',fontsize=18)
		plt.xlabel('Lags of cases and deaths by up to 14 days',fontsize=12)
		plt.ylabel('Coefficient size',fontsize=12) 
		#Change color and shape and size and edges
		(markers, stemlines, baseline) = plt.stem(summary_nc['new_cases'])
		plt.setp(markers, marker='D', markersize=5, markeredgecolor="orange", markeredgewidth=2)   
		     
		#New deaths  
		summary_nd = summary[['new_deaths','new_deaths_pvalues']]
		mask_nd = (summary_nd['new_deaths_pvalues'] > 0.01)
		summary_nd['new_deaths'][mask_nd] = 0   
		#Plot new deaths versus old cases and old deaths(up to and inclduing 14 days)
		plt.figure(figsize=(15,5))
		plt.stem(summary_nd['new_deaths'], markerfmt=' ')
		plt.xticks(my_range,summary_nd.index,rotation=90)
		plt.title("Link between current COVID-19 deaths and past cases and deaths", loc='center',fontsize=18)
		plt.xlabel('Lags of cases and deaths by up to 14 days',fontsize=12)
		plt.ylabel('Coefficient size',fontsize=12) 
		(markers, stemlines, baseline) = plt.stem(summary_nd['new_deaths'])
		plt.setp(markers, marker='D', markersize=5, markeredgecolor="red", markeredgewidth=2)      
