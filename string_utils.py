import fetchProcedures


# ["string", id]
def build_input_options(self, array_of_options):
    choices = ""
    choices_matrix = {}
    for num, i in enumerate(array_of_options):
        string = convertTuple(i[0])
        choice_id = i[1]
        num += 1
        string = f"{num}) {string} \n"
        choices += string
        choices_matrix[str(num)] = choice_id
    self.choices_id_matrix = choices_matrix
    return choices

def convertTuple(tup): 
    str =  ''.join(tup) 
    return str



