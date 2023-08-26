# Harry's Restaurant
Harry's Restaurant is a full-stack, responsive website built for a fictional Restaurant for educational purposes only.

It allows the user to create an account so they can make a booking at table at the restaurant. Users can also browse the menu, letting them veiw the delicious dishes that are on offer.

## Agile Methodology
The plan for this project was carried out using Agile Methodology. GitHub Issues were used to record the User Stories. These were made up of all the key functionality that a user would expect from a Restaurant website.

Each Each User Story contains Acceptance Criteria and Tasks which I sometimes had to adjust during the process, as I wasn't yet sure what was required to achieve the Acceptance Criteria.

To aid with prioritisation, I used The MoSCoW Method, which consisted of classifying each User Story as a 'Must Have', 'Should Have' or 'Could Have'. Some 'Could Have's didn't make it into the project and were left in the Backlog for a future iteration. It is important to note here, that by writing only enough User Stories to reach the Minimum Viable Product(MVP), 'Won't Have' was not included currently as a category.

To summarise, I found using the Agile Methodology of great benefit as it helped me to better organise, prioritise and plan the development of my project. Although I didn't give myself a specific duration for each iteration, it greatly helped my time management. I also felt sense of achievement, ticking off the Tasks while working on a User Story and placing it in the 'Done' column when it was completed.

## User Experience

### Strategy / Site Objectives
Harry's Restaurant aims to create an inviting and welcoming impression that makes it easy for people and their families and friends to enjoy a quality meal together.

It provides a simple way for people to book a table and organise a nice get-together for a special occasion.

The target audience aimed towards people aged 18 years+, however anyone is welcome to Harry's Restaurant.

### Scope / User Stories

* **First Time Visitor Goals**
    * As a first time user, I want to be about to sign up to an account to have access to other features such as making a booking.
    * As a first time user, I want to be able to view the menu so that I can so what food is available.
            
* **Returning Visitor Goals**            
    * As a returning visitor, I would like to see if there are any changes to the menu.
    * As a returning visitor, I would like to know what if there are any changes to the opening times.
    * As a returning visitor, I would like to know any updates on the contact details.
    * As a returning Visitor, I would like to be able to find links to the social media pages of the restaurant.

* **Authenticated User Goals**
    * As an authenticated user, I want to be able to book a table at the restaurant to reserve a space.
    * As an authenticated user, I want to be able to make changes to my reservation such as the date or the time or number of people attending.
    * As an authenticated, user I want to be able to view all of the bookings that I have made to easily manage them
    * As an authenticated user, I would like to be able to cancel any bookings that I have made.

### Structure / Designs Choices

The website is simple to use and consistent within its structure. The website was designed to be responsive on screens from 375px and above, making it great ti use from mobile to desktop.

For desktop users the navigation bar shows the 'Harry's Restaurant' logo and links to pages for 'Home', 'Bookings', 'Menu' and 'Logout' (for authenticated users) or 'Sign up' and 'Login' pages (for unauthenticated users). For users on a screen size of 767px or below the navigation bar will collapse down and be accessible via a burger button to save screen space and a more polished appearance. The navigation bar is repeated across all pages on the site, allowing for easy navigation.

The Footer displays social media links which open in a separate tab for ease of use. It also displays the restaurants's address, the opening hours and other contact details. The footer is also repeated across all pages to keep the design uniform and for ease of access.

The Home Page clearly indicates the purpose of the site with a jumbotron which will urge users to sign up (for unauthenticated users) or book a table (for authenticated users). Below is a description of the restaurant which describes the style of cuisine on offer and an 'Our Story' section, which gives insight to the orgins of the restaurant and its mission.

The Bookings page allow users to easily see all of there bookings that have been made and clearly display the details of the booking. Users can also edit and cancel any of their bookings as well as add a new booking from this page. Users can also click the booking number of any booking to see the details of that particular booking.

The Menu page clearly shows the user what food the restaurant has on offer. the dishes are broken down in categories of Starters, Mains and Deserts.

The Sign up / Login pages are clear and and display the fields in a familiar format to the user.

#### Database Schema

One custom model has been implemented for this project: Reservation.

![This is an image of my Entity Relatated Diagram](readme_images/harrys_restaurant_erd.jpeg)

### Skeleton / Wireframes

Using wireframes greatly aided the planning process and allowed me to have a clear direction I want the structure of the project to go. I only completed wireframes for the Home and Booking pages as these were the only pages, that I felt, that need attention to their structure. The other pages are very basic and did not need much planning if any at all.

[Click here to view the home page wireframe](readme_images/harrys_restaurant_home_wf.pdf)

[Click here to view the bookings page wireframe](readme_images/harrys_restaurant_bookings_wf.pdf)

> [!NOTE]
> Wireframes are not coming out quite as planned but the primary structure is still visible.

### Surface

#### Colour Scheme

The colour scheme that I used was very monochromatic, with splashes of colour for items of interest such as buttons or links.

The primary background colour is White with black text for easy readablility. The jumbotron used on the home page is a contrast to this colour scheme, which has a black background and white text, to indicate the start and end of a new section.

#### Typography

The two fonts I used for this project were EB Garamond and Roboto. EB Garamond was used for the main headings of the site and Roboto was used for the main body of text. EB Garamond is a serif based font while Roboto is a sans-serif which enabled them to offer a good contrast and compliment eachother well while still being easily readable.

#### Icons

Icons were used to display the social media icons in the footer as I found it an easy and intuitive was of displaying the links to the user. Aria-labels are used on the links to help assist screen readers.

## Feautures

### Existing Features

#### Header & Navigation

The header and navigation are displayed across all pages and includes a link on the Logo which brings the user to the home page. For medium screen sizes and below a hamburger button appears, which expands to show the navigation list with links to the Home, Bookings, Menu, Register and Login pages. This helps reduce the clutter on the header by keeping the page links neatly stowed away until the user clicks the hamburger button.

Links to the Home, Bookings, Menu, Register and Login pages on desktop, are displayed openly across the header, which help the user to navigate easily from page to page, without having to revert back to the previous page via the back button. 

When a user is authenticated the Register and Login links will be replaced with a Logout link.

#### Footer

The footer, which is displayed across all pages and is fully responsive, includes the opening times of the restaurant, links to social media pages, the address of the restaurant and other major contact details.

The social media links utilize the hover CSS pseudo-class which gives a good visual indication to the user that they are hovering over a link.

#### Home Page Jumbotron

The Home Page jumbotron is big and bold, enabling it to catch the users attention. This is a dynamic feature that will promt the user to sign up and register if they are not authenticated or alternatively, it will promt the user to make a booking if they are authenticated.

#### Home page content

The rest of the content on the home page tells the user a little bit about the restaurant such as its origin story, what it values and the mission as a restaurant.

#### Bookings Page

The Bookings page is a place where user can go to for anything related to the bookings. The can add, edit, cancel and view their current bookings.

Booking details are listed in date order and display all of the key details of the bookings.

This page requires the user to be authenticated should they try and access the page via the URL directly.

#### Booking Details Page

The Booking Details page is a page that will display the booking details of a specific booking. It is access by clicking the booking number of a booking on the Bookings page.

This page requires the user to be authenticated should they try and access the page via the URL directly.

#### Add Booking Page

This page generates a form based from the Reservation model that the user can fill in to create a booking. The form is validated and the user cannot submit out the form if it is incomplete.

This page requires the user to be authenticated should they try and access the page via the URL directly.

#### Edit Booking Page

This page generates a form automatically filled with the details of the booking that is being edited. The form is based from the Reservation model and has all of the required field to input the data correctly

This page requires the user to be authenticated should they try and access the page via the URL directly.

#### Cancel Booking Page

If the user wish to cancel a booking, they are asked to confirm the cancelation. The page displays the booking details of the booking that the user wishes to cancel so they can be sure they are canceling the corrrect booking.

This page requires the user to be authenticated should they try and access the page via the URL directly.

#### The Menu Page

This page display all of the dishes the restaurant has to offer in a clear and easy to read format that makes it easy for the user to make their choice.

#### Registration Page

This is the page that a user will come to if they wish to create an account. The form template is generated using [django-allauth](https://django-allauth.readthedocs.io/en/latest/) and it is comprised of the following fields:
* Username
* Email
* Password
* Password (again)

The addition of the second password field ensures that the user does not make a mistake in setting up their account.

If the user already has an account, they can login in using the link that will take them to the login page

#### Login Page

This is the page that a user will come to if they wish to create an account. The form template is generated using [django-allauth](https://django-allauth.readthedocs.io/en/latest/) and it is comprised of the following fields:
* Username
* Password

If the user has not created an account they can sign up using the link that will take them to the registration page.

#### Logout page

Users can easily logout via the logout page. Users are asked if they are sure they wish to logout and once confirmed, the user is logged out and directed to the home page.

The form template is generated using [django-allauth](https://django-allauth.readthedocs.io/en/latest/).

### Future Features

* I look to implement a Google Map API and assign it to the restaurants location so that users can see the location on a map.

* I would like to notify the user when they login our logout with an alert so they are confirmed of the change in authentication.

## Technologies Used

### Languages
* [HTML5](https://en.wikipedia.org/wiki/HTML5)
* [CSS3](https://en.wikipedia.org/wiki/CSS)
* [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Libraries and Frameworks
* [Django 3.2.20](https://docs.djangoproject.com/en/4.2/releases/3.2.20/) - Free and open source Python Web Framework
* [Gunicorn 21.2.0](https://docs.gunicorn.org/en/stable/) - A Python WSGI HTTP server compatible with Django and used to run the project on Heroku
* [PostregSQL 0.5.0](https://www.postgresql.org/) - A powerful, open-source object-relational database system
* [Psycopg 2.9.6](https://www.psycopg.org/docs/) - A PostgreSQL database adapter for Python
* [Cloudinary 1.33.0](https://cloudinary.com/) - A persistent file store for media
* [Heroku](https://dashboard.heroku.com/) - A cloud platform used to deploy the project
* [ElephantSQL](https://www.elephantsql.com/) - PostgreSQL database hosting service
SQLite3 - The database provided by Django
* [Django-allauth](https://django-allauth.readthedocs.io/en/latest/) - - Integrated set of Django applications used for authentication and registration
* [Bootstrap 5.2.3](https://getbootstrap.com/docs/5.2/getting-started/introduction/) - A Framework for building responsive, mobile-fist sites



## Testing

## Deployment

### Forking the Github repository

### Creating a local clone

## Credits

### Code

## Acknowledgements