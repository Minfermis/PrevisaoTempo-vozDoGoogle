# Bibliotecas a serem instaladas. 

import requests
import pyttsx3

# Sua chave de API do OpenWeatherMap
api_key = 'SUA_CHAVE_DE_API_AQUI' # Entrando no site e criando um login voce ganha uma chave, use essa chave para acessar a previsão de tempo da API.

# Função para obter informações do clima de uma cidade
def get_weather_info(city):
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(base_url)
    
    if response.status_code == 200:
        data = response.json()
        temperature = data['main']['temp']
        weather_description = data['weather'][0]['description']
        return temperature, weather_description
    else:
        return None, None

# Função para fornecer lembretes com a voz do Google
def provide_reminders(city):
    temperature, weather_description = get_weather_info(city)
    
    if temperature is not None and weather_description is not None:
        # Inicializa o motor de síntese de voz do Google
        engine = pyttsx3.init()
        
        # Define a voz do Google
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)  # Escolha a voz que você prefere

        # Fala a temperatura atual
        engine.say(f"A temperatura em {city} é {temperature:.1f} graus Celsius.")
        
        # Verifica as condições com base na temperatura
        if temperature <= 15:
            engine.say(f"Vai estar frio em {city}. Não se esqueça de levar um agasalho.")
        elif 16 <= temperature <= 24:
            engine.say(f"O clima em {city} está normal. Aproveite o seu dia!")
        else:
            engine.say(f"Vai estar quente em {city}. Lembre-se de usar protetor solar antes de sair.")
        
        # Verifica as condições de chuva
        if "rain" in weather_description:
            engine.say(f"E também está prevista chuva em {city}. Não se esqueça de levar um guarda-chuva.")
        
        engine.runAndWait()
    else:
        print(f"Não foi possível obter informações do clima para {city}.")

if __name__ == '__main__':
    cidade = 'Guarulhos'  # Substitua 'sua-cidade' pelo nome da sua cidade
    provide_reminders(cidade)
