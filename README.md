This repo contains work relevant to two parts of my coursework for CS3012:

A): GitHub Access - “Interrogate the GitHub API to retrieve and display data regarding the logged in developer”

B): Social Graph - “Interrogate the GitHub API to build visualisation of data available that elucidates some aspect of the software engineering process, such as a social graph of developers and projects, or a visualisation of individual or team performance”

My language of choice for this project was Python, and I used PyGithub to access and interrogate the GitHub API. I was originally going to use JavaScript and create a display on a webpage, but having had bad experiences with trying to get JS to work fully in the past, I elected instead to  try to make it in Python. This was a decidedly good choice in hindsight, as it gave me a chance to gain a better knowledge to a language I was unfamiliar with but had wanted to get a chance to use for a while. To create my graphs I made use of the PyGal Library; this was another good choice as it greatly simplified my workflow for this project. 

If you open the svg files in new tabs, they should become interactive (i.e. you should be able to highlight
different parts/be able to make some components invisible by clicking on their corresponding boxes)

# GithubSocialGraph
Creation of a Social Graph derived from user data accessed using the GitHub API - Part of my Software Engineering coursework


# GithubAccess

The relevant commit for this portion of the assignment can be found at commit c14579cad3e4813e067cd265a604e6ba66c81ea6,
and the folder that contains the basic code also includes a screenshot for proof of it working.

According to the course website, the goal to be achieved for this was to "Interrogate the GitHub API to retrieve and display data
regarding the logged in developer". In order to satisfy the requirements of this assignment, I wrote a basic program that
accesses the names of all repos that the logged in user has, and displays the name of each repo and their most recent commit.

# Social Graph

The relevant commit for this portion of my work can be found at commit
a41861350e0775ba9697ee7ffcb047e2085b0196. All files relevant to this portion of my work can be found in the GithubAccess folder. Before setting out to work on this task, I thought about a couple of different possibilities for what could be implemented. My first thought was to try to make something along the lines of metrics similar to those used in industry for developing metrics on engineers. I then also thought about creating a display that could provide some information on the people taking CS3012 this year. This idea was soon dropped when I decided that it might be better to retrieve data that isn’t as close to home as that. The theme I settled on in the end was to compare the 10 most popular repos for a series of languages. This gradually developed into a comparison of languages revolving around the comparison of related languages: for example, I made a graph comparing the popularity of three less popular languages - Prolog, Brainfuck, and COBOL.

In order to reduce the monotony of creating these visualisations, I made use of several different types of graphs which can be found in the PyGal library, such as Pie Charts, Bar Graphs, and Line Graphs.

In order to set about on this project, I had to decide on a metric that could be used to determine the popularity of a particular repo. I learned that the default PyGithub query for a language returns repos based on the number of stars they have. I thought this was a valid metric and reasoned that it would be a reasonable way of determining which repos I would need to consider. After deciding on this, I then went on to retrieve the star counts and names of the top 10 repos for a plethora of languages:

	- Java
	- Python
	- Prolog
	- Brainfuck
	- COBOL
	- HTML
	- CSS
	- JavaScript
	- PHP
	- FORTRAN
	- LISP
	- Smalltalk

After retrieving this information, I then thought about the most suitable way to compare these languages to one another. For Java and Python, I decided that it would be best to isolate them and compare the 10 repos for both of these languages against one another. For Java, I created the svg file javaBarchart, and for Python I made pyPie.svg.

My next visualisation to implement was a comparison in the popularity of some less commonly-used languages. For this, I chose Prolog, Brainfuck, and COBOL. I found the differences between the results interesting for this, as COBOL had the most popular repos, but only 3 of them were popular, with the other 7 being the least popular repos in the entire graph. Prolog had a very sustainable popularity - 7 of the 10 repos sampled for this had nearly equal popularity. Brainfuck also held its own surprisingly well despite being a very obscure and impractical language.

I then created 2 more comparisons - one of some of the most popular web development languages (HTML, CSS, JavaScript, and PHP), and another for older programming languages ( FORTRAN, COBOL, LISP, and Smalltalk).
