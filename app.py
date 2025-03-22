import streamlit as st
import random

def get_questions():
    return [
        {"question": "What is the output of `print(type([]) is list)`?", "options": ["True", "False"], "answer": "True"},
        {"question": "Which method is used to add an element to a set?", "options": ["append()", "add()", "insert()"], "answer": "add()"},
        {"question": "What will `bool([])` return?", "options": ["True", "False"], "answer": "False"},
        {"question": "Which module is used to handle regular expressions in Python?", "options": ["regex", "re", "regexp"], "answer": "re"},
        {"question": "How do you create an empty dictionary?", "options": ["{}", "[]", "dict()"], "answer": "dict()"},
        {"question": "Which of these data types is immutable?", "options": ["List", "Set", "Tuple"], "answer": "Tuple"},
        {"question": "What does `open('file.txt', 'w')` do?", "options": ["Reads file", "Deletes content and writes", "Appends to file"], "answer": "Deletes content and writes"},
        {"question": "Which of the following is a correct way to create a frozenset?", "options": ["set([])", "frozenset([])", "immutable_set([])"], "answer": "frozenset([])"},
        {"question": "What does `set([1,2,2,3])` return?", "options": ["{1,2,3}", "[1,2,3]", "{1,2,2,3}"], "answer": "{1,2,3}"},
        {"question": "What is the default return type of `input()` function?", "options": ["int", "str", "float"], "answer": "str"},
    {"question": "What is the output of 3 * 3?", "options": ["6", "9", "12", "15"], "answer": "9"},
    {"question": "Which keyword is used to define a function in Python?", "options": ["func", "define", "def", "function"], "answer": "def"},
    {"question": "What will be the output of: print(type([]))?", "options": ["list", "tuple", "dict", "set"], "answer": "list"},
    {"question": "Which of the following is immutable?", "options": ["list", "dict", "tuple", "set"], "answer": "tuple"},
    {"question": "What does the 'break' keyword do in a loop?", "options": ["Skips iteration", "Exits loop", "Continues loop", "Throws error"], "answer": "Exits loop"},
    {"question": "What is the output of bool([])?", "options": ["True", "False"], "answer": "False"},
    {"question": "Which method is used to remove an item from a list by value?", "options": ["pop()", "remove()", "discard()", "delete()"], "answer": "remove()"},
    {"question": "What is the purpose of the 'pass' statement?", "options": ["Skip iteration", "Exit loop", "Do nothing", "Throw error"], "answer": "Do nothing"},
    {"question": "Which operator is used for exponentiation in Python?", "options": ["^", "**", "//", "%%"], "answer": "**"},
    {"question": "Which of the following is a correct way to open a file for writing?", "options": ["open('file.txt', 'w')", "open('file.txt', 'r')", "open('file.txt', 'a')", "open('file.txt', 'x')"], "answer": "open('file.txt', 'w')"},
    {"question": "How do you create a dictionary?", "options": ["dict = {}", "dict = []", "dict = ()", "dict = ''"], "answer": "dict = {}"},
    {"question": "Which function is used to get the length of a list?", "options": ["size()", "len()", "count()", "length()"], "answer": "len()"},
    {"question": "Which statement is used to exit a function?", "options": ["exit", "break", "continue", "return"], "answer": "return"},
    {"question": "What is the output of '5' + '5' in Python?", "options": ["10", "55", "Error", "None"], "answer": "55"},
    {"question": "What does 'is' operator compare?", "options": ["Values", "Memory addresses", "Data types", "Length"], "answer": "Memory addresses"},
    {"question": "Which method is used to convert a string to uppercase?", "options": ["upper()", "capitalize()", "toUpper()", "touppercase()"], "answer": "upper()"},
    {"question": "What does 'lambda' define?", "options": ["Anonymous function", "Loop", "Class", "Module"], "answer": "Anonymous function"},
    {"question": "Which function converts a string to an integer?", "options": ["int()", "str()", "float()", "bool()"], "answer": "int()"},
    {"question": "What is the output of range(2, 10, 2)?", "options": ["[2, 4, 6, 8, 10]", "[2, 4, 6, 8]", "[2, 3, 4, 5, 6, 7, 8, 9]", "None"], "answer": "[2, 4, 6, 8]"},
    {"question": "Which keyword is used to create a class?", "options": ["class", "define", "struct", "object"], "answer": "class"},
    {"question": "What will 'set([1,2,2,3])' return?", "options": ["{1,2,3}", "[1,2,3]", "{1,2,2,3}", "None"], "answer": "{1,2,3}"},
    {"question": "How do you check if 'x' is greater than 'y'?", "options": ["x => y", "x > y", "x =< y", "x < y"], "answer": "x > y"},
    {"question": "What will be the output of print(bool(0))?", "options": ["True", "False", "Error", "None"], "answer": "False"},
    {"question": "Which function is used to read user input?", "options": ["get()", "input()", "read()", "scan()"], "answer": "input()"}
]
    

def quiz_app():
    st.title("Python Quiz App 🧠")
    
    name = st.text_input("Enter your Name:")
    email = st.text_input("Enter your Email:")
    slot = st.text_input("Enter your Slot:")
    
    if not name or not email or not slot:
        st.warning("Please fill in all details to proceed.")
        return
    
    questions = random.sample(get_questions(), 20)  # Random 250 questions
    user_answers = {}
    
    for i, q in enumerate(questions):
        st.write(f"**Q{i+1}: {q['question']}**")
        user_answers[i] = st.radio("Select an option:", q["options"], key=i)
    
    if st.button("Submit Quiz"):
        correct_count = sum(1 for i, q in enumerate(questions) if user_answers[i] == q["answer"])
        st.success(f"You got {correct_count}/{len(questions)} correct!")
        
        st.subheader("Correct Answers:")
        for i, q in enumerate(questions):
            st.write(f"**Q{i+1}: {q['question']}** - ✅ {q['answer']}")

if __name__ == "__main__":
    quiz_app()
