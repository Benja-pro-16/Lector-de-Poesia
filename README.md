# Lector-de-Poesia
Es una app con el principio de Text to Speech, donde se puede subir texto y convierte a un archivo de audio.
Cuenta con una base de datos para probar las funcionalidades, tambien se pueden subir todo tipo de texto.
Para ello se debe seleccionar ** subir poema** y debe suministrar un titulo, luego el texto y pulsar el boton ** agregar ** para que se suba el texto a la base de datos.
Para generar el audio, se debe seleccionar ** recitame tus poesias ** y elegir por titulo el texto a convertir a audio. Luego de elegir el titulo, se presiona ** Generar audio ** y se generara un archivo mp3, tambien con el toggle es posible ver el texto para poder seguir el audio.
Los titulos y los textos se guardan en una base de datos sql, mientras que el archivo de audio es siempre el mismo que se va sobreescribiendo en cada seleccion.

Al usar la libreria GTTS, es necesaria la conexion a internet.
