# Previsão do tempo (Em tempo real) com voz do Google

## Introdução
Este código utiliza as bibliotecas requests e pyttsx3 para consultar a previsão do tempo usando a API da OpenWeatherMap e, em seguida, fornece informações sobre a temperatura e lembretes com base nas condições climáticas. Logo fiz para brincar com meu problema de não olhar a previsão do tempo e sempre ser do contra no decorrer do dia. Certifique-se de fornecer sua chave de API da OpenWeatherMap para que o código funcione corretamente.

### Bibliotecas Usadas
- `requests`: Essa biblioteca é usada para fazer solicitações HTTP à API da OpenWeatherMap para obter dados de previsão do tempo.
- `pyttsx3`: Essa biblioteca é usada para sintetizar a fala com a voz do Google para fornecer informações sobre a previsão do tempo.

### Chave de API
~~~Python
api_key = 'SUA_CHAVE_DE_API_AQUI'
~~~
Você precisa substituir `'SUA_CHAVE_DE_API_AQUI'` pela sua chave de API da OpenWeatherMap (Entrando no site e criando um login voce ganha uma chave. Esse é o site <https://openweathermap.org>). A chave de API é necessária para autenticar e acessar os dados de previsão do tempo da API.



### Solicitação de Informação
~~~Python
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

~~~
- Esta função é responsável por fazer uma solicitação à API da OpenWeatherMap e obter informações sobre a temperatura e a descrição do clima para uma cidade específica.
- Ela monta a URL da API com base na cidade e na chave de API fornecidas e faz uma solicitação GET para obter os dados meteorológicos.
- Se a resposta da API for bem-sucedida (código de status 200), ela analisa os dados JSON `(JSON é uma abreviação de "JavaScript Object Notation" (Notação de Objetos JavaScript). É um formato de dados leve, legível por humanos e independente da linguagem de programação usada para representar dados estruturados. O JSON é comumente usado para trocar dados entre um servidor e um cliente, ou entre diferentes partes de um programa.)` para extrair a temperatura e a descrição do clima e as retorna. Caso contrário, retorna `None` para ambos.

### Recebe informações do tempo de acordo com a cidade preechida
~~~Python
def provide_reminders(city):
    temperature, weather_description = get_weather_info(city)
    
    if temperature is not None and weather_description is not None:
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        
        engine.say(f"A temperatura em {city} é {temperature:.1f} graus Celsius.")
        
        if temperature <= 15:
            engine.say(f"Vai estar frio em {city}. Não se esqueça de levar um agasalho.")
        elif 16 <= temperature <= 24:
            engine.say(f"O clima em {city} está normal. Aproveite o seu dia!")
        else:
            engine.say(f"Vai estar quente em {city}. Lembre-se de usar protetor solar antes de sair.")
        
        if "rain" in weather_description:
            engine.say(f"E também está prevista chuva em {city}. Não se esqueça de levar um guarda-chuva.")
        
        engine.runAndWait()
    else:
        print(f"Não foi possível obter informações do clima para {city}.")

~~~
- Esta função recebe o nome de uma cidade como entrada e usa a função `get_weather_info` para obter informações sobre a temperatura e a descrição do clima para essa cidade.
- Em seguida, inicializa o motor de síntese de voz do Google `(pyttsx3)`, configura a voz e utiliza o mecanismo para fornecer informações sobre o clima com base nas condições climáticas e na temperatura.
- Se a temperatura estiver abaixo de 15°C, ele dirá que está frio. Se estiver entre 16°C e 24°C, dirá que o clima está normal. Se estiver acima de 24°C, dirá que está quente. Além disso, ele verificará se há previsão de chuva e fornecerá um lembrete, se necessário.
- Se não for possível obter informações do clima para a cidade especificada, ele imprimirá uma mensagem de erro.

### Execução Principal
~~~Python
if __name__ == '__main__':
    cidade = 'Sua-cidade'  # Substitua 'sua-cidade' pelo nome da sua cidade
    provide_reminders(cidade)

~~~
- Esta parte do código verifica se o script está sendo executado como um programa principal (não importado como um módulo). Se sim, ele define o nome da cidade (por exemplo, 'Guarulhos') que você deseja consultar e chama a função provide_reminders para fornecer informações sobre o clima e lembretes com base nas condições meteorológicas. Certifique-se de substituir 'Guarulhos' pela cidade que você deseja consultar.

Certifique-se de fornecer sua chave de API da OpenWeatherMap para que o código funcione corretamente.
