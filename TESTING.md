![The Book Nook](static/images/testing/the-book-nook.PNG)


Contents

- [**Testing**](#testing)

- [**Bugs**](#bugs)

## **Testing**




## **Bugs**

- The project was produced on git branches to allow new features to be tested and merged to the main branch if successful. Any bugs caught afterwards are noted on the commit message as follows: `Fix: "commit message"`.

- **Bugs found and fixed** 
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
  
- **Bugs not solved**
  - When a user selects to add a book to favourites this can be added multiple times evidenced [here](static/images/testing/favourites-bug.PNG). This is a bug I thought could be solved by converting to a Python set but unsuccessfully.
