from pyscript import display, document # pyright: ignore[reportMissingImports]

subjects_list = ['English', 'Math', 'Social Studies', 'Music', 'PE', 'VE'] # specifying list

number_of_units = 5, 5, 3, 1, 1, 1

total_units = 16

def student_gwa(e):
    document.getElementById("output").innerHTML = " " 

    eng_grade = float(document.getElementById('english').value)
    eng_result = eng_grade * 5

    math_grade = float(document.getElementById('math').value)
    math_result = math_grade * 5

    ss_grade = float(document.getElementById('ss').value)
    ss_result = ss_grade * 3

    music_grade = float(document.getElementById('music').value)
    music_result = music_grade * 1

    pe_grade = float(document.getElementById('pe').value)
    pe_result = pe_grade * 1

    ve_grade = float(document.getElementById('ve').value)
    ve_result = ve_grade * 1

    sum = ((eng_result + math_result + ss_result + music_result + pe_result + ve_result) // total_units)

    first_name = document.getElementById('fname').value
    last_name = document.getElementById('lname').value

    display(f'Name: {first_name} {last_name}', target='output')
    display(f'Your GWA is: {sum}', target='output') 