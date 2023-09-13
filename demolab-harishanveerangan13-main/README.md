[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/Uts6x72g)
# Demo Lab

In this lab, we'll learn how to use the Git version control system, how to use the GitHub remote repository system, and we'll submit this assignment to invole the auto-grader for these lab assignments by writing and submitting a simple Python program.

## Getting Started

Install pytest, which is a module for Python that allows you to verify that your code is correct before you submit, using the following command in Windows:

`pip install pytest`

You can use this equivalent command in Linux or MacOS:

`sudo -H pip3 install pytest`

If you have previously installed `pytest`, then you can skip this step.


## Instructions

In this lab, you will edit the `demo_lab.py` file that currently prints `nothing`, and modify the code so that it prints `Hello, world!` instead.

_**Note:** The output has to match exactly, and there will be a newline after each variable output (as is the default for `print()`)._



## Verifying Correctness

Run the pre-written tests that verify that your lab assignment code passes, using the following command:

`pytest --capture=sys`

Examine the output closely.  There should be hints about what went wrong, if any of the tests fail.  If you are struggling to figure it out, you can always ask for help (see __Getting Help__ for details).

## How to Submit

First, ensure that your code passes the tests (see the section __Verifying Correctness__ for details).  If you are certain that your code passes all of the tests, then you can submit your work using the following commands:

```
git add --all
git commit -m "Demo lab completed code"
git push origin main
```

_**Note:** This code is not to be marked.  It is merely for practice so that you know how to use GitHub and GitHub Classroom.  The instructor and TA will not give you any feedback for this demo lab automatically.  If you run into difficulty, please ask one of us for help._

Once you have submitted your work, you can also double check that your auto-grading was successful by clicking on the `Actions` tab in your repository page on GitHub.  Sometimes, this takes a few minutes to complete, so please be patient.