# Importamos la función unescape del módulo html para convertir las entidades HTML en sus caracteres correspondientes
import html

# Importamos todos los elementos del módulo data
from data import *

# Importamos todos los elementos del módulo question_model
from question_model import *

# Importamos todos los elementos del módulo quiz_brain
from quiz_brain import *

from user_interface import QuizInterface


# Creamos una lista vacía llamada question_bank, que sera una lista de objetos
question_bank=[]

# Iteramos sobre cada diccionario en la lista question_data
for  diccionary in question_data:
    
    # Convertimos las entidades HTML "&quot" en el texto de la pregunta a sus caracteres correspondientes
    diccionary["question"]=html.unescape(diccionary["question"])
    
    # Creamos un nuevo objeto de la clase Question con los valores asociados a las claves "question" y "correct_answer" en el diccionario actual
    new_question=Question(text=diccionary["question"], answer=diccionary["correct_answer"])
    
    # Añadimos el nuevo objeto Question a la lista question_bank
    question_bank.append(new_question)

#  Imprimimos la respuesta asociada al primer objeto de la lista question_bank
# print(question_bank[0].answer)    


# Creamos un nuevo objeto de la clase QuizBrain y le pasamos la lista de preguntas question_bank
quiz=QuizBrain(question_list=question_bank)


#creando objeto de la clase Quizinterface, recibe como paremetro el objeto de la clase QuizBrain
quiz_interface=QuizInterface(quiz)


# # Mientras aún queden preguntas en el cuestionario
# while quiz.still_has_question():
    
#     # Pasamos a la siguiente pregunta
#     quiz.next_question()