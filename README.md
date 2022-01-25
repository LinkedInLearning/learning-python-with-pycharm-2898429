# Learning Python with PyCharm
This is the repository for the LinkedIn Learning course Learning Python with PyCharm. The full course is available from [LinkedIn Learning][lil-course-url].

![Learning Python with PyCharm][lil-thumbnail-url] 

PyCharm is a leading tool for Python development. In this course, instructor Mehdi Oulmakki introduces several key best practices for Python development and shows you how to use PyCharm as a one stop shop solution for managing the intricacies of development. First, Mehdi walks you through installing Python and PyCharm and gives you some useful tips and tricks for writing and developing code with PyCharm. He shows you how to create and navigate your projects in the PyCharm UI. Next, Mehdi discusses ways to use PyCharm with Git and GitHub to organize, save, and collaborate on your work. He covers managing dependencies, then goes into facets of code quality, how debugging improves your code quality, and ways to use breakpoints and unit tests for debugging. Plus, Mehdi goes over the principles and purpose of code style and the quality-of-life features within PyCharm that help reformat and refactor your code safely.

## Instructions
This repository has branches for each of the videos in the course. You can use the branch pop up menu in github to switch to a specific branch and take a look at the course at that stage, or you can add `/tree/BRANCH_NAME` to the URL to go to the branch you want to access.

## Branches
The branches are structured to correspond to the videos in the course. The naming convention is `CHAPTER#_MOVIE#`. As an example, the branch named `02_03` corresponds to the second chapter and the third video in that chapter. 
Some branches will have a beginning and an end state. These are marked with the letters `b` for "beginning" and `e` for "end". The `b` branch contains the code as it is at the beginning of the movie. The `e` branch contains the code as it is at the end of the movie. The `main` branch holds the final state of the code when in the course.

When switching from one exercise files branch to the next after making changes to the files, you may get a message like this:

    error: Your local changes to the following files would be overwritten by checkout:        [files]
    Please commit your changes or stash them before you switch branches.
    Aborting

To resolve this issue:
	
    Add changes to git using this command: git add .
	Commit changes using this command: git commit -m "some message"


### Instructor

Mehdi Oulmakki 
                            
Software engineer

                            

Check out my other courses on [LinkedIn Learning](https://www.linkedin.com/learning/instructors/mehdi-oulmakki).

[lil-course-url]: https://www.linkedin.com/learning/learning-python-with-pycharm-14509667
[lil-thumbnail-url]: https://cdn.lynda.com/course/2898429/2898429-1642789960777-16x9.jpg
