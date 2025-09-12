
Encuesta de Ideas de Proyecto 
Este programa en Python permite realizar una encuesta a estudiantes para recopilar sus ideas de proyectos para el curso.
Las respuestas se almacenan y luego se muestran en un resumen de resultados junto con un conteo de las ideas propuestas.

 Características
Registro de nombre, edad e idea de proyecto de cada estudiante.

Muestra una tabla con todos los resultados ingresados.

Genera un resumen de ideas, contando cuántos estudiantes propusieron la misma.

Se ejecuta para 9 estudiantes de manera predeterminada.

 Ejecución
El programa pedirá interactivamente los datos de cada estudiante (nombre, edad e idea de proyecto).

Al finalizar:

Se mostrarán los resultados en tabla.

Se generará un resumen con el conteo de votos por idea.

 Estructura del Código
Clase Estudiante: Representa a cada estudiante con sus datos.

Clase Encuesta:

Contiene las preguntas y respuestas.

Métodos principales:

agregar_respuesta(): Agrega una nueva respuesta.

mostrar_resultados(): Muestra todas las respuestas en una tabla.

resumen(): Cuenta y resume las ideas de proyecto.

Función ejecutar_encuesta(): Ejecuta la encuesta para 9 estudiantes.

Bloque principal (if __name__ == "__main__":): Inicia la ejecución del programa.



 Ejemplo de salida
 # encuesta a un solo estudiante 
 
ENCUESTA A ESTUDIANTES
¿Cuál es tu nombre?: wilman             ¿Cuál es tu edad?: 18
¿Qué idea para el proyecto tienes?:blioteca virtual
Respuesta de wilman guardada.

 Resultados de la Encuesta
Nombre          Edad  Idea_Proyecto     
--------------------------------------------------
wilman          18    blioteca virtual  

Resumen de Ideas de Proyecto
Idea 'Blioteca virtual': 1 voto(s)



# nota NO PUDE COLOCAR LA CAPTURA DE LA SALIDA DEL VOD
