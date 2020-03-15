import fetchProcedures

def build_input_options(array_of_options):
    choices = ""
    for num, i in enumerate(array_of_options):
        string = convertTuple(i)
        num += 1
        string = f"{num}) {string} \n"
        choices += string
    return choices

def convertTuple(tup): 
    str =  ''.join(tup) 
    return str


