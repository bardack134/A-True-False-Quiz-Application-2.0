
# Definimos una clase llamada QuizBrain
class QuizBrain():
    
    # El método de inicialización que se llama cuando se crea un nuevo objeto de la clase QuizBrain
    def __init__(self, question_list):
        # Inicializamos el número de pregunta a 0
        self.question_number=0
        
        # Asignamos la lista de preguntas proporcionada a la propiedad question_list del objeto
        self.question_list = question_list
        
        # Inicializamos el puntaje a 0
        self.score=0

    # Método para verificar si aún quedan preguntas en la lista de preguntas
    def still_has_question(self):
        
        # Obtenemos la longitud de la lista de preguntas
        length = len(self.question_list)
        
        # Si el número de pregunta es igual a la longitud de la lista de preguntas, significa que hemos terminado el cuestionario
        if self.question_number==length:
            # Imprimimos un mensaje indicando que el cuestionario ha terminado
            print("You have completed the quiz game")
            
            # Imprimimos el puntaje final
            print(f"Your final score was: {self.score}/{length}")
            
            # Retornamos False ya que no quedan más preguntas
            return False
        
        else:
            # Si aún quedan preguntas, retornamos True
            return True       

    # Método para pasar a la siguiente pregunta
    def next_question(self ):
        
        # Obtenemos la pregunta actual de la lista de preguntas
        current_question = self.question_list[self.question_number]
        
        # Incrementamos el número de pregunta
        self.question_number +=1
        
        return f"Q.{self.question_number}: {current_question.text}"
        # # Solicitamos al usuario que responda la pregunta actual
        # user_answer=input(f"Q.{self.question_number}: {current_question.text} (True/False): " )
        
        # # Verificamos si la respuesta del usuario es correcta, y le pasamos los parametros, correct_answer es igual a current_questioon y current_questioon es una lista de objetos
        # self.check_answer(user_answer, correct_answer=current_question.answer)

    # Método para verificar si la respuesta del usuario es correcta, recibe 2 parametros user_answer y correct_answer 
    def check_answer(self, user_answer, correct_answer):
        
        # Si la respuesta del usuario es igual a la respuesta correcta
        if user_answer.lower()==correct_answer.lower():
            
            # Imprimimos un mensaje indicando que la respuesta es correcta
            print("you got it right") 
            # Incrementamos el puntaje
            self.score += 1 
            
        else:
            # Si la respuesta del usuario es incorrecta, imprimimos un mensaje indicando que la respuesta es incorrecta
            print("That's wrong")
            
            # Imprimimos la respuesta correcta
            print(f"The correct answer was {correct_answer}")
            
        # Imprimimos el puntaje actual y el número de la pregunta actual
        print(f"Your current score is {self.score}/ curent question {self.question_number}") 
           
        # Imprimimos una línea en blanco para separar las preguntas
        print()    