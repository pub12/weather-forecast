import requests
import datetime, pytz
from quickchart import QuickChart


OPEN_WEATHER_MAP_APIKEY = '16786afe8ea0f6b683ab9298e52ac247'

def get_weather_data_by_location( lat, long):
	url = f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={long}&appid={OPEN_WEATHER_MAP_APIKEY}&units=metric'
	print(f"Getting data via {url}")
	r = requests.get(url)
	return r.json()
	if r.status_code == 200:
		return r.json()
	else:
		return None


	def get_quick_chart( json_data , output_file):
		qc = QuickChart()
		qc.width = 500
		qc.width = 500

		labels = []	#Declare to hold the x-axis tick labels
		weather_readings = []  #get the data labels

		for index in range( 1, 8):
			local_time = datetime.datetime.fromtimestamp( json_data['daily'][index]['dt'] , tz=pytz.timezone('Asia/Singapore'))
			labels.append(   local_time.strftime( '%a %d/%m ' ) )

			weather_readings.append( round( json_data['daily'][index]['temp']['day'] ,1) )

		qc.config = """{ 
						  type: 'line', 
						  data: { 
						    labels: """ + str( labels ) + """,
						datasets: [
		 				      { 
						        backgroundColor: 'rgb(255, 99, 132)', 
						        data: """ + str( weather_readings) + """,
						        lineTension: 0.4,
						        fill: false,
						      }
						    ],
						  },
						  options: { 
						  				title: { display: true,  text: '7-Day Weather Forecast' }, 
						  				legend: { display: false}, 
						  				scales: { yAxes: [ { scaleLabel: 
						  									 { display: true, labelString: 'Temperature Degrees Celcius' } } ]},
						  				plugins: {
												      datalabels: {
												        display: true,
												        align: 'bottom',
												        backgroundColor: '#ccc',
												        borderRadius: 3
												      },
												  }
						  			},
						}""" 
		print(qc.get_short_url()) 	#Print out the chart URL
		qc.to_file(output_file)	#Save to a file



if __name__ == '__main__':
	print("Getting Weather Data")
	json_data =  get_weather_data_by_location( '22.300910042194783', '114.17070449064359') 
	get_quick_chart( json_data , 'mychart.png' )

