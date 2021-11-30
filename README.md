# Serviço de reconhecimento de usuários
Esse serviço visa o reconhecimento de usuários com base em padrões de digitação do teclado usando o algoritmo KNN em conjunto com o cálculo da distância de Manhattan. Os dados são baseados em intervalos de tempo da digitação.

## Requisitos
- Linux/Mac/Windows
- Python 3.9

## Como usar

### Criando ambiente virtual
```
pip virtual env
source env/bin/activate
pip install -r requirements.txt
```

### Iniciando serviço
```
py wsgi.py
```

## Wiki

### Exemplo de dado esperado
| ID | E-mail | Nome | Input do teclado |
| -- | ------ | ---- | ---------------- |
| 1 | rafa1@bol.com.br | Rafael | d_52_313 u_52_332 d_66_549 u_66_569 d_70_899 u_70_919 d_49_1054 u_49_1079 d_68_1176 u_68_1210 d_49_1292 u_49_1317 |

#### Input do teclado
Esse campo é uma lista de itens separado por espaços e uma máscara para cada tecla digitada pelo usuário:
```
(d/u)_<keycode>_<time>
```
- **d/u** - Evento (keyup ou keydown)
- **keycode** - Código da tecla mapeada no Javascript
- **time** - Tempo decorrido desde o primeiro botão pressionado

### Processamento das entradas
Para extrair e comparar o tempo entre a digitação, utilizamos uma lista com a diferença de tempo de cada tecla pressionada/tempo:
```
[60, 135, 60, 70, 39, 46, 79, 274, 80, 235, 59, 44, 81]
```
Desta forma, podemos comparar duas listas de maneira fácil utilizando o método de distância de Manhattan ou Euclidiano. Após a comparação usamos o algoritmo KNN para descobrir os vizinhos mais próximos.

### Comparação e resultados
Após as previsões do algoritmo, comparamos com o ID do usuário enviado na chamada do serviço que serviu como referência para trazer os resultados de forma individual

#### Exemplo
![image](https://user-images.githubusercontent.com/42397106/143965562-ce5e1612-e64e-4d1d-9486-55a88cdb2a94.png)

## Melhorias
- Combinar melhor resultados e score
- Treinar diferentes formas de comparação com o algoritmo de IA
- Talvez treinar o algoritmo para usar outros métricas
- Resultado lento e não efetivo com muitos dados distantes
