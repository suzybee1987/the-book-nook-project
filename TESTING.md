![The Book Nook](static/images/testing/the-book-nook.PNG)


Contents

- [**Testing**](#testing)

- [**Bugs**](#bugs)

## **Testing**

### Navigation is extended from *base.html* so the navigation links on all pages are the same with some differences for admin users.

**Navigation all pages - Logged In Users**

| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | :----: |
| Home button    | To redirect to home page| Click the home button | Button navigates to home | Pass |
| Social Media Links | Redirect to Facebook in new tab | Click Facebook icon | Facebook page opened in new tab | Pass |
|  | Redirect to Instagram in new tab | Click Instagram icon | Instagram page opened in new tab | Pass |
| | Redirect to GitHub in new tab | Click GitHub icon | My GitHub profile page opened in new tab | Pass |
| Nav links | Clicking All Reviews takes user to All Reviews page | Click All Reviews | Redirected to All Reviews page | Pass |
|   | Clicking Profile takes user to their profile page | Click Profile | Redirected to Profile Page | Pass |
|   | Click Add Review takes user to Add Review form | Click Add Review | Redirected to Add Review page | Pass |
|  | Click Log Out logs out the user | Click Log Out | User logged out and redirected to Log In Page | Pass |


**Navigation all pages - User not logged in**

| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | :-----:|
| Nav links | Clicking All Reviews takes user to All Reviews page | Click All Reviews | Redirected to All Reviews page | Pass |
| | Click Log In redirects to log in page | Click Log In | User redirected to Log In Page | Pass |
|  | Click Register redirects to log in page | Click Register | User redirected to Register Page | Pass |


**Welcome Page**
| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- |:----:|
| Card 'Come On In' button | Clicking "Come On In" button takes users to All Reviews | Click "Come On In" button | User redirected to All Reviews | Pass |
| Quotes Carousel  | Play automatically | View carousel to make sure it moves automatically | carousel moves automatically | Pass |
|  | Stop when hovered over  | hover mouse over to see if it stops  | carousel stops on mouse hover | Pass |


**Log In Page**
| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-----------------| ----------|  ---------- | :----: |
| Log in functionality | Correct user/pass combination directs user to their profile page | Log in with correct user/pass combination | Redirected to user profile page | Pass |
|   | Incorrect user/pass combination | Error showing "incorrect username/password" | Flash message displaying [error](static/images/testing/user-pass-error.png) | Pass |
|Link to Register | Redirect to Register page | Click link to register | Redirected to Register page | Pass |



**Register Page**
| Feature        | Expected           | Testing  | Result |
| ------------- |-------------| -----|  ---------- |
| Register functionality | Form validation for email requires `@` symbol |  Attempt to register without `@` in input field | Form validation requests valid email [address](static/images/testing/email-test.png) | Pass |
| | Username and Password must be between 8 and 20 characters | Attempt to enter username and password with less than 8 characters | Feedback error [displayed](static/images/testing/user-pass-validation.png) | Pass |
| | Username and Password must be between 8 and 20 characters | Attempt to enter username and password with more than 20 characters | Form won't let the user use more than 20 characters | Pass |
| | Register with new user and password to be logged in and redirected to Profile page | Enter email address, name, username, password and click register | New account registered and profile page shown | Pass |

**All Reviews Page - user not logged in**

| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | :----:|
| Search Function | Search by book name | Type book name "Mort" into search field and click search | Search returns book name "Mort" by Terry Pratchett | Pass |
|  | Search by author | Type "Terry Pratchett" into search field and click search | Search returns "Mort" and "Guards! Guards" results | Pass |
| | Search by genre | Type "fantasy" into search field and click search  | Search returns all books with genre "Fantasy" | Pass |
|  | Search by username | Type username "cdesquire" into search field | Search displays book/books written by the username "cdesquire" | Pass |
| | Reset button should reset the search form | Enter text to search form then click Reset | Form resets to show all reviews | Pass |
| Reviews | Clicking the image of the book takes user to the book review for that specific book | Click image of "Mort" | Redirected to the book review page for "Mort" | Pass |  
|  | Clicking the See Full Review link under book title on book card takes user to the book review for that specific book | Click See Full Review on "Mort" card | Redirected to the book review page for "Mort" | Pass |  
| Back to Top | When the user scrolls down the page a button appears to click to go back to top of the page | Scroll down the page to see if Back to Top appears | Back to Top Button [displayed](static/images/testing/back-to-top.png) | Pass | 


**All Reviews Page - user logged in**

| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | :----:|
| Favourites | User clicks Favourite button and book is added to favourites, user is redirected to Profile to display this and flash message displayed to confirm | Click Favourite button underneath "Mort" | Redirected to Profile and book is displayed in Favourites table and flash message [displayed](static/images/testing/favourite.png) | Pass |


**Book Review Page**
| Feature        | Expected           | Testing  | Result |
| ------------- |-------------| -----|  ---------- |


**Add Review Page**
| Feature        | Expected           | Testing  | Result |
| ------------- |-------------| -----|  ---------- |


**Edit Review Page**
| Feature        | Expected           | Testing  | Result |
| ------------- |-------------| -----|  ---------- |

**Book Review Page**
| Feature        | Expected           | Testing  | Result |
| ------------- |-------------| -----|  ---------- |





## **Bugs**

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
  
- **Bugs not solved**
  - When a user selects to add a book to favourites this can be added multiple times evidenced [here](static/images/testing/favourites-bug.PNG). This is a bug I thought could be solved by converting to a Python set but unsuccessfully.
  - Search bar on mobile issue, user must click under the input form for this to work. Issue with MaterializeCSS that couldn't be rectified. See [here](static/images/testing/search-input-bug.png)