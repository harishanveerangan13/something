import demo_lab
import sys

# This function tests your lab 01 code, ensuring that it prints the correct output
def test_main(capsys):
    demo_lab.main() # run the student's code
    
    captured = capsys.readouterr()
    sys.stderr.write('actual output:\n')
    sys.stderr.write(captured.out + '\n')

    correct_output = 'Hello, world!\n'
    sys.stderr.write('correct output:\n')
    sys.stderr.write(correct_output + '\n')
    assert captured.out == correct_output # verify that the output is a match
