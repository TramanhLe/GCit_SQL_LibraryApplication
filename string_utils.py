def build_input_options(array_of_options):
    choices = ""
    for num, i in enumerate(array_of_options):
        num += 1
        string = f"{num}) {i} \n"
        choices += string
    return choices