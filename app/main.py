#DUALIDAD | SCRIPTS TERMINAL - ARCHIVOS O MODULOS
import utils
import read_csv
import charts

#para modularizar y que no se ejecute todo el modulo al lamarlo desde otra parte, se deben embeber en funciones y así en el otro lado se llama lo que se quiere; las VARIABLES se dejan por fuera de las funciones para invocarlas
def run():
  data = read_csv.read_csv('data.csv')
  data = list(filter(lambda i : i['Continent']=='South America', data))
  countries = list(map(lambda x: x['Country/Territory'], data))
  percent = list(map(lambda x: x['World Population Percentage'], data))
  charts.generate_pie_chart(countries, percent)
  
  
 ## data = read_csv.read_csv('./app/data.csv')
  country = input('Type country ==> ')
  pais = country
  result = utils.population_by_country(data, country)

  #para conirmar que encontró al pais
  if len(result) > 0:
    country = result[0]
    keys, vaules = utils.get_poblation(country)
    charts.generate_bar_chart(pais, keys, vaules)
  

#si quiero ejecutar este archivo desde la terminal sin que lo controle example que es de donde se llama el metodo run se hace así:

# si se ejecuta desde la terminal, hace lo que esta debajo, quie es ejecurar run
if __name__ == '__main__':
  run()
