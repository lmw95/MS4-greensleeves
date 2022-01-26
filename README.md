# MS4 - Greensleeves
Greensleeves is an e-Commerce site specialising in the sale of various indoor plants and accessories, and was created for educational purposes as the 4th milestine project for the Code Institute's Full Stack Software Development Diploma. 

# Table of contents
* UK
    * Strategy
    * User stories
    * Scope
    * Structure
    * Skeleton
    * Surface
* Features
    * Existing features
    * Features for future implementation
* Technologies
    * Languages
    * Libraries & frameworks
    * Database
    * Validation
    * Other tools
* Testing
    * Code validation
    * Testing user stories
    * Manual testing
    * Automated testing
    * Responsiveness
    * Accessibility
    * Compatability
    * Lighthouse reports
    * Bugs, major errors & fixes
* Deployment
* Credits
    * Code
    * Media
    * Content
    * Acknowledgements

# **UX**
## **Strategy**
***Introduction***

The rise of indoor plant sales, particularly amongst those between 18 and 30, has shot up almost 500% in recent years. Once thougth of as an 'old people's hobby', this increase in young people who are adopting the label of 'proud plant parents' is driving the demand for easy guidance to proper plant care and the availability of good quality plants to buy online.

Greensleeves offers a diverse range of high quality and well cared-for indoor plants at reasonable prices for the target demographic, along with various plant accessories such as pots, spray bottles, watering cans, propagation sets, plant food and more.

***Site owner goals***
* To increase customer base to include younger demographics
* To spread awareness of proper plant care amongst new plant owners through simple
* To offer tools to new plant parents with the aim of translating interest into sales 
* To spread the joy of plant ownership

***User goals***
* To access the website across multiple devices
* To discover new plants and tools
* To learn about proper plant care
* To buy plants and accessories from a trusted source

---

## **User stories**

***Site user***
* As a site user, I want to be able to browse the selection of plants and accessories so I can decide whether I want to make a purchase
* As a site user, I want to be able to easily navigate the site so I can get to the specifc section that I need
* As a site user, I want the website to be responsive so that I can access it on a variety of devices
* As a site user, I want to see information about the plants (sucb as ease of care, humidity, watering, light, air purifying, etc.) so that I can assess whether this plant is for me
* As a site user, I want to see suggested accessories on each plant page so that I know which tools I need should I buy this plant
* As a site user, I want to be able to contact the site owner should I have any questions
* As a site user, I want to be made aware of any deals or shipping discounts available
* As a site user, I want to be able to see the most popular plants on the site
* As a site user, I want to be able to read reviews of others that have used the site
* As a site user, I want to be able to visit the site's social media so that I can keep up with any deals or lates events
* As a site user, I want to be able to register with an account, so that I can see my past orders

***Shopper***
* As a shopper, I want to see prices of the plants and accessories so I can judge whether I can afford them
* As a shopper, I want to be able to filter search results or all items (for example by price, ease of care, plant type or plant origins etc.) so that I can quickly narrow down my search
* As a shopper, I want to be able to see all items or search for items and have my results displayed to me
* As a shopper, I want to be able to select quantity of items in case I want to buy more than one
* As a shopper, I want to be able to instantly see how many items are in my 'shopping bag' without needing to enter it
* As a shopper, I want to be able to see my 'shopping bag' so I can see what I'm planning to buy
* As a shopper, I want to be able to see the total of my 'shopping bag' 
* As a shopper, I want to enter payment information in a safe and secure way so that I can checkout quickly with confidence my details will be protected
* As a shopper, I want to receive confirmation of my order so that I can have a proof of purchase
* As a shopper, I want to be able to notify whether my items are a gift and the ability to write a personalised message 

***Account holder***
* As an account holder, I want to be able to log in and out safely
* As an account holder, I want to be able to edit my profile so that I can update my personal information
* As an account holder, I want to be able to reset my password if I forget it
* As an account holder, I want to delete my account so that my personal information are removed from the website
* As an account holder, I want to be able to favourite items so that I may come back to them at a later date
* As an account holder, I want to be able to leave a review of the website so that I can notify other users of my experience

***Administration***
* As site admin, I want to add, edit and delete an item and its contents so that the website stays up to date and accurate
* As site admin, I want to be able to add related products so that I can encourage multiple sales
* As site admin, I want to be able to edit most of the content of the website, so that I can keep my website up to date
* As site admin, I want to manage orders from the console so I can know I have dispatched orders

---

## **Scope**
***Functional requirements***
* Content
    * Responsive design 
    * Collapsable menu
* User authentication
    * User can register securely
    * User can log in / log out
    * User can edit profile information
    * User can view profile
    * User can delete profile
* Search & shop
    * See all items
    * Sort items by various filters 
    * Search website with search bar
    * Display search details
    * Paginate site items
* Shopping bag & checkout
    * Display shopping bag notification
    * Add / delete item
    * View shopping bag
    * Update quantities
    * Add / edit delivery information
    * Add gift option
    * Add gift option message
    * Enter payment details
    * Process & complete payment
    * Show order in user's account
* Feeback
    * Feedback on user authentication
    * Email to verify user email
    * Email for order confirmation
    * Email for order dispatch
    * Feedback for deleted user
* Contact & interaction
    * User can leave reviews
    * Display testimonials
    * Contact site owner
    * Links to social media
* Site administration
    * Add / edit / delete items
    * Add / edit / delete filters
    * Link items to filter categories
    * Display items 
    * Update all site content
* Inventory
    * Add stock quantities
    * Adjust stock quantities after orders
* Error handling
    * Handle errors 403, 404, 500

***Non-functional requirements***  
* Interactive components
* Navigatable and minimal design
* Aesthetically pleasing display of items and content

***Content rquirements***
* Details about company
* Information regarding plant care
* Information regarding accessories
* Images of plants and accessories
* Forms where user input is needed
* Attractive layout to guide users through site
* Icons for interactive elements and sub-sections

***Limitations***
* The site owner is in the process of learning Python and Django which may limit the features available on the website
* There is a time limit which may place constraints on certain elements which will need to be planned carefully

---

## **Structure**
***Architecture***

![](documentation/structure/information-architecture.png)

***Organisation***
* Header: Collapsable navbar with brand logo and navigation links
* Homepage: Hero image, information about the company, suggested plants, company reviews and offers on delivery etc.
* Profile: Registered users can see delivery info, preferred payment info, favourited items "for later"
* About: Company info, statements and history
* Plants: All the available plants to buy
* Accessories: All the available accessories to buy
* Product page: Information about the selected product
* Shopping bag: User's items to buy
* Contact us: Get in touch with company
* Footer: Social media links and statements

***Database structure***

[to be added]

--- 

## **Skeleton**

![](documentation/wireframes/homepage.png)

* [Homepage](https://github.com/lmw95/MS4-greensleeves/blob/main/documentation/wireframes/homepage.png)
* [About](https://github.com/lmw95/MS4-greensleeves/blob/main/documentation/wireframes/about.png)
* [Contact us](https://github.com/lmw95/MS4-greensleeves/blob/main/documentation/wireframes/contact.png)
* [Shop items](https://github.com/lmw95/MS4-greensleeves/blob/main/documentation/wireframes/shop.png)
* [Item page](https://github.com/lmw95/MS4-greensleeves/blob/main/documentation/wireframes/item-page.png)
* [Checkout](https://github.com/lmw95/MS4-greensleeves/blob/main/documentation/wireframes/checkout.png)
* [Sign in / log in](https://github.com/lmw95/MS4-greensleeves/blob/main/documentation/wireframes/signin-login.png)
* [Profile](https://github.com/lmw95/MS4-greensleeves/blob/main/documentation/wireframes/profile.png)
* [Shopping bag modal](https://github.com/lmw95/MS4-greensleeves/blob/main/documentation/wireframes/shopping-bag.png)
* [Order successful](https://github.com/lmw95/MS4-greensleeves/blob/main/documentation/wireframes/order-success.png)
* [FAQs](https://github.com/lmw95/MS4-greensleeves/blob/main/documentation/wireframes/faqs.png)
* [Statements](https://github.com/lmw95/MS4-greensleeves/blob/main/documentation/wireframes/statements.png)
* [Policies](https://github.com/lmw95/MS4-greensleeves/blob/main/documentation/wireframes/policies.png)

---

## **Surface**
The overall design of the website will be minimal with splashes of colour coming from the icons and certain sections of each page.

***Colour*** 

The colour palette will feature mostly 'Earthy' and muted colours, keeping in tone with the website's products. I chose the colours below using [Coolors]().

![](documentation/design/palette.png)

***Imagery***

The images used in the website will come from [Flaticon]() and are linked in the Credits section. All images will be relevant to the content they are used in conjunction with, and will be used sparingly throughout the site. 

***Typography***
* [Pacifico](https://fonts.google.com/specimen/Pacifico?category=Handwriting#standard-styles) will be used for the brand logo only
* [Prata](https://fonts.google.com/specimen/Prata?category=Serif) will be used for headers
* [Be Vietnam Pro](https://fonts.google.com/specimen/Be+Vietnam+Pro?category=Sans+Serif&preview.text=%C2%A315.00&preview.text_type=custom) will be used as the body text

***Iconography***

Icons will be from [FontAwesome](https://fontawesome.com/) and [Flaticon](https://www.flaticon.com/) and will be used to highlight certain bits of information or interactive elements like buttons


# Technologies
### **Languages**
* HTML
* CSS
* JavaScript
* Python

### **Libraries & frameworks**
* jQuery
* Django
* Gunicorn
* Jinja
* Bootstrap5
* FontAwesome
* AnimateCSS
* crispy-forms
* Google Fonts

### **Database, platforms & cloud storage**
* SQLite
* Heroku Postgres
* Amazon AWS S3
* Heroku

### **Validation**
* W3C Markup Validation Service
* W3C CSS Validator
* WAVE Web Accessibility Evaluation Tool
* PEP8 online
* JSHint
* Chrome DevTools
* Google lighthouse

### **Other tools**
* Flaticon
* Stripe
* Balsamiq
* Dbdiagram.io


# Credits

**Code, media and content**

[See all credits here]()

**Acknowledgements**
* Inspiration for this site comes from other plant sites such as [Beards & Daisies](https://www.beardsanddaisies.co.uk/cart)

