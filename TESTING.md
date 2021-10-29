![The Book Nook](static/images/testing/the-book-nook.PNG)


## **Contents**

- [**Testing**](#testing)
  - [**Navigation**](#navigation)
  - [**Buttons**](#buttons)
  - [**Welcome Page**](#welcome-page)
  - [**Register Page**](#register-page)
  - [**Log In Page**](#log-in-page)
  - [**Profile Page**](#profile-page)
  - [**All Reviews Page**](#all-reviews-page)
  - [**Book Review Page**](#book-review-page)
  - [**Add Review Page**](#add-review-page)
  - [**Edit/Delete Review Page**](#editdelete-review-page)
  -[**Admin Pages**](#admin-pages)
    - [**Manage Users**](#manage-users)
    - [**Manage Genres**](#manage-genres)
  - [**Lighthouse Report**](#lighthouse)
  - [**Validators**](#validators)
    - [**HTML Validator**](#html-validator)
    - [**CSS Jigsaw**](#css-jigsaw)
    - [**JSHint**](#jshint)
    - [**PEP8**](#pep8])
- [**Bugs**](#bugs)

# **Testing**

### Navigation is extended from *base.html* so the navigation links on all pages are the same with some differences for admin users.

### **Navigation** 
    - all pages - Logged In Users

| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | :----: |
| Home button    | To redirect to home page| Click the home button | Button navigates to home | Pass |
| Social Media Links | Redirect to Facebook in new tab | Click Facebook icon | Facebook page opened in new tab | Pass |
|  | Redirect to Instagram in new tab | Click Instagram icon | Instagram page opened in new tab | Pass |
| | Redirect to GitHub in new tab | Click GitHub icon | My GitHub profile page opened in new tab | Pass |
| Nav links | Clicking All Reviews takes user to All Reviews page | Click All Reviews | Redirected to All Reviews page | Pass |
|   | Clicking Profile takes user to their profile page | Click Profile | Redirected to Profile Page | Pass |
|   | Click Add Review takes user to Add Review form | Click Add Review | Redirected to Add Review page | Pass |
|  | Click Log Out logs out the user | Click Log Out | User logged out and redirected to Log In [Page](static/images/testing/log-out-feedback.png) | Pass |


### **Navigation**
    - all pages - User not logged in

| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | :-----:|
| Nav links | Clicking All Reviews takes user to All Reviews page | Click All Reviews | Redirected to All Reviews page | Pass |
| | Click Log In redirects to log in page | Click Log In | User redirected to Log In Page | Pass |
|  | Click Register redirects to log in page | Click Register | User redirected to Register Page | Pass |


[Back to contents](#contents)

### **Buttons**
  - all pages - on desktop site

| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | :-----:|
| Feedback on hover | buttons change colour or when user hovers the mouse over them and icons rotate on all except Home (which transforms to increase in size) and Come On In Button on Welcome screen  | Hover mouse over each button | Buttons change colour when hovered over and icons rotate on all except Home (which increases in size) and Come On In Button on Welcome screen | Pass |


### **Welcome Page**

| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- |:----:|
| Card 'Come On In' button | Clicking "Come On In" button takes users to All Reviews | Click "Come On In" button | User redirected to All Reviews | Pass |
| Typewriter message - on desktop | On page load typewriter message is displayed gradually in card | Reload page to view typewriter message | Typewritter message successfully displayed | Pass |
| Quotes Carousel - on desktop | Play automatically | View carousel to make sure it moves automatically | carousel moves automatically | Pass |
|  | Stop when hovered over  | hover mouse over to see if it stops  | carousel stops on mouse hover | Pass |


### **Register Page**
| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | :-----:|
| Register functionality | Form validation for email requires `@` symbol |  Attempt to register without `@` in input field | Form validation requests valid email [address](static/images/testing/email-test.png) | Pass |
| | Username and Password must be between 8 and 20 characters | Attempt to enter username and password with less than 8 characters | Feedback error [displayed](static/images/testing/user-pass-validation.png) | Pass |
| | Username and Password must be between 8 and 20 characters | Attempt to enter username and password with more than 20 characters | Form restrcits the user from using more than 20 characters | Pass |
| | Register with new user and password to be logged in and redirected to Profile page | Enter email address, name, username, password and click register | New account registered and profile page shown | Pass |


[Back to contents](#contents)

### **Log In Page**

| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-----------------| ----------|  ---------- | :----: |
| Log in functionality | Correct user/pass combination directs user to their profile page with name displayed | Log in with correct username/password combination | Redirected to user profile [page](static/images/testing/log-in-feedback.png) with name displayed | Pass |
|   | Incorrect username/password combination | Error showing "incorrect username/password" | Flash message displaying [error](static/images/testing/user-pass-error.png) | Pass |
| Link to Register | Redirect to Register page | Click link to register | Redirected to Register page | Pass |


### **Profile Page**

| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | :----:|
| Reviews written | Reviews written can be viewed and navigated to | Navigate to Profile page, scroll to My Reviews section, click book review. | The book review is visible in My Reviews section and can be accessed when clicking the book name | Pass |
|  | If no reviews written there is a prompt to write one | Scroll to My Reviews section, see message prompt to click to create a review | No reviews written so message is displayed and clicking the link leads to the add review page | Pass |
| Favourites | Favourites can be viewed and removed | Scroll down to Favourites section, click icon to remove from favourites | Upon clicking favourites the book review is removed from favourites for that [user](static/images/testing/favourite.png) | Pass |
|  | If no reviews saved as a favourite there is a prompt to add one with link to all reviews | Scroll to Favourites section, see message prompt to click to look at reviews | No favourites added so message is displayed and clicking the link leads to the reviews page | Pass |


[Back to contents](#contents)

### **All Reviews Page**
    - user not logged in

| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | :----:|
| Search Function | Search by book name | Type book name "Mort" into search field and click search | Search returns book name "Mort" by Terry Pratchett | Pass |
|  | Search by author | Type "Terry Pratchett" into search field and click search | Search returns "Mort" and "Guards! Guards" results | Pass |
| | Search by genre | Type "fantasy" into search field and click search  | Search returns all books with genre "Fantasy" | Pass |
|  | Search by username | Type username "cdesquire" into search field | Search displays book/books written by the username "cdesquire" | Pass |
| | Reset button should reset the search form | Enter text to search form then click Reset | Form resets to show all reviews | Pass |
| | Message displayed if no search results found | Type nonsense word into search bar and click search | No Results Found displayed to the [user](static/images/testing/no-search.png) and button to try again | Pass |
| | Try Again button if no search results | Type nonsense word into search bar and click search, when no results found click Please Try Again | User redirected to All Reviews | Pass |
| Reviews | Clicking the image of the book takes user to the book review for that specific book | Click image of "Mort" | Redirected to the book review page for "Mort" | Pass |  
|  | Clicking the See Full Review link under book title on book card takes user to the book review for that specific book | Click See Full Review on "Mort" card | Redirected to the book review page for "Mort" | Pass |  
| Back to Top | When the user scrolls down the page a button appears to click to go back to top of the page | Scroll down the page to see if Back to Top appears | Back to Top Button [displayed](static/images/testing/back-to-top.png) | Pass | 


### **All Reviews Page**
    - user logged in

| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | :----:|
| Favourites | User clicks Favourite button and book is added to favourites, user is redirected to Profile to display this and flash message displayed to confirm | Click Favourite button underneath "Mort" | Redirected to Profile and book is displayed in Favourites table and flash message [displayed](static/images/testing/favourite.png) | Pass |


[Back to contents](#contents)


### **Book Review Page**
    - user logged in
| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | :-----:|
| Favourites | User clicks Favourite button and book is added to favourites, user is redirected to Profile to display this and flash message displayed to confirm | Click Favourite button underneath "Mort" | Redirected to Profile and book is displayed in Favourites table and flash message [displayed](static/images/testing/favourite.png) | Pass |
| Book information | Book name, author, genre, image and description information expected for individual books | Click to view "Mort" | Image, book name, author name, genre and description all displayed correctly for individual book | Pass |
| | | Click to view "Guards! Guards!" | Image, book name, author name, genre and description all displayed correctly for individual book | Pass |
| Review information | Review title, full review, rating, username of reviewer and date of review displayed for each review | Scroll to Review section, view review is specific to the book | Review displayed | Pass |
| Local book shop link | Clicking the link takes the user to the site in new tab | Click link for local bookshop | New tab opens with local bookshop search page displayed | Pass |
| Amazon link | Clicking the link takes the user to amazon.co.uk in new tab | Click Amazon icon | New tab opens and user taken to amazon.co.uk | Pass |
| Thoughts section | User can add a comment/their thoughts about the book by filling in the form | Add thoughts to the form and click submit | Thoughts [added](static/images/testing/thoughts-test.png) to the page and flash message [confirms](static/images/testing/thoughts-flash.png) | Pass |  
| | Thoughts displayed in thoughts section | All thoughts displayed in thoughts section | Scroll to thoughts section | All thoughts [displayed](static/images/testing/thoughts.png) | Pass | 


### **Book Review Page**

    - the user is the reviewer or admin logged in
| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | :-----:|
| Edit and Delete  | If the user wrote the review they should have edit and delete buttons displayed | Write test review, Look for Edit and Delete Buttons under review | Edit and Delete buttons [displayed](static/images/testing/edit-delete.png) | Pass |
| | Editing the review saves the changes | Click to edit test review, edit the review, click submit | Review edited [successfully](static/images/testing/review-edited.png) with flash message [confirmation](static/images/testing/review-flash-edit.png)| Pass |  


[Back to contents](#contents)

### **Add Review Page**

| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | :-----:|
| Submit new review | New review is saved to all reviews page | Click add review, fill in new review form, click submit | New review added to reviews [page](static/images/testing/test-review.png) and flash message feedback [given](static/images/testing/review-added.png) | Pass | 
| Back up image | If no book image URL provided a back up image displayed | Make new review without including image URL: fill out form, click submit but leave image input blank | Back up image is displayed to the [user](static/images/testing/test-review.png) | Pass | 



### **Edit/Delete Review Page**

| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | :-----: |
| Edit functionality | Only admin or reviewer can edit reviews | Log in as admin, navigate to a book review page, click edit, edit review, click submit, view book review to check edit successful | Edit successful for admin user | Pass |
| | Only admin or reviewer can edit reviews | Log in as standard user, create review, edit review, click submit, view book review to check edit successful | Edit successful for reviewer | Pass | 
| | | Log in as different standard user, attempt to edit review | Edit/Delete button not available | Pass |
| Review info prepopulated on edit | Book review title, author, genre, etc should be prepopulated on editing a review | Log in as admin, click edit review, check book info is the same as book review | Book information in form is present in form | Pass | 
| Delete functionality | Only reviewer and admin can delete reviews | Log in as admin, navigate to a book review page, click delete, modal launch to confirm, click confirm | Delete successful for admin | Pass |
| | | Log in as standard user, create review, click delete | Delete successful for reviewer | Pass | 
| | | Log in as different standard user, attempt to edit review | Edit button not available | Pass |
| | | Log in as different standard user, attempt to delete review | Delete button not available | Pass |


[Back to contents](#contents)

## **Admin Pages**

As well as the ability to edit and delete reviews the admin has access to manage genres and users. This includes creating new genres and deleting generes and users. User is required to log in as admin before attempting these tests.

### **Manage Users**

| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | :-----:|
| Delete User | The functionality to delete a user | Navigate to Manage Users, click delete button under user to delete, redirected to delete user page, click delete, and confirm on modal | User deleted successfully with flash [confirmation](static/images/testing/user-deleted.png) | Pass |


### **Manage Genres**

| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | :-----: |
| Add Genre | Be able to add new genre | Navigate to Manage Genres, click Add New Genre, type genre name in form, submit | Genre created successfully and flash message confirms to the [user](static/images/testing/new-genre.png) | Pass | 
| Delete Genre | The functionality to delete a genre | Navigate to Manage Genres, click delete button under genre to delete, redirected to delete genre page, click delete, and confirm on modal | Genre deleted successfully with flash [confirmation](static/images/testing/genre-deleted.png) | Pass |

[Back to contents](#contents)


## **Lighthouse Testing**
Google Chrome Lighthouse report was generated and no major issues were found. Mainly the issues were due to the use of MaterializeCSS and JQuery as some of the classes are unused in this site. See [report](static/images/testing/log-in-feedback.png)

## **Validators**

### **HTML Validator**
HTML was validated on https://validator.w3.org/ with no major issues. 
- [Welcome Page](static/images/testing/validators/html-welcome.jpg)
- [Register Page](static/images/testing/validators/html-register.jpg)
- [Profile Page](static/images/testing/validators/html-profile.jpg)
- [Log In Page](static/images/testing/validators/html-login.jpg)
- [Edit Review](static/images/testing/validators/html-edit-review.jpg)
- [Book Review](static/images/testing/validators/html-book-review.jpg)
- [All Reviews](static/images/testing/validators/html-all-reviews.jpg)
  - One issue on this page due to the use of ID twice however this is only displayed once on the page as one ID is used for small screens and in the other instance on medium screens and up. 
- [Add Review](static/images/testing/validators/html-add-review.jpg)
- [Manage Genres](static/images/testing/validators/html-genres.png)
- [Manage Users](static/images/testing/validators/html-users.png)

### **CSS Jigsaw** 
CSS3 Validated using https://jigsaw.w3.org/css-validator/ with no issues.
- [All CSS](static/images/testing/validators/css-validator.png)

### **JSHint**
JavaScript was validated using https://jshint.com/ with no issues.
- [All JavaScript](static/images/testing/validators/jshint.png)

### **PEP8**
Python was checked to PEP8 compliance and passed on http://pep8online.com/
- [PEP8](static/images/testing/validators/pep8.png)


[Back to contents](#contents)

# **Bugs**

- The project was produced on git branches to allow new features to be tested and merged to the main branch if successful. Any bugs caught afterwards are noted on the commit message as follows: `Fix: "commit message"`.

- **Bugs found and fixed** 
  - [Manifest Bug](static/images/testing/manifest-bug.png) 
    - Fixed by adding `crossorigin="use-credentials"` to the manifest link in the head of *base.html*
  - [Commit e61643a](https://github.com/suzybee1987/the-book-nook-project/commit/e61643a76dbcec7bd4174f30c534d2066c83fcd4), [Commit cbe04ec](https://github.com/suzybee1987/the-book-nook-project/commit/cbe04ec84624ee2cd34c191cf3a44a2039a8c7dc) and [Commit 7292f14](https://github.com/suzybee1987/the-book-nook-project/commit/7292f1492b26796a9f0a42aa09f6aba0ce98f6a7)
    - Bug as a result of incorrectly trying to retrieve the users first name to display on the welcome page. This caused no name to be shown at all and was fixed by adding 

      `fname = mongo.db.users.find_one(
            {"username": username})["fname"]`
    
      to the profile function on app.py.
  - [Commit a7fda44](https://github.com/suzybee1987/the-book-nook-project/commit/a7fda4408f12f8d08b8d21a0a0ef04fd1c9363cf)
    - Bug fixed in review title where the pattern set `pattern="^[a-zA-Z0-9]{5,50}$"` resuted in the user having to use alphanumeric characters but this wouldn't be expected for a short title. Pattern removed to allow any characters to be used.
  - [Commit ea547d1](https://github.com/suzybee1987/the-book-nook-project/commit/ea547d1acd256ce598a6b447f737aad239714387), [Commit 90afebb](https://github.com/suzybee1987/the-book-nook-project/commit/90afebb715d9dff293e3e38874300d974001e1f6), [Commit 7122d2b](https://github.com/suzybee1987/the-book-nook-project/commit/7122d2b4d178e21529ef139415335667d9c7fb74), [Commit 9d08e0](https://github.com/suzybee1987/the-book-nook-project/commit/9d08e05e8e1c2f70a6ea7d1aa6c62855fa42acf3), [Commit be870e4](https://github.com/suzybee1987/the-book-nook-project/commit/be870e441782bf512f682270ac1db07313a3e5f2)
    - All these commits related to the favourites functionality. The favourites functionality caused an error when new users accessed the profile page as they had no favourites to show. I attempted a Jinja for loop however this was unsuccessful as every time the profile page was landed on there was a subsequent error. I reached out for help from my fellow Slack student Emanuel Silva who helped me set up the favourites functionality with only insignificant bugs which are still unsolved (see unsolved below). (https://github.com/manni8436/MS3-Project)
  - [Commit f139082](https://github.com/suzybee1987/the-book-nook-project/commit/f1390820874ca2a3bf281de0e7a1161f90e768bc)
    - Form wasn't inside the card, fixed by removing an end div tag.
  - [Commit 261a013](https://github.com/suzybee1987/the-book-nook-project/commit/261a01e624b32a1da34269ca2c4d1af1da290452)
    - Bug when editing a review caused because review_date was not added to the edit_review() function in the app.py file. This was fixed by manually updating the app.py with `"review_date": datetime.datetime.utcnow()` and the edited reviews updated to have a valid review_date field. This is because the review_date field was added later and the implications not considered on the edit_review() function.
  - [Commit 14434dd](https://github.com/suzybee1987/the-book-nook-project/commit/14434dd2e9c152c92a0ddc1a176c53ea88462b0a)
    - Bug when logging in with incorrect username or password did not display the flash message due to an indentation error. Fixed by rectifying the indentation error.


[Back to contents](#contents)
  
- **Bugs not solved**
  - When a user selects to add a book to favourites this can be added multiple times evidenced [here](static/images/testing/favourites-bug.PNG). This is a bug I thought could be solved by converting to a Python set but unsuccessfully.
  - Search bar on mobile issue, user must click under the input form for this to work. Issue with MaterializeCSS that couldn't be rectified. See [here](static/images/testing/search-input-bug.png)


  [Back to contents](#contents)