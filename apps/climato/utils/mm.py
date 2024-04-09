import requests
from textx import metamodel_from_str


class MeteoMatch:
    def __init__(self):
        self.id = 1
        self.time_begin = [2020, 1, 1]
        self.time_end = [2020, 1, 1]
        self.contraintes_temp = []
        self.contraintes_time = []

    def __str__(self):
        # return f"Initialisation pour la balise {self.id} sur la période du {self.time_begin} au {self.time_end})."
        return ""

    def interpret(self, model):
        # model is an instance of Program
        for c in model.requests:
            if c.__class__.__name__ == "Init":
                self.id = c.id
                self.time_begin = [c.aaaa, c.mm, c.jj]
                self.time_end = [c.aaaa_end, c.mm_end, c.jj_end]
                print(
                    f"Initialisation à la borne : {self.id} sur la période du {self.time_begin} au {self.time_end}"
                )

            elif c.__class__.__name__ == "Temp":
                self.contraintes_temp.append(
                    [c.vals.lval, c.vals.hval, c.time.lval, c.time.hval]
                )
                print(f"Contraintes temp: {self.contraintes_temp}")
            else:
                self.contraintes_time.append(
                    [c.vals.lval, c.vals.hval, c.time.lval, c.time.hval]
                )
                print(f"Contraintes time: {self.contraintes_time}")


def translate(criteria: str):
    grammar = """
MeteoMatchModel: requests*=Request;
Request: (Init | Temp | Pp) ';'; 
Init: 'Init station 'id=INT 'pour periode de 'aaaa=INT'-'mm=INT'-'jj=INT 'à 'aaaa_end=INT'-'mm_end=INT'-'jj_end=INT;
Temp: 'temp dans' vals=Interval 'pdt' time=Interval;
Pp: 'pp dans' vals=Interval 'pdt' time=Interval;
Interval: '['lval=INT','hval=INT']';
Value: INT;"""
    mm = MeteoMatch()
    mm_meta = metamodel_from_str(grammar)
    mm_model = mm_meta.model_from_str(criteria)
    mm.interpret(mm_model)
    return mm


if __name__ == "__main__":
    example = """
    Init station 1 pour periode de 2020-01-10 à 2022-01-10;  
    temp dans [0, 1] pdt [0, 5]; 
    temp dans [10, 20] pdt [6, 10]; 
    pp dans [2, 1] pdt [6, 10]; """
    translate(example)
