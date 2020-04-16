 
### VAR analysis of COVID_19 in different countries.

The analysis explores patterns in current new cases and deaths across countries. The data was sourced from the cdc and is made available in this repo. See cdc.csv.

Three countries were chosen for this analysis. The results of the analysis are contained within the notebook entitled, covidresults.ipynb.

Within that notebook is an analysis of where Australia, Ireland and South Korea are in terms of flattening their respective curves.

Vector Autoregression analysis picks up statistical relationships across time. Data from the daily recorded new cases and new deaths were lagged for up to fourteen days to see what linkages were still evident across time.

Visualising those statistical linkages was done by only showing links(coefficients) which held at the 99% confidence level. If a lag was not significant at this level is was suppressed to zero to make visualisation simpler.

Countries like Australia and South Korea, who are flattening their respective curves, have only recent and negative links showing. At the time of writing, Ireland was in the process of flattening it's curve and was still showing positive linkages to older case and death numbers. 
