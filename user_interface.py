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
        self.true_button=Button(image=true_photo, highlightthickness=0)
        self.true_button.grid(row=2, column=0, padx=20, )
        
        
        self.false_button=Button(image=false_photo, highlightthickness=0)
        self.false_button.grid(row=2, column=1, padx=20, )
        
        
        #score text
        self.score=Label(text="Score: 0", bg=THEME_COLOR, fg="white" )
        self.score.grid(row=0, column=1 )
        
        
        #llamamos a la funcion de nuestras preguntas, para que al correr el codigo nos muestre una preguntilla 
        self.get_next_Question()
        
        
        self.window.mainloop()
        
        
    def get_next_Question(self):
        
        #ya podemos acceder por medio de nuestra propiedad, a la funcion next_question() de la clase QuizBrain
        self.question=self.quiz.next_question()
        
        
        #actualizamos nuestro canvas con la nueva preguntilla
        self.canvas.itemconfigure(self.question_text, text=self.question)