from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR="#375362"


#TODO: vamos a crear la interfaz grafica usando tinker con OOP
class QuizInterface:
    
    #nuestra clase recibe como parametro un objeto de la clase QuizBrain
    def __init__(self, quiz: QuizBrain):
        
        #esta propiedad recibe como valor un objeto de la clase QuizBrain
        self.quiz = quiz
        
        #ventana
        self.window=Tk()       
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)        
        self.window.title("Quiz Interface") #titulo dela ventana
        
        
        #creando objeto canvas
        self.canvas=Canvas(width=300, height=250, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        
        
        #creando texto donde iran nuestras preguntas
        self.question_text=self.canvas.create_text(150, 125, text="Question", font=("Arial", 20, "italic"), fill=THEME_COLOR, width=280)
        
        
        true_photo=PhotoImage(file="images/true.png")
        false_photo=PhotoImage(file="images/false.png")
        
        
        #creando botones (true, false)
        self.true_button=Button(image=true_photo, highlightthickness=0, command=self.answer_true)
        self.true_button.grid(row=2, column=0, padx=20, )
        
        
        self.false_button=Button(image=false_photo, highlightthickness=0, command=self.answer_false)
        self.false_button.grid(row=2, column=1, padx=20, )
        
        
        #score text
        self.score=Label(text="Score: 0", bg=THEME_COLOR, fg="white" )
        self.score.grid(row=0, column=1 )
        
        
        #llamamos a la funcion de nuestras preguntas, para que al correr el codigo nos muestre una preguntilla 
        self.get_next_Question()
        
        
        self.window.mainloop()
        
        
    def get_next_Question(self):
        
        #tenemos apenas 10 preguntas a responder, porlo que evaluamos con el metodo still_has_question, si quedan preguntas or not
        if self.quiz.still_has_question()==True:
            #ya podemos acceder por medio de nuestra propiedad, a la funcion next_question() de la clase QuizBrain
            self.question=self.quiz.next_question()
            
            
            #actualizamos nuestro canvas con la nueva preguntilla
            self.canvas.itemconfigure(self.question_text, text=self.question)
        
        
        else:
            #indicamos al usuario que se acabaron las preguntas
            self.canvas.itemconfigure(self.question_text, text=f"End of the questions. Total Score= {self.quiz.score}/10")
            
            
            #desactivamos los botones, ya que no hay mas questions
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
            
            
            
    #funcion que se llama cuando oprimo el boton "True" - "green checkmark"
    def answer_true(self):
        
        #chequiamos si la respuesta del user es correcta o incorrecta, este metodo de QuizBrain recibe 2 parametros user_answer y correct_answer 
        correct_or_incorrect=self.quiz.check_answer(user_answer="True", correct_answer=self.quiz.current_question.answer)

        
        #actualizamos nuestro score, puntaje
        self.score.config(text=f'Score: {self.quiz.score}')
                      
        
        self.give_feedback(correct_or_incorrect)
        
              
        #llamamos a la sgt pregunta
        self.get_next_Question()

        
    #funcion que se llama cuando oprimo el boton "False" - "Red mark"
    def answer_false(self):
        
        #chequiamos si la respuesta del user es correcta o incorrecta, este metodo recibe 2 parametros user_answer y correct_answer 
        correct_or_incorrect=self.quiz.check_answer(user_answer="False", correct_answer=self.quiz.current_question.answer)
        
        
        #actualizamos nuestro score, puntaje
        self.score.config(text=f'Score: {self.quiz.score}')
        
        
        self.give_feedback(correct_or_incorrect)
        
        
        #llamamos a la sgt pregunta
        self.get_next_Question()
        
        
    #funcion que ledara feedback al user, mostrando color verde si respondio correctamente y rojo si respondio incorrectamente           
    def give_feedback(self, correct_or_incorrect ):
        
        #esta variable contiene un valor booleano resultado del metodo checkanswer de QuizBrain class
        if correct_or_incorrect==True:
            
            #si respondio correctamente canviamos color del background de canvas a verde
            self.canvas.configure(bg="green")
        
            
        else:
            #si respondio incorrectamente canbiamos color del background de canvas a rojo
            self.canvas.configure(self.canvas, bg="red")
            
            
        self.window.after(1000, lambda:self.canvas.configure(bg="white"))
            
    