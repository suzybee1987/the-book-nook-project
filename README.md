# The Book Nook

![GitHub contributors](https://img.shields.io/github/contributors/suzybee1987/the-book-nook-project)
![GitHub last commit](https://img.shields.io/github/last-commit/suzybee1987/the-book-nook-project)
![GitHub language count](https://img.shields.io/github/languages/count/suzybee1987/the-book-nook-project)
![GitHub top language](https://img.shields.io/github/languages/top/suzybee1987/the-book-nook-project)

## About

**The Book Nook** is an interactive book review site aimed at book lovers looking to find reviews on books they are interested in reading and allows them to leave reviews for ones they have read. The site is designed to be responsive and easy to navigate on a range of devices to make it accessible for book lovers. 

Link to [live site]

## **Contents**

- [**UX (User Experience)**](#ux-user-experience)
  - [**User Stories**](#user-stories)
  - [**Site Owner Goals**](#site-owner-goals)
- [**Design Choices**](#design-choices)
  - [**Fonts**](#fonts)
  - [**Colours**](#colours)
  - [**Imagery**](#imagery)
  - [**Wireframes**](#wireframes)
- [**Technologies**](#technologies)
  - [**Languages**](#languages)
  - [**Database**](#database)
  - [**Libraries**](#libraries)
  - [**Tools**](#tools)
- [**Features**](#features)
  - [**Features Implemented**](#features-implemented)
  - [**Future Features**](#future-features)
  - [**Responsive Design**](#responsive-design)
- [**Version Control**](#version-control)
- [**Testing**](#testing)
- [**Deployment**](#deployment)
  - [**Running Locally**](#running-locally)
- [**Credits**](#credits)
  - [**Code**](#code)
  - [**Content**](#content)
  - [**Images**](#images)
  - [**Inspiration**](#inspiration)
  - [**Acknowledgements**](#acknowledgements)
  

## **UX (User Experience)**


### **User Stories**
- As a first time user
    - I would like to find books to read based on their reviews
    - I


- As a returning user


- As a frequent user


- All users
    - I want the site to have links to websites where I can buy the book I am interested in.
    - I want the site to be easy to navigate on mobile primarily so I can use it on the go.
    - I want the site to be responsive on all devices.
    - I also want to be able to contact the site owner with feedback.


### **Site Owner Goals** 
- Earn money on each book purchased via a link from the site.
- I want the site to be responsive on all devices for the best user experience to encourage customers to return. 


[Back to contents](#contents)


## **Design Choices**


### **Fonts**




### **Colours**



### **Imagery**



### **Wireframes**

The wireframes were created using [Adobe XD](https://www.adobe.com/uk/products/xd.html) and can be found in pdf form in [wireframes](wireframes)


- Desktop view
  - [Home](wireframes/desktop_home.png)
  - [Log In](wireframes/desktop_log_in.png)
  - [Register](wireframes/desktop_register.png)
  - [Add Review](wireframes/desktop_add_review.png)
  - [Edit Review](wireframes/desktop_edit_review.png)
  - [My Reviews](wireframes/desktop_my_reviews.png)


- Mobile view
  - [Home](wireframes/mobile_home.png)
  - [Menu](wireframes/mobile_menu.png)
  - [Log In](wireframes/mobile_log_in.png)
  - [Add Review](wireframes/mobile_add_review.png)
  - [Edit Review](wireframes/mobile_edit_review.png)
  - [My Reviews](wireframes/mobile_my_reviews.png)



[Back to contents](#contents)


## **Technologies**


### **Languages**

- [HTML5](https://developer.mozilla.org/en-US/docs/Web/HTML)
  - Used as the main markup language for the website content.
- [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS)
  - Used to style the individual webpages.
- [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
    - Used to show the questions through pagination and for the game play.
- [Python 3](https://www.python.org/)
    - Used to run the site and database

### **Database**

- [MongoDB Atlas](https://www.mongodb.com/)
    - Cloud based database to hold the user and book review documents


### **Libraries**

- [Materialize](https://materializecss.com/)
    - Used to design a mobile-first responsive website layout along with custom components. 
- [jQuery](https://developer.mozilla.org/en-US/docs/Glossary/jQuery) 
    - Used for initialisation for Materialize CSS components.
- [Flask](https://palletsprojects.com/p/flask/)
    - Used as a lightweight WSGI web application framework
- [Werkzeug](https://werkzeug.palletsprojects.com/en/2.0.x/#)
    - A comprehensive WSGI web application library. 
- [ItsDangerous](https://palletsprojects.com/p/itsdangerous/)
    - Allows data to be sent and received safely using Python and secret keys
- [PyMongo](https://pymongo.readthedocs.io/en/stable/)
    - Python distribution containing tools for working with MongoDB
- [Flask-PyMongo](https://flask-pymongo.readthedocs.io/en/latest/)
    - Flask-PyMongo bridges Flask and PyMongo
- [DNSPython](https://www.dnspython.org/)
    - A DNS toolkit for Python
- [Jinja2](https://palletsprojects.com/p/jinja/)
    - Jinja2 is a full-featured template engine for Python


### **Services**

- [emailJS](https://www.emailjs.com/) 
    - Used with the contact form to receive the comments from users
  

### **Tools**

- [Git](https://git-scm.com/)
  - Git was used for version control (commit to Git and push to GitHub).
- [GitHub](https://github.com/)
  - Used to store, host and deploy the project files and source code after being pushed from Git. I also used it for the Project Kanban board to keep track and split tasks into smaller tasks to make them easier to fulfill.
- [Gitpod](https://www.gitpod.io/)
  - An online IDE linked to the GitHub repository used to write my code.
- [Heroku](https://www.heroku.com/home)
    - A Cloud Application Platform used to deploy the site
- [JSHint](https://jshint.com/)
    - Used to detect errors in the JavaScript files
- [PEP8 Online](http://pep8online.com/)
    - Used to check PEP8 compliance in the code
- [W3C Markup Validator](https://validator.w3.org/)
    - Markup validation service for HTML5
- [Jigsaw Validator](https://jigsaw.w3.org/css-validator/)
    - CSS3 Validation Service
- [Neon Project](https://thenounproject.com/)
  - For the images of the characters and spinning turtle home button
- [Google fonts](https://fonts.google.com/)
  - Used to compare and choose fonts. 
- [Coolors](https://coolors.co/)
  - Used to research and choose the colour scheme by comparing and contrasting similar colours in the generator.
- [Favicons](https://favicon.io/)
  - Used to generate a favicon for the website title.
- [Lighthouse](https://developers.google.com/web/tools/lighthouse)
  - Used to audit the site for quality and ensure responsiveness.
- [amiresponsive](http://ami.responsivedesign.is/)
  - An online tool to check how responsive the site is on different devices.
- [tinypng](https://tinypng.com/)
  - Used to reduce the size of the images for better user experience.


[Back to contents](#contents)

## **Features**

### **Features Implemented**

Features relevant to all pages:

- **Header**
    - Contains the navigation links and is fixed to the top of the page for easy use on all devices.
    - Mobile Side View navigation
    - The home button is on the left side of the header and sections of the page listed on the right where a user would expect them to be.
    - Navigation links are underlined or animated when the user hovers over them to give feedback that they have hovered over the right spot.
    - The navbar is semi-transparent to allow the user to enjoy the full length of the hero images.
    - The colour scheme is designed to be easy to read with the contrast and the ratio tested on Google Dev Tools.

  
- **Footer** 


#### Home Page

-
    -




#### Contact Page

- **Contact form**
    - For the user to give feedback these fields are required: Name, Email and comments and show error messages if not filled before clicking submit. Once the user fills out this section an email is sent to my inbox with the details and the user receives confirmation via alert on window to confirm their email has been sent. 
    - On the form the buttons are as a user would expect there is a submit and reset button on the form with the Reset button having more muted colours and Submit button the obvious choice for the user to select upon filling out the form.  


#### *404.html*

 - **Button**
    - On the 404.html page the button redirects the user back to Home Page to prevent them having to press the browser back button for better user experience. 

### **Future Features**



### **Responsive Design**

- Materialize CSS columns were used to make the site responsive on all devices and viewport height adjusted for the best user experience

[Back to contents](#contents)


## **Version Control**

**Version control** was managed within **GitHub** and **Gitpod** and regular commits pushed to **GitHub**. 
See below for how this was managed:

### Gitpod Workspaces
1. Starting from GitHub clone the [Code Institute template](https://github.com/Code-Institute-Org/gitpod-full-template) by clicking Use This Template and copying to my repository under the name ms1-ali-shiatsu. The workspace is then launched by clicking GitPod - this action only needs to be performed once and then workspace reopened from GitPod.
2. Start the Gitpod Workspace which opens an **online IDE editor** window.

### Gitpod branching and committing to GitHub
1. I created various branches to work on different sections of code to push to master. I did this by typing into the terminal the commands: *git status* to find out which branch currently on; *git switch -c <*branchname*>* to create a new branch and switch to it immediately and then once the work was completed on that branch typed *git add <*files to be added*>* , *git commit -m <*commit message*>* and *git push --set-upstream <*remote*> <*branchname*>* to push to GitHub. I then created a pull request to pull the changes to the master if happy with the changes. From this point I would use *git -d <*branchname*>* to delete the local branch and delete the remote branch on GitHub. 
2. Meaningful commit messages were used to allow to roll back any changes made throughout the journey.

[Back to contents](#contents)

## **Testing**

- Testing can be found [here](TESTING.md)

## **Deployment**

The project was developed using [GitPod](https://gitpod.io/) and pushed to [GitHub](https://github.com/) the deployed on Heroku using these instructions:

1. Create a requirements.txt file using command *pip3 freeze --local > requirements.txt*
2. Create a Procfile with the terminal command *echo web: python app.py > Procfile* and at this point checking the Procfile to make sure there is no stray line as this can cause issues when deploying to Heroku.
3. The new requirements file and Procfile committed to GitHub.
4. New app created in Heroku by clicking "New" and "Create New App" and giving it an original name and setting the region to closest to location.
5. From Heroku dashboard click "Deploy" -> "Deployment Method" and select "GitHub"
6. Search for GitHub repo and connect.
7. In the dashboard click "Settings" -> "Reveal Config Vars"
8. Set config vars:

Table:

| Key | Value |
| ----------|--------- |
| PORT | 5000 |
| IP | 0.0.0.0 |
| DEBUG | False |
| MONGO_URI | USER_MONGODB_URI |
| MONGO_DBNAME | USER_MONGODB_NAME |
| Secret_Key | USER_SECRET_KEY |


### How to contribute to the site

1. Navigate to [GitHub](https://github.com/) and log in
2. Locate my [repo](https://github.com/suzybee1987/the-book-nook-project)
3. On the right side of the screen click Fork
4. This creates a copy in your own repository to make changes in [GitPod](https://gitpod.io/)
5. Once finished with changes add, commit and push to your own [GitHub](https://github.com/)
6. Click Pull Requests and select "New Pull Request" button.


### How to run the project locally

To clone this project from GitHub follow the instructions taken from [GitHub Docs](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository) explained here:
1. Navigate to the [GitHub Repository](https://github.com/suzybee1987/milestone-2the-book-nook-project)
3. To clone using HTTPS click the clipboard symbol under "Clone with HTTPS". To clone using SSH key click Use SSH then click the clipboard symbol. To clone using GitHub CLI select Use GitHub CLI and click the clipboard symbol. 
4. Open Git Bash
5. Change the working directory to the location you want the cloned directory to be.
6. Type 'git clone' and paste the url copied from step 3. 
7. Press 'enter' to create your clone.

[Back to contents](#contents)


## **Credits**


### **Code**

- CodeInstitute Full Stack Developer Course
- [SitePoint](https://www.sitepoint.com/simple-javascript-quiz/#whatsnext) for help with the quiz layout including pagination
- Wes Bos [JavaScript 30](https://javascript30.com/) for extra ideas on using JavaScript

- Stack Overflow for some bug fixing:
  - [Helpers](https://stackoverflow.com/questions/52113587/materializes-responsive-utilites-not-working) to explain how Materialize show/hide functions work
  - [JavaScript Function Guidance](https://stackoverflow.com/questions/36581504/materialize-carousel-slider-autoplay) to help with the carousel on welcome page
  - [Datetime Tutorial](https://stackabuse.com/how-to-format-dates-in-python/) to help to add time the reviews and thoughts were submitted.


### **Content**



### **Layout**

-Code Institute lessons
-[Background layout](https://css-tricks.com/perfect-full-page-background-image/) from css-tricks.com



### **Images**




### **Inspiration**
 


### **Acknowledgements**

- My Mentor for confidence boosting and helpful advice and feedback.
- Friends and family for testing the site and giving feedback on different devices.
- @Tobi and @Scott_Boning_lead on Slack who supported me through the journey.
- My husband for all his support, patience and great ideas.

[Back to contents](#contents)