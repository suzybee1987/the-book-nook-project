# The Book Nook

![](static/images/readme/amiresponsive.PNG)

![GitHub contributors](https://img.shields.io/github/contributors/suzybee1987/the-book-nook-project)
![GitHub last commit](https://img.shields.io/github/last-commit/suzybee1987/the-book-nook-project)
![GitHub language count](https://img.shields.io/github/languages/count/suzybee1987/the-book-nook-project)
![GitHub top language](https://img.shields.io/github/languages/top/suzybee1987/the-book-nook-project)

## About

**The Book Nook** is an interactive book review site aimed at book lovers looking to find reviews on books they are interested in reading and allows them to leave reviews for ones they have read. The site is designed to be responsive and easy to navigate on a range of devices to make it accessible for book lovers. 

Link to [live site][(https://the-book-nook1.onrender.com/welcome)]

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
  - [**Site Navigation**](#site-navigation)
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
- All users
    - I would like to find books to read based on their reviews
    - I want the site to be easy to navigate on mobile primarily so I can use it on the go.
    - I want the site to be responsive on all devices.
    - I would like to see a timestamp from when the review was posted so I can determine how recent it is and if it follows on from a movie release or sequel/prequel
    - I would like there to be a link to a site where I can buy the book after reading the review 
    - I would like to be able to save book reviews to favourites to read later
    - I would like to see the book cover images to get an idea of the book and genre
    - I would like to see images of books and fonts in-keeping with the theme
    - I would like there to be navigation buttons to prevent having to use the back browser button and lots of scrolling on long lists
    - I would like a profile page showing the reviews I have written and favourited
    - I would like to be able to search by author, genre and book name for books I may have read or be interested in and be able to comment on those I have read
    - I would like to be able to add a new review for a new book and be able to edit and delete if required.

- As a first time user
    - I would like to be able to register with no problems and minimal information required
    - I would like it to be obvious that I am on a book review site 
    - I would like to be able to view book reviews

- As a returning user
  - I would like to be able to see reviews I have previously written and favourited
  - I would like to be able to log in to see book reviews I have written and favourited on one page


### **Site Owner Goals** 
- Earn money on each book purchased via an affiliate link from the site. Note no affiliate link was created for this site but a link to Amazon has been provided.
- I want the site to be responsive on all devices for the best user experience to encourage customers to return. 


[Back to contents](#contents)


## **Design Choices**


### **Fonts**

- The fonts have been chosen to complement one another and also give the aesthetic of a book store with a mixture of serif for the book names, sans serif for descriptions and cursive for quotes and comments.
  -  [Libre Baskerville](static/images/readme/libre-baskerville.PNG) was used for the headings on each of the pages to create consistency.
  - [Special Elite](static/images/readme/special-elite.PNG) was used the the book titles and author names as it mimics the traditional typewriter font and puts the user in mind of vintage books.
  - [Merienda](static/images/readme/merienda.PNG) is a cursive font with a look of real handwriting which was used for the comments and reviews to give the impression they were handwritten.
  - [Lato](static/images/readme/lato.png) was used for any descriptions or text which is instructional so as not to distract from the rest of the page.


### **Colours**

- ![](static/images/readme/ms3-coolors.png) This Coolors palette was used to put together a colour scheme in keeping with the colour of the wood on book shelves to make the user feel like they are closer to a book store than online site. The lighter 'Desert Sand' colour was used for the cards and opacity added so the background underneath can still be seen without having to use a harsher white colour. 


### **Imagery**

The images used were taken from [Pexels](https://www.pexels.com/) which offers royalty free use of images as long as not for business use. They were all used to complement the colour scheme of the header and footer.
- The [Register and Log in pages](static/images/pexels-skitterphoto.jpg) have a background image of a nice big library space to make the site inviting.
- The [Welcome page and Profile page](static/images/pexels-skitterphoto-book.jpg) show a nice background image of a book opened wide with the pages spread out to encourage the user to come in to the book site. 
- The [Hero Image](static/images/pexels-books-long.jpg) for the reviews page was used to bring a splash of colour and innovation. 
- The [Add Review](static/images/pexels-negative-space.jpg) image was used to encourage the user with some examples of vintage book titles.
- The [Users and Genres](static/images/pexels-janko.jpg) image was used to continue the theme of the book shop but was kept different to the other pages to remind the user these are admin pages. 
- The [back up image](static/images/pexels-lilartsy.jpg) was provided in the instance that the reviewer does not add an image or the image link provided is broken. 


### **Wireframes**

The wireframes were created using [Adobe XD](https://www.adobe.com/uk/products/xd.html) and can be found in pdf form in [wireframes](wireframes).


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
- [Render](https://render.com/)
    - A Cloud Application Platform used to deploy the site
- [JSHint](https://jshint.com/)
    - Used to detect errors in the JavaScript files
- [PEP8 Online](http://pep8online.com/)
    - Used to check PEP8 compliance in the code
- [W3C Markup Validator](https://validator.w3.org/)
    - Markup validation service for HTML5
- [Jigsaw Validator](https://jigsaw.w3.org/css-validator/)
    - CSS3 Validation Service
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

### **Site Navigation**

The site journey taken by users is shown below.

For users logged out:
![](static/images/readme/site-logged-out.png)

For users logged in:
![](static/images/readme/site-logged-in.png)

For admin users:
![](static/images/readme/site-admin.png)



### **Features Implemented**

All aspects of CRUD functionality are included in this site for users who are logged in. 
For example: 

| Function | Location     |
| -------- | ------------ |
| Create   | Add Reviews  |
|          | Add Thoughts |
| Read     | All Reviews  |
|          | Book Review  |
|          | Profile      |
| Update   | Edit Reviews | 
| Delete   | Book Review  |


The admin user has extra functionality included:

| Function    | Location                   |
| ----------- | -------------------------- |
| Create      | Manage Genres -> Add Genre |
| Read        | Manage Genres              |
|             | Manage Users               |
| Update      | Edit Genres                | 
| Delete      | Delete Genre               |
|             | Delete User                |

[Back to contents](#contents)


#### **Features relevant to all pages** (extended via *base.html*):

- **Header**
  - **Navigation**
    - Contains the navigation links and is fixed to the top of the page for easy use on all devices.
    - Mobile Side View navigation for easier use.
    - The home button is on the left side of the header and sections of the page listed on the right where a user would expect them to be.
    - Navigation links are highlighted or animated when the user hovers over them to give feedback that they have hovered over the right spot.
    - The colour scheme is designed to be easy to read with the contrast and the ratio tested on Google Dev Tools.
    - Jinja if statements used to ensure only certain navbar menus are visible to certain users. Only admin is able to see `Manage Genres`, `Manage Users` links and only users who are logged in are able to see `Add Review`, `Profile` and `Log Out`. Users not logged in will see `Register`, `Log In` and all users will see `All Reviews`. This is to ensure the best user experience and avoid confusion or breaches of security. 

  
- **Hero sections**
    - The images take up the full width of the browser to leave a high impact lasting impression with the user and this is replicated on all pages to bring a sense of familiarity when browsing.
    - The content is displayed on cards with a slight opacity to make the background image visible underneath but not to the extent where it distracts.

  
- **Footer** 
    - Contains links to social media
    - Copyright symbol with datetime feature to update the date every year


#### **Welcome Page** (*welcome.html*) 
    - Card displaying an introduction to the site including name, brief     description and typewriter feature on medium and above screen sizes prompting the user to log in. Button to click to enter the site, leading to *reviews.html*. User is not required to log in to view reviews. 
    - Carousel of quotes from authors about books for users to view and enjoy on medium screens and above.


#### **Log In Page** (*login.html*)
  **Form** 
    - Card requesting the user sign in with their username and password with prompt to create an account if they haven't already registered and linking them to `register.html` 


#### **Register** (*register.html*)
   **Form**
   - Card requesting the user register with their email address, name, username and password with prompt to log in to an account if they have already registered and linking them to `login.html`.

[Back to contents](#contents)

#### **Profile Page** (*profile.html*) [see here](static/images/readme/profile-page.png)

- **Welcome**
    - Feedback to user that they have been logged in through flash message at the top of the page to feedback that log in was successful and also card heading `Welcome <users first name>` for the personal touch.
- **My Reviews** 
    - Reviews written by the user are in this section, including book name, author, review title and the rating left. By clicking on the book name the user is redirected to the book review page where they can view, edit or delete it. 
- **My Favourites**
    - Reviews where the user has clicked to add to favourites are located here, including book name, author and a link to remove the review from favourites. The user can click the book name link to be taken to the review if they wish.
    

#### **All Reviews** (*reviews.html*) [see here](static/images/readme/all-reviews.png)

 - **Search Bar**
    - The search bar allows the user to search by book name, author, genre and reviewed by so they can find more books based on their interests. Search and reset buttons present for easy use. 
    
- **Book Reviews**
    - List present of all books reviewed so far by other users including book front cover image, book name, author, title of review, rating, link to full review and button to save to favourites. This button allows the user to save for their own use later. By clicking on the image of the front cover or `See Full Review` link the user is directed to the full review page where they can add their thoughts. If no image available for the book review a default alternative will be posted. This is completed using Jinja for loop of reviews and extracting information from MongoDB.

#### **Book Review Page** (*book_review.html*) [see here](static/images/readme/book-review.png)

  - **Book Review**
    - Image of book cover, book name, author and brief description of the book is displayed on page loading. This is completed using Jinja for loop of reviews and extracting information from MongoDB. Favourite button also present here to allow user to save to their profile.
    - Original review posted beneath the description of the book to allow the user to see what the original reviewer thought. Username, date stamp and rating also included here so that the user can search for other reviews by this user.

  - **Link to book store** 
    - Link to direct the user to buy the book from an independent bookshop via this [website](https://www.booksellers.org.uk/bookshopsearch) for ease. It prompts the user to find their nearest book shop.

  - **Thoughts section**
    - Prompts the user to add their thoughts on the book and displays what previous users have commented, again with username of commenter and date and time stamp.

 - **Button**
    - The button redirects the user back to *reviews.html* to prevent them having to press the browser back button for better user experience. 


#### **Add Review** *(add_review.html)*

 - **Form** 
  - Allows user to enter details of the book including: genre, book name, author, review title, full review, description of the book, link to cover image for the book and rating.

 - **Buttons**
    - The `Back to Reviews` button redirects the user back to *reviews.html* to prevent them having to press the browser back button for better user experience. This is also achieved by clicking `Cancel` underneath the form. The `Submit Review` button submits the add review form.

[Back to contents](#contents)

#### **Edit Review** *(edit_review.html)*

 - **Form** 
  - Allows user to enter details of the book including: genre, book name, author, review title, full review, description of the book, link to cover image for the book and rating. This is prepopulated with the details existing already on the review document.

 - **Buttons**
    - The `Back to Reviews` button redirects the user back to *reviews.html* to prevent them having to press the browser back button for better user experience. This is also achieved by clicking `Cancel` underneath the form. The `Submit Review` button submits the add review form.


#### **Manage Users** (*users.html*) - Only seen by admin user
  - Card displaying all of the users who have registered so far with options to edit them or delete them.
  - **Edit users** button leads to (*edit_user.html*) and a form where a switch can be flipped to make a user an admin. The user's username is generated to provide confirmation of user to be made admin.
  - **Delete users** button leads to (*delete_user.html*) and a form where the user can be deleted, whereupon a modal is launched to confirm you would like to delete; confirming the username and name of user to be deleted. 

#### **Manage Genres** (*genres.html*) - Only seen by admin user
  - Card displaying all of the genres created so far with options to edit them or delete them.
  - **Edit Genres** button leads to (*edit_genre.html*) and a form where a genre's name can be changed. The genre name is generated to provide confirmation of genre to be made changed.
  - **Delete Genres** button leads to (*delete_genre.html*) and a form where the genre can be deleted, whereupon a modal is launched to confirm you would like to delete; confirming the name of genre to be deleted. 

[Back to contents](#contents)

### **Error Pages**

#### *404.html*

 - **Button**
    - On the (*404.html*) page the button redirects the user back to Home Page to prevent them having to press the browser back button for better user experience. 

#### *500.html*

 - **Button**
    - On the (*500.html*) page the button redirects the user back to Home Page to prevent them having to press the browser back button for better user experience. 

### **Future Features**

- In future I would like to implement a few extra features for example:
  - the ability to click a username to find what other reviews they have written. At present this can be searched in the (*reviews.html*) search bar. 
  - to add a privacy policy and terms and conditions page
  - to allow users to edit their thoughts (comments) on the reviews.
  - allow the users with admin rights to give other users admin rights.


### **Responsive Design**

- Materialize CSS columns were used to make the site responsive on all devices and viewport height adjusted for the best user experience

[Back to contents](#contents)


## **Database Layout**

Collection: book-nook
| Title      | Field    | Data Type |
| ---------- | -------- | --------- |
| Favourites | _id      | ObjectId  |
|            | book_id  | ObjectId  |
|            | username | String    |


| Title      | Field    | Data Type |
| ---------- | -------- | --------- |
| Genre      | _id      | ObjectId  | 
|            | genre_id | ObjectId  |


| Title      | Field        | Data Type |
| ---------- | -----------  | --------- |
| Quotes     | _id          | ObjectId  |
|            | quote_author | String    |
|            | quote_text   | String    |
|            | href         | String    |


| Title      | Field     | Data Type |
| ---------- | --------- | --------- |
| Rating      | _id      | ObjectId  |
|            | rating_no | Int32     |

| Title      | Field        | Data Type | 
| ---------- | -----------  |  -------- | 
| Reviews    | _id          | ObjectId  |  
|            | book_name    | String    | 
|            | author_name  | String    |  
|            | review_title | String    |  
|            | review       | String    | 
|            | description  | String    | 
|            | rating_no    | Int32     |  
|            | image        | String    | 
|            | reviewed_by  | String    |    
|            | review_date  | Date      | 
|            | thoughts     | Array     |  

| Title      | Field        | Data Type |
| ---------- | -----------  | --------- |
| users      | _id          | ObjectId  | 
|            | fname        | String    |
|            | lname        | String    | 
|            | email        | String    | 
|            | username     | String    | 
|            | password     | String    | 

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

- Testing and Bugs can be found [here](TESTING.md)


## **Deployment**

The project was developed using [GitPod](https://gitpod.io/) and pushed to [GitHub](https://github.com/) then deployed on Heroku using these instructions:

1. Create a requirements.txt file using command *pip3 freeze --local > requirements.txt*
2. Create a Procfile with the terminal command *echo web: python app.py > Procfile* and at this point checking the Procfile to make sure there is no stray line as this can cause issues when deploying to Heroku.
3. The new requirements file and Procfile committed to GitHub.
4. New app created in Heroku by clicking "New" and "Create New App" and giving it an original name and setting the region to closest to location.
5. From Heroku dashboard click "Deploy" -> "Deployment Method" and select "GitHub"
6. Search for GitHub repo and connect.
7. In the dashboard click "Settings" -> "Reveal Config Vars"
8. Set config vars:

Table:

| Key          | Value |
| ------------ |--------- |
| PORT         | 5000 |
| IP           | 0.0.0.0 |
| MONGO_URI    | USER_MONGODB_URI |
| MONGO_DBNAME | USER_MONGODB_NAME |
| Secret_Key   | USER_SECRET_KEY |

Deployment was moved to Render following the withdrawal of the free plan on Heroku. 


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
- Wes Bos [JavaScript 30](https://javascript30.com/) for extra ideas on using JavaScript

- Stack Overflow for some bug fixing:
  - [Helpers](https://stackoverflow.com/questions/52113587/materializes-responsive-utilites-not-working) to explain how Materialize show/hide functions work
  - [JavaScript Function Guidance](https://stackoverflow.com/questions/36581504/materialize-carousel-slider-autoplay) to help with the carousel on welcome page
- [Datetime Tutorial](https://stackabuse.com/how-to-format-dates-in-python/) to help to add time the reviews and thoughts were submitted.
- [HR CSS](https://codepen.io/Grienauer/pen/PdPPKZ) to separate the book review sections using `<hr>` elements and CSS.
- [Simon Vardy's Reading Room project](https://github.com/simonjvardy/the-reading-room) brought some inspiration for how the site could look and some of the features that could be implemented, eg the comments section.
- [Emanuel Silva MS3 favourites list](https://github.com/manni8436/MS3-Project) Emanuel helped me to set up the favourites list code in app.py.
- Code Institute lessons
  -[Background layout](https://css-tricks.com/perfect-full-page-background-image/) this was taught in one of the Code Institute lessons from css-tricks.com and I use it constantly for my background images. 


### **Content**
Some book review sites were consulted before beginning this project to check what content may be requested by the user. 
Mainly:
- [SFBook](https://sfbook.com/) gave me the idea of a carousel due to it's changing book images on the home page. I decided to use the carousel as a way to display quotes from authors.
- [GoodReads](https://www.goodreads.com/?ref=nav_hom) and [Waterstones](https://www.waterstones.com/) helped me work out potential layout for the review pages to look


### **Images**

- [User and Genre pages](https://www.pexels.com/photo/light-inside-library-590493/) use this photo by Janko Ferlic from Pexels.
- The Login and Register pages sample [this image](https://www.pexels.com/photo/ancient-antique-architectural-design-architecture-442420/) by Skitterphoto on Pexels.
- The Welcome and Profile pages sample [this image](https://www.pexels.com/photo/book-page-1005324/) by Skitterphoto on Pexels.
- The Add Review and Edit Review pages [background](https://www.pexels.com/photo/books-old-book-knowledge-bookstore-34592/) is provided by Negative Space on Pexels.
- All Reviews page [background](https://www.pexels.com/photo/books-1926988/) supplied by Ricardo Esquivel on Pexels
- If no image is posted in the review [this](https://www.pexels.com/photo/photo-of-hands-holding-a-book-3563625/) one is shown instead. Photo by lilartsy from Pexels


### **Acknowledgements**

- My Mentor for confidence boosting and helpful advice and feedback.
- Friends and family for testing the site and giving feedback on different devices, especially my father in law, Alasdair for diligently testing and finding things to be fixed.
- @Eventyret_mentor, Amy O'Shea, Iryna, Claire Lemmonaire on Slack who supported me through the journey.
- My husband for all his support, patience and great ideas.
- And, lastly my cheerleaders Emanuel Silva and Jonathan Swift for helping me to stay motivated, sharing great ideas and bad jokes to keep us going. 

[Back to contents](#contents)
