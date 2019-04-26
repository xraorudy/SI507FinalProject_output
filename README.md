# Parks Data System

Rudy Rao
[Link to this repository](https://github.com/xraorudy/SI507FinalProject_output)

---

## Project Description

My project will use the data from the national park database and write the information into csv file for reader's reference. This project will provid the text information(i.e. Name, Type, Location, and Text Description) to the users and they can get specific information they want by the file. And also we will provide the interation function to customize the page input by the users. They can save the parks which they are interested into the Flask application.  The project will allow users to use two ways to input informations in different states and see all the parks' information they have inputted in one page. What’s more, the users also can learn some numbers in one page(i.e. the total number of saved park)

## How to run

1. First, you should install all requirements with `pip install -r requirements.txt`
2. Second, you should run it by gitbash terminal, locating the file route and entering 'python SI507project_code'.

## How to use

1. Run the 'SI507project_code.py' and it would create a csv file 'park_data.csv'.
2. Open the 'park_data.csv' and find your interesting park information.
3. Open the homepage url in your brower and copy & paste the information you find in csv file. Or you can also input the data from a book, internet or anything you think is reliable.
3. Change the url or click the link of each page to explore it. (Pictures of each route are in the parts below)

## Routes in this application
- `/home/` -> this is the home page which is a human computer interaction page(See the picture below) The user should input the data which is from the csv file or created by himself to make the data saved. In the corner of the page, it shows total saved park "Now <n> parks saved." When you click submit button, the page will redirect to '/new_park' route. And you also can clik the two redirecting link, 'Click here to see all parks' and 'Click here to see all states' to other two route.</p>
![image](https://github.com/xraorudy/SI507FinalProject_output/blob/master/pictures/HomePage.JPG)
- `/all_parks/` -> This route will show a list of the parks’ name and type of all the parks in the database. It will show the type, name and state of each park saved.</p>
![image](https://github.com/xraorudy/SI507FinalProject_output/blob/master/pictures/all_parks.JPG)
- `/all_states/ ` -> This route will show the data classfied by state. It will show how many parks in each state for each state(only state which has been input) "<State and location> has <number> parks/park"</p>
![image](https://github.com/xraorudy/SI507FinalProject_output/blob/master/pictures/all_states.JPG)
- `/new_park/` -> This page CAN NOT be opened by URL links. It only shows up when you submit your data in the home page. It would shows what you have input in a organized format. "New Park: <name of the park> in <State and Location> and its type is 'Type'. <Description>"</p>
![image](https://github.com/xraorudy/SI507FinalProject_output/blob/master/pictures/new_park.JPG)
- `/new/park/<name>/<state>/<type>/<description>` -> This is another way to create new park in the database by URL link. You should put the same inforamtion as home page and it will also redirect to the "/new_park/"page.</p>
![image](https://github.com/xraorudy/SI507FinalProject_output/blob/master/pictures/another%20way%20to%20add.JPG)


## How to run tests
1. First, you should run the SI507project_code file to create correspondingly file(i.e. json file)
2. Input the data from csv file for 5-10 items or whatever you like and try to inlude as many as different kinds of types and states.
3. Run the specific test file
![image](https://github.com/xraorudy/SI507FinalProject_output/blob/master/pictures/test.JPG)
## In this repository:
- Database
  - DatabaseDesign.JPG
  - DatabaseDesign.pptx
- pictures
  - HomePage.JPG
  - all_parks.JPG
  - all_states.JPG
  - another way to add.JPG
  - new_park.JPG
- templates
  - all_parks.html
  - all_states.html
  - bootstrap.css
  - index.html
  - parks_description_template.html
  - save_park.html
  - saved_park.html
- README.md
- SI507project_code.py
- SI507project_tests.py
- SI507project_tools.py
- advanced_expiry_caching.py
- finalproject_cache.json
- park_data.csv
- requirements.txt
- sample_parks.db



## Code Requirements for Grading
Please check the requirements you have accomplished in your code as demonstrated.
- [x] This is a completed requirement.
- [ ] This is an incomplete requirement.

Below is a list of the requirements listed in the rubric for you to copy and paste.  See rubric on Canvas for more details.

### General
- [x] Project is submitted as a Github repository
- [x] Project includes a working Flask application that runs locally on a computer
- [x] Project includes at least 1 test suite file with reasonable tests in it.
- [x] Includes a `requirements.txt` file containing all required modules to run program
- [x] Includes a clear and readable README.md that follows this template
- [x] Includes a sample .sqlite/.db file
- [x] Includes a diagram of your database schema
- [x] Includes EVERY file needed in order to run the project
- [x] Includes screenshots and/or clear descriptions of what your project should look like when it is working

### Flask Application
- [x] Includes at least 3 different routes
- [x] View/s a user can see when the application runs that are understandable/legible for someone who has NOT taken this course
- [x] Interactions with a database that has at least 2 tables
- [x] At least 1 relationship between 2 tables in database
- [x] Information stored in the database is viewed or interacted with in some way

### Additional Components (at least 6 required)
- [ ] Use of a new module
- [ ] Use of a second new module
- [ ] Object definitions using inheritance (indicate if this counts for 2 or 3 of the six requirements in a parenthetical)
- [ ] A many-to-many relationship in your database structure
- [x] At least one form in your Flask application
- [x] Templating in your Flask application
- [x] Inclusion of JavaScript files in the application
- [x] Links in the views of Flask application page/s
- [ ] Relevant use of `itertools` and/or `collections`
- [x] Sourcing of data using web scraping
- [ ] Sourcing of data using web REST API requests
- [x] Sourcing of data using user input and/or a downloaded .csv or .json dataset
- [x] Caching of data you continually retrieve from the internet in some way

### Submission
- [x] I included a link to my GitHub repository with the correct permissions on Canvas! (Did you though? Did you actually? Are you sure you didn't forget?)
- [x] I included a summary of my project and how I thought it went **in my Canvas submission**!
