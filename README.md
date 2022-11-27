<h1 align="center">Miller  Davies</h1>
These days, when the world around us seems to get more and more chaotic each day, people need to feel that their lives have some kind of stability and that they are somehow prepared for harder times. To help create this sense of security, gardening and growing your own food, to at least some extent, is a good start. Therefore the gardening and seed-selling business should be a growing market.
 
Miller & Davies is an imaginary e-commerce site selling organic seeds for garden and indoor growing. It focuses on a wide range of users by offering a large collection of seeds. For now it is focusing on the products available, but in the future the site will increase its contents with gardening information, for beginners and more experienced gardeners and also with more material with inspirational content.

[View the live project here](https://hj-miller-and-davies.herokuapp.com/).  
![Responsiveness image](documentation/images/responsive_image.png)

## Table of Contents
**[User Experience](#user-experience)**  
**[Planning the Project](#planning-the-project)**  
**[Features](#features)** 
**[E-Commerce Business Model and Marketing Strategies](#e-commerce-business-model-and-marketing-strategies)** 
**[Technologies Used](#technologies-used)**   
**[Testing](#testing)**  
**[Deployment](#deployment)**  
**[Credits](#credits)**  
**[Acknowledgements](#acknowledgements)**  
**[Conclusion](#conclusion )**  

## User Experience
### Target Audience
The target audience for the Miller & Davies site is people of all ages that are interested in gardening and planting seeds. People from rural and suburban areas should be in majority even if urban people might be interested in the selection of seeds suitable for growing indoors.  
The site fulfills their needs of buying organic vegetable, flower and herb seeds.

### User Stories
The user stories for this project can be found in [this document](documentation/user_stories.md).

## Planning the Project
The planning of this project is done in Github Projects and follows an Agile strategy.
[Link to the project's Kanban Board](https://github.com/Odden69/Miller_and_Davies/projects/1).  
My observation during this project is that it takes a lot of experience to make good time estimates! Therefore the time aspect, in this project as well as my previous, has not been very highly prioritized when doing the planning of this project. I have instead focused on the tasks and the acceptance criteria as well as on always having a working app after each iteration. Even if the time aspect wasn't perfect I found myself using the Kanban board quite often to scroll through, and check tasks and issues.


### Database Diagram
To illustrate the logic of the database I used [diagrams.net](https://www.diagrams.net/).
![Database diagram](documentation/images/database_diagram.png)

### SEO
When brainstorming for ideas, I came up with a number of words and expressions I thought would be relevant searches for a user looking for a site like this. After searching for them on Google, using “others search for” and “related searches”, and finally Wordtracker, I ended up with these words and phrases to use on the site to improve SEO:
- organic seeds
- gardening seeds
- vegetable seeds
- flower seeds
- herb seeds
- organic vegetable seeds
- organic flower seeds
- organic herb seeds
- organic vegetable seeds online
- seeds online
- seeds for vegetables
- seeds for garden
- seeds for windowsill

These keywords and expressions has been added to the sites keywords and to headers throughout the site, to improve its ranking by search engines.

This project is still in its early stages and needs a lot of more content before it is a fully developed website. The SEO will improve with relevant information about
gardening, tools and inspiration for users on different levels of background knowledge.   

### Wireframes
The wireframes for this project can be found in [this document](documentation/wireframes.md).


## Features
### Existing Features
<details>
  <summary>Click to see the existing features</summary>

#### The Start/Product Page
The first page consists of a relevant hero image of a hand planting a seed and a concise message describing the purpose of the site.  
Scrolling down, the user can find all products from the store, paginated on several pages.
![Start/Product Page](documentation/images/features/startpage_1.png)  
  
![Start/Product Page](documentation/images/features/startpage_2.png)  

#### The Header
The header is consistent through all the site's pages.  
On small screens it is compressed with a collapsed navbar.
![Header on Large Screens](documentation/images/features/header_1.png)
![Header on Small Screens](documentation/images/features/header_2.png)  
* The header has a logo with a link back to the product page.  
* The search bar gives the user the opportunity to search for site content. The scope of the search is a product's name and description. 
* A link to the users basket can be found, in the top of the header for a large screen, and in the navbar for a small. It shows whether the basket is empty or, if it has any content, the total cost of the order.
* The **All Products** dropdown link lets the user choose the order of the presented products, by name, by price or by rating.  
![The All Products Dropdown](documentation/images/features/all_products_dropdown.png) 
* The **Vegetables** link filters the products and shows only the ones belonging to the Vegetable category. The same goes for the Flowers and Herbs links respectively.
* The **Indoor Growing** link filters the products and shows the ones marked suitable for growing indoors.
* The **Bargains** link filters the products with respect to products on sale.
* The @icon-heart link filters the products and shows the ones the user has marked as their favorites.
* The content of the user dropdown menu, @icon-user, is dependent on the login status of the user and will be described in more detail below.

#### The Category/Subcategory Selection

On large screens there is a set of buttons between the hero image and the products. Which buttons are visible depends on where in the product structure the user is navigating.  
On small screens, however, these selections are available in the collapsed navbar.  
To help the user navigate the site a breadcrumb trail is available.  
Every category and subcategory ahs its own il 

In the image below a user has navigated to Flowers and can select between Annuals, Biennials and Perennials to narrow down the products shown even more.  
![Category/Subcategory Selection on Large Screens](documentation/images/features/categories_1.png)  
The category selections on a small screen:  
![Category/Subcategory Selection on Small Screens](documentation/images/features/categories_2.png)

#### Indoor Growing Page
On this page the user finds a selection of the products which are suitable for growing on a windowsill.
![Growing Greens Indoors](documentation/images/features/indoors.png)

#### Bargains Page 
Here the products on sale can be found.  
![Bargains](documentation/images/features/bargains.png)

#### The Favorites Page
A user can mark products as favorites and then find them all gathered on this page. 
![Favorites](documentation/images/features/favorites.png)

#### Product Cards
Each product on the products page is presented on an individual card. Each card shows an image of the product, the product's rating, the name of the product and if the user marked it as a favorite. Also the size of the product's packet and its price is presented as well as a note shown if the product is on sale. On the bottom there is a button to add the product to the shopping basket.  
![Product Card](documentation/images/features/card.png)

#### Product Detail Page
Each product has a detail page which can be reached by clicking anywhere on the product card, except for the buy now button.  
A product detail page consists of a larger image of the product, the product's name together with a description of the product.
The rating is displayed together with the number of ratings. On this page a logged in user can rate the product. There is also a favorite icon which shows if the user added the product to their favorites.   
The products sku, packet's size and and prize is also displayed.
If the product is on sale the original price as well as the on sale price is shown.  
On this page a user can adjust the amount before adding the product to the shopping basket.  

![Product Detail](documentation/images/features/product_detail.png)

#### Shopping Basket
Clicking on the basket link in the header will bring the user to the basket page.  
If the basket is empty the page shows an informative message and offers a link back to the product page.  
![Empty Basket](documentation/images/features/basket_1.png)
  
A basket with a content, on the other hand, shows a list of the picked products where the user can adjust the amounts of each product and also entirely delete it from the shopping basket.  
When the user has reviewed the list there is a Checkout button which brings the user to the checkout page.  
![Basket](documentation/images/features/basket_2.png)

#### Checkout
On the checkout page the user can go back and adjust the basket via a link or they can fill out the delivery and payment form and finally push the Complete Order Button to place the order.  
A logged in user is proposed to save the filled out form to simplify a future order when the information be prefilled on the form. A non logged in user is offered a link to log in or sign up for an account.  
Completing the order brings the user to an order confirmation page.
![Checkout](documentation/images/features/checkout.png)

#### Order Confirmation
On the order confirmation page the user can view the order they just placed to make sure everything is correct. 
The user will also receive a confirmation email. 
![Order Confirmation](documentation/images/features/order_conf.png)

#### Sign Up
A user does not have to create an account to place an order from Miller & Davies, but an account will simplify an order checkout and makes it possible for a user to review previous orders.  
The sign up page is reached from the user dropdown menu.  
![Sign Up Link, Large Screen](documentation/images/features/sign_up_1.png)  
![Sign Up Page](documentation/images/features/sign_up_2.png)  
After filling out and sending the form the user receives a confirmation email and is redirected to a page with a confirmation message.  
![Sign Up Confirmation](documentation/images/features/sign_up_3.png)  
From a link in the email the user ends up on a verify email page.
![Verify Email](documentation/images/features/sign_up_4.png)  

#### Log in
The log in link is also reached from the user dropdown menu.  
![Log In Link, Small Screen](documentation/images/features/login_1.png)  
From the login page a user can recover a lost password by clicking the forgot Password? link. The user then receives an email with a recovery link.    
![Log In Page](documentation/images/features/login_2.png)  
  
As a logged in user you can access a few more features than as an anonymous user.  

#### Rate a product
A logged in user can rate a product from the product detail page. 
![Rate Product](documentation/images/features/rate.png)  

#### Profile Page
A logged in user can also access their profile page from the user dropdown menu.  
![Profile Link](documentation/images/features/profile_1.png)  
On this page the user can update their default delivery information and also view their previous orders.
![Profile Page](documentation/images/features/profile_2.png)  
With a click on the order number link the user is redirected to the past order confirmation page and can view the order and then go back to the profile page.  
![Past Order Confirmation Page](documentation/images/features/profile_3.png) 

#### Log out
A logged in user can log out again via the user dropdown menu.  
![Log Out Link](documentation/images/features/logout_1.png)  
From that link the user is redirected to a confirm logout page.  
![Log Out Page](documentation/images/features/logout_2.png)

#### Newsletters
At the bottom of each page there is a newsletter sign up form where a user, logged in or non logged in, can sign up to receive a weekly newsletter with inspirational content.  
![Newsletter Sign Up](documentation/images/features/newsletter.png)

#### Footer
Each page on the site has a footer with social media links and a contact email address.  
![Footer](documentation/images/features/footer.png)  

#### User Action Confirmation
All actions a user makes on the page is confirmed with a positive or negative message. For example a successful login results in:  
![Confirmation message, success](documentation/images/features/confirmation_1.png)  
An information message appears, for example, when the user tries to rate a product they already rated:
![Confirmation message, info](documentation/images/features/confirmation_3.png)  
An error message appears, for example, if a non authorized user tries to reach a page that requires authorization by entering the URL:  
![Confirmation message, fail](documentation/images/features/confirmation_2.png)  
  
</details>

### Remaining Bugs, Room for improvements and Features Left to Implement
#### Room for Improvements
One main concern is the slow rendering of the pages on this app. My first effort in the right direction was when I realized I didn't filter the products by the pagination page. I was hoping this would make a bigger difference on the rendering than it did, even though it had a rather big impact on the rendering time when running the site locally. When digging just a bit deeper in the problem I saw that, of 8.39s for a page to load, 7.25s were "waiting for server response". I'm not sure what can be done to improve that and leave that issue for more investigations after this project is finished.  
One major thing I should do is to replace all the current .jpg images with .webp to decrease the size of the images.  
  
#### Remaining Bugs
One big bug still left on the site, which I with some more experience probably would have realized earlier and could have done something about, is a URL problem. All URL queries are lost when rerendering.  
There are a lot of situations on this site that would work, or improve, if the URL of the current page was used as input to the next. Here are a couple of them:  
* The pagination only works for non sorted All Products pages. All other filtered or sorted pages returns to an All Products page when the paginate page is changed.
* If a user is on the favorite page and removes one of their favorites, they are redirected back to the product page instead of remaining on the favorite page.   
  
Another bug left to fix is a rating issue. Trying to rate a product with five stars results in a 500 error page even though the rating is successfully saved.  
The investigation to solve that issue would take more time that I have right now, so it will also have to wait.

#### Features Left to Implement
To even begin to resemble an actual e-commerce site Miller & Davies would need a lot more interesting content. Pages with gardening tips and inspirational ideas as well as more relating products like tools and fertilizers for instance. It also lacks links to other sites with relating content.  

When I started the project I added sowing and harvest seasons to the product model 
but I decided quite early in the project to postpone these, since I realized it would grow too big for my time frame.  
It would be nice to implement these to let a user view and select products from this point of view.  
I also planned to implement a Product in Stock feature. That is not hard to implement but is still postponed to after the deadline of this project. 

The admin side of this site also needs a lot more work.
* First out is the ability to compose confirmation letters that are appealing to the eye.
* The newsletter feature is not finished. The user can sign up for a newsletter but there is no way for an admin user to compose the letters or use the send list. 

It would also be nice to implement a contact form for a user to fill in, in case of questions or comments.

## E-Commerce Business Model and Marketing Strategies
This is an E-commerce site in its simplest form, a B2C business model only meant for stand-alone transactions to private customers where no subscribed transactions are offered.

Miller and Davies' marketing strategies are to be seen on social medias and to send newsletter to signed up customers.  
There are Facebook and Instagram links in the footer of the site to pages where the business is promoted by regular posts with inspiration and information.  
The newsletter is sent out regularly to promote news and offers, and to share information and inspiration with the customers.  
(Since this is just a project created for educational purposes, the links on the site are not directed to a specific facebook or instagram page.)  
This image shows what a facebook page created for this site might look like.  
![Miller & Davies facebook page](documentation/images/facebook.jpg)

## Technologies Used
### Programming Languages
**Python**  
**CSS**  
**HTML**  
**JavaScript**  

### Libraries and Frameworks
The whole project is built on the [**Django**](https://www.djangoproject.com/) framework and quite a few different django libraries are used throughout the project.  
  
To check the python code, dynamically, I installed **pylint-django** and **pylint-plugin-utils**.  
  
To aid the styling and responsivness process I used [**Bootstrap 5**](https://getbootstrap.com/).  

### Programs and Sites
The site is deployed on [**Heroku**](https://www.heroku.com/) with a **gunicorn** server and a **psycopg2** adapter, using an external **PostgreSQL** database on [**ElephantSQL**](https://www.elephantsql.com/).  
  
To store the static and media files for deployment I used [**AWS**](https://aws.amazon.com/).  
  
The payment service used is [**Stripe**](https://stripe.com/).  
  
For the Logo font I used [**Google Fonts**](https://fonts.google.com/).  
  
The icons are collected from [**Font Awsome**](https://fontawesome.com/).  
 


## Testing
¨¨All through the development process the site has been undergoing manual testing to confirm the intended functionality.

Up to a certain point in the project (a commit made on April 28th), the code was also tested with automated testing by unit testing. At that point the tests passed, with one exception, and the coverage was 100%. Since then the project grew without me maintaining the testing files, therefore tests now fail and the coverage, especially for views, are really low.
But even if the automated testing was not completed, the work I put into it was not wasted. I learned a lot about testing but also about how some of the code works which I before that had some trouble understanding.¨¨

### Testing User Stories from User Experience (UX) Section
¨¨All user stories in the list [above](#user-stories) has been tested and confirmed after implementation, apart from the ones marked with an asterisk, which will be implemented at a later stage.¨¨

### Validation and Responsivity
¨¨The validations of the code were made on these sites:
- Python : [pep8online](http://pep8online.com/checkresult)
- CSS : [jigsaw W3C](https://jigsaw.w3.org/css-validator/validator)
- HTML : [WS HTML Validator](https://validator.w3.org/)
- JavaScript : [JSHint](https://jshint.com/)

The tests were all without errors with two exceptions described in this [Test Document](documentation/Testing_ITrain.xlsx).  
 
All pages were tested in **Lighthouse** validation. Apart from some performance results on a phone, all results were very close to 100%. These tests are also documented in the [Test Document](documentation/testing_itrain.xlsx).

All the links on the site have been tested, as well as the function of the forms.
These tests include testing of the CRUD functionality and the use of confirmation messages.
These tests are documented in the [Test Document](documentation/testing_itrain.xlsx) as well.¨¨

### Color Contrast Check
¨¨The color contrast was checked on [Contrast Grid](https://contrast-grid.eightshapes.com/?version=1.1.0&background-colors=&foreground-colors=%23FFFFFF%2C%20White%0D%0A%23000%2C%20black%0D%0A%2312110D%0D%0A%23A87556%0D%0A%23C7C7BC%0D%0A%236F310A%0D%0A&es-color-form__tile-size=compact&es-color-form__show-contrast=aaa&es-color-form__show-contrast=aa&es-color-form__show-contrast=aa18&es-color-form__show-contrast=dnp).  ¨¨
![Color Contrast Check](documentation/contrast_check.png)

## Deployment
### Clone a GitHub repository
To make a local copy of this project you can make a clone by following these steps:
- Log in to GitHub and find the [repository](https://github.com/Odden69/ITrain).
- Above the list of files click on the code button. By the https address there is a copy symbol, click on that.
- Open Git Bash
- Change the current working directory to the location where you want the cloned directory.
- Type "git clone", and paste in the copied URL.
- Press Enter to create your local clone.

### Deploy to Heroku
This site was deployed to Heroku Apps. The instructions below have been updated after my initial deployment since I changed the storage of the static files from Cloudinary to WhiteNoise.

To deploy a copy of this site, follow these steps:
- Start by installing everything in the requirements.txt file.
- Make sure you have correct requirements.txt and Procfile before moving on with the deployment.
- Log in to [Heroku apps](https://heroku.com/)
- On the Heroku dashboard go to the "New" menu and choose "Create new app".
- Give the app a name that needs to be unique, select your region and click "Create app".
- Now the new app's dashboard is opened. Click on the resources tab.
- Add the Heroku Postgres Add-on.
- Go to the settings tab and reveal the Config Vars. 
- Add a SECRET_KEY Config Var and give it a string value of your choice. Preferably, use a secret key generator.
- To run the project locally you need to create an env.py file in your top level directory.
  - Copy the DATABASE_URL from Heroku's Config Vars. 
  - Add os.environ["DATABASE_URL"] to the env.py file and set it to the DATABASE_URL copied from Heroku.
  - Add os.environ["SECRET_KEY"] to your env.py file, copy the value of your SECRET_KEY in Heroku and paste it here.
- IMPORTANT! Make sure your env.py file is added to your .gitignore file so that your sensitive information is kept secret.
- Update the ALLOWED_HOSTS variable in the settings.py file by replacing *hj-itrain* with the name of your Heroku app. 
- Add, commit and push your changes to GitHub
- Login to Heroku from your terminal with: *heroku login -i*
- Get your app name from Heroku with: *heroku apps*
- Set the Heroku remote with: *heroku git:remote -a <app_name>*
- Push your changes to Heroku with: *git push heroku main*
- Run the app by clicking the Open app button on top of the page on the Heroku dashboard.
Good luck!

## Credits
### Code
¨¨
- [Django documentation](https://docs.djangoproject.com/en/4.0/)  
  If I had used a paper version of the Django documentation, I would have worn out the pages about Models and ModelForms.
- On a [Blog by Valentino Gagliardi](https://www.valentinog.com/blog/testing-django) I found tips about automatic testing in Django.
- [Blog by Hui Wen](https://www.huiwenteo.com/normal/2018/07/24/django-calendar.html). Here I found the code for the calendar.
- [Simple IT Rocks](https://simpleit.rocks/python/django/dynamic-add-form-with-add-button-in-django-modelformset-template/) is where I copied the code from to dynamically add exercise formsets to the Workout form.
- A post on [Stackoveflow](https://stackoverflow.com/questions/41129551/django-creating-an-if-statement-based-on-the-request-path-not-working) showed me how to highlight the active page in the navbar.
- I struggled for a while to add a filter to a formset field. This was where I found the solution: [Django project forum](https://forum.djangoproject.com/t/filter-dropdown-options-in-django-inline-formset-based-on-attribute-of-through-model/13374/4).
- As usual, [Stackoveflow](https://stackoverflow.com) has been frequently searched during the project, as well as [w3school](https://www.w3schools.com/).¨¨

### Other
¨¨
- The background image came from [pxhere](https://pxhere.com/sv/photo/1283826?utm_content=shareClip&utm_medium=referral&utm_source=pxhere), as well as the images on the about page.
- The Logo came from [focusfitness](https://www.focusfitness.net/stock-photos/downloads/fit-woman-chatting-phone-exercising-treadmill/).
- The colour scheme was extracted from the background image and some complementary colour were added on [coolors](https://coolors.co/).¨¨

## Acknowledgements
- First of all I want to thank my mentor, Narender Singh. As always he comes up with good ideas and useful hints. Thank you Narender for your support during my course at Code Institute!
- A big thank you to Sean and the other tutors who patiently guided me through some, quite embarrassing questions, which I should have solved on my own. (I think I blamed it on stressful times.) But who also helped me with some really tough ones which would have taken me forever to solve by myself. You're heroic!
- As usual the slack crowd can't be thanked enough. Especially I like to thank StevenW_5p for a lot of tips and encouragement all through this project.
- And a giant thank you to my, always supportive, friends from my very first Hackathon. Thanks Andrew, Patrik and Kat for your support through this project too and for the time you spent on checking the site!

## Conclusion
Finally my journey with Code Institute has come to an end. I am so grateful for this experience which has taken me to a new era in my life. I'm a bit nervous about the future but I feel that I'm ready to throw myself out there and try my wings.  
  
Happy Coding!

[Back to the top](#table-of-contents)