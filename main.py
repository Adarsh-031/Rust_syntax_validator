from lexer import lexer
from parser import parser   
from parser import parse_errors    
from io import StringIO
import sys

def test_input(input_string):
    parse_errors.clear()
    lexer.input(input_string)
    result = parser.parse(input_string)
    if parse_errors:
        print("Parsing failed with errors:")
        for err in parse_errors:
            print(err)
    else:
        print("Parsing succeeded")

# Sample test inputs
inputs = [
    "fn add(x: i32, y: i32) -> i32 { x + y; }",
    "fn multiply(a, b) { a * b }",
    "if x > y { return x; } else { return y; }",
    "if x > y: { x } else { y }", 
    "for i in 0..10 {i; }",
    "for i in range(0, 10) { i }", 
    "let mut counter: i32 = 0;",
    "let y i32 = 10;",  
    "let mut 2count: i32 = 0;", 
    "let result: i32 = add(10, 20);",
    "result = add(10 20);",  
    "add(10, );", 
]

with open("output.txt", "w", encoding="utf-8") as f:
    for input_str in inputs:
        print(f"Testing input: {input_str}")       
        f.write(f"Testing input: {input_str}\n")   
        old_stdout = sys.stdout
        sys.stdout = mystdout = StringIO()
        test_input(input_str)
        sys.stdout = old_stdout
        result_output = mystdout.getvalue()
        print(result_output.strip())
        print()
        f.write(result_output)
        f.write("\n")


