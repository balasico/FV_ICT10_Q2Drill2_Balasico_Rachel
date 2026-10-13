from pyscript import document, display

def new_member(e):

    grade_8 = {'Jayana Tremor'}
    grade_9 = {'Fairy Admat','Kyrie Funtanilla'}
    grade_10 = {'Rachel Balasico','Caitlyn Tano','Hope Benitez','Sammantha Lacuesta','Rocky Saludes'}
    grade_11 = {'Lorenzo Calida','Queeny Ramos'}
    grade_12 = {'Anna Avestruz','Lloyd Gonzales','Elisha Padre'}

    #gets the info from index.html
    first_name = document.getElementById("firstname").value
    last_name = document.getElementById("lastname").value

    new_fellow = first_name + " " + last_name
    new_fellow_again = {new_fellow}

    #combines all the sets
    all_members = grade_8 | grade_9 | grade_10 | grade_11 | grade_12 | new_fellow_again

    #sorts the names alphabetically
    all_members = sorted(all_members)

    #displays the heading
    display("ALL MEMBERS", target="result")

    for member in all_members: display(member, target="result")

    #displays the total number of members
    display("Total Members: " + str(len(all_members)), target="result")