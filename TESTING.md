# Testing

Find the testing for MS4 - Greensleeves

[Back to README](https://github.com/lmw95/MS4-greensleeves#ms4---greensleeves)

# Table of Contents
* [Validation](https://github.com/lmw95/MS4-greensleeves/blob/main/TESTING.md#validation)
* [Responsiveness](https://github.com/lmw95/MS4-greensleeves/blob/main/TESTING.md#responsiveness)
* [Browser compatability](https://github.com/lmw95/MS4-greensleeves/blob/main/TESTING.md#browser-compatability)
* [Testing user stories](https://github.com/lmw95/MS4-greensleeves/blob/main/TESTING.md#testing-user-stories)
* [Issues and bugs](https://github.com/lmw95/MS4-greensleeves/blob/main/TESTING.md#issues-bugs)

## **Validation**

**PEP8 - Python**

1st round testing revealed the following errors:

![](https://github.com/lmw95/MS4-greensleeves/blob/main/documentation/testing/python-errors.png)
![](https://github.com/lmw95/MS4-greensleeves/blob/main/documentation/testing/python-errors-2.png)
![](https://github.com/lmw95/MS4-greensleeves/blob/main/documentation/testing/python-errors-3.png)
![](https://github.com/lmw95/MS4-greensleeves/blob/main/documentation/testing/python-errors-4.png)

* I fixed all similar errors throughout the project and removed whitespaces, made lines shorter and ensured correct spacing

**JSHint - JavaScript**

1st round testing revealed no errors for script.js and stripe-js-elements.js

![](https://github.com/lmw95/MS4-greensleeves/blob/main/documentation/testing/js-errors-script.png)
![](https://github.com/lmw95/MS4-greensleeves/blob/main/documentation/testing/js-errors-stripe.png)

**W3C CSS Validator - CSS**

1st round testing - the following errors were found:

![](https://github.com/lmw95/MS4-greensleeves/blob/main/documentation/testing/css-errors.png)
![](https://github.com/lmw95/MS4-greensleeves/blob/main/documentation/testing/css-errors-2.png)

* The 69 errors were from the AOS library, which the developer could not amend
* After the other css errors were fixed, no more errors were shown

**W3C Markup Validator - HTML**

1st round testing - the following errors were found:

![](https://github.com/lmw95/MS4-greensleeves/blob/main/documentation/testing/markup-errors.png)

* After fixing these errors, no errors were shown

## **Responsiveness**

The website was tested in Google Chrome using the Viewport Resizer extension, Chrome DevTools and the Responsive Design Checker.

The website's layout was tested pixel by pixel and on all popular mobile and tablet devices. The design is consistently responsive at all screen sizes and there is no change in the appearance or performance of interactive features.

There were, however, some issues with layout and aesthetics for screens smaller than 300px, notably the Galaxy Fold. As it is important to keep websites up-to-date with the latest devices, I amended the site to improve the layout on these screens.

Before:

![](https://github.com/lmw95/MS4-greensleeves/blob/main/documentation/testing/responsive-errors.png)

After:

![](https://github.com/lmw95/MS4-greensleeves/blob/main/documentation/testing/responsive-fix.png)

## **Browser compatability**

The application was tested in the following browsers:

Google Chrome
Microsoft Edge
Opera
Safari

The application proved itself highly compatible with all browsers and performance was consistent across all.

## **Testing user stories**

1) As a site user, I want to be able to browse the selection of plants and accessories so I can decide whether I want to make a purchase

![](https://github.com/lmw95/MS4-greensleeves/blob/main/documentation/testing/us-1.png)

* Verdit: PASS

2) As a site user, I want to be able to easily navigate the site so I can get to the specifc section that I need

![](https://github.com/lmw95/MS4-greensleeves/blob/main/documentation/testing/us-2.png)

* Verdict: PASS

3) As a site user, I want the website to be responsive so that I can access it on a variety of devices

![](https://github.com/lmw95/MS4-greensleeves/blob/main/documentation/testing/us-3(1).png)
![](https://github.com/lmw95/MS4-greensleeves/blob/main/documentation/testing/us-3(2).png)
![](https://github.com/lmw95/MS4-greensleeves/blob/main/documentation/testing/us-3(3).png)

* Verdict: PASS

4) As a site user, I want to see information about the plants (sucb as ease of care, humidity, watering, light, air purifying, etc.) so that I can assess whether this plant is for me

![](https://github.com/lmw95/MS4-greensleeves/blob/main/documentation/testing/us-4.png)

* Verdict: PASS

5) As a site user, I want to see suggested accessories on each plant page so that I know which tools I need should I buy this plant

![](https://github.com/lmw95/MS4-greensleeves/blob/main/documentation/testing/us-5.png)

* Verdict: PASS

6) As a site user, I want to be able to contact the site owner should I have any questions

![](https://github.com/lmw95/MS4-greensleeves/blob/main/documentation/testing/us-6(1).png)
![](https://github.com/lmw95/MS4-greensleeves/blob/main/documentation/testing/us-6(2).png)

* Verdict: PASS

7) As a site user, I want to be made aware of any deals or shipping discounts available

![](https://github.com/lmw95/MS4-greensleeves/blob/main/documentation/testing/us-7.png)

* Verdict: PASS

8) As a site user, I want to be able to visit the site's social media so that I can keep up with any deals or lates events

![](https://github.com/lmw95/MS4-greensleeves/blob/main/documentation/testing/us-8.png)

* Verdict: PASS

9) As a site user, I want to be able to register with an account, so that I can see my past orders

![](https://github.com/lmw95/MS4-greensleeves/blob/main/documentation/testing/us-9.png)

* Verdict: PASS

10) As a shopper, I want to see prices of the plants and accessories so I can judge whether I can afford them

![](https://github.com/lmw95/MS4-greensleeves/blob/main/documentation/testing/us-1.png)

* Verdict: PASS

11) As a shopper, I want to be able to filter search results or all items (for example by price, ease of care, plant type or plant origins etc.) so that I can quickly narrow down my search

![](https://github.com/lmw95/MS4-greensleeves/blob/main/documentation/testing/us-4.png)
![](https://github.com/lmw95/MS4-greensleeves/blob/main/documentation/testing/us-10.png)

* Verdict: PASS

12) As a shopper, I want to be able to see all items or search for items and have my results displayed to me

![](https://github.com/lmw95/MS4-greensleeves/blob/main/documentation/testing/us-10.png)

* Verdict: PASS

13) As a shopper, I want to be able to select quantity of items in case I want to buy more than one

![](https://github.com/lmw95/MS4-greensleeves/blob/main/documentation/testing/us-11.png)

* Verdict: PASS

14) As a shopper, I want to be able to see my 'shopping bag' so I can see what I'm planning to buy

![](https://github.com/lmw95/MS4-greensleeves/blob/main/documentation/testing/us-12.png)

* Verdict: PASS

15) As a shopper, I want to be able to see the total of my 'shopping bag'

![](https://github.com/lmw95/MS4-greensleeves/blob/main/documentation/testing/us-12.png)
![](https://github.com/lmw95/MS4-greensleeves/blob/main/documentation/testing/us-13.png)

* Verdict: PASS

16) As a shopper, I want to enter payment information in a safe and secure way so that I can checkout quickly with confidence my details will be protected

![](https://github.com/lmw95/MS4-greensleeves/blob/main/documentation/testing/us-14.png)

* Verdict: PASS

17) As a shopper, I want to receive confirmation of my order so that I can have a proof of purchase

![](https://github.com/lmw95/MS4-greensleeves/blob/main/documentation/testing/us-15.png)

* Verdict: 

18) As an account holder, I want to be able to log in and out safely

![](https://github.com/lmw95/MS4-greensleeves/blob/main/documentation/testing/us-16(1).png)
![](https://github.com/lmw95/MS4-greensleeves/blob/main/documentation/testing/us-16(2).png)

* Verdict: PASS

19) As an account holder, I want to be able to edit my profile so that I can update my personal information

![](https://github.com/lmw95/MS4-greensleeves/blob/main/documentation/testing/us-17(1).png)
![](https://github.com/lmw95/MS4-greensleeves/blob/main/documentation/testing/us-17(2).png)

* Verdict: PASS

20) As an account holder, I want to delete my account so that my personal information are removed from the website

![](https://github.com/lmw95/MS4-greensleeves/blob/main/documentation/testing/us-18(1).png)
![](https://github.com/lmw95/MS4-greensleeves/blob/main/documentation/testing/us-18(2).png)

* Verdict: PASS

21) As an account holder, I want to be able to view exclusive blog posts and leave comments as feedback

![](https://github.com/lmw95/MS4-greensleeves/blob/main/documentation/testing/us-19(1).png)
![](https://github.com/lmw95/MS4-greensleeves/blob/main/documentation/testing/us-19(2).png)

* Verdict: PASS

22) As site admin, I want to add, edit and delete an item and its contents so that the website stays up to date and accurate

![](https://github.com/lmw95/MS4-greensleeves/blob/main/documentation/testing/us-20(1).png)
![](https://github.com/lmw95/MS4-greensleeves/blob/main/documentation/testing/us-20(2).png)

* Verdict: PASS

24) As site admin, I want to be able to add related products so that I can encourage multiple sales

![](https://github.com/lmw95/MS4-greensleeves/blob/main/documentation/testing/us-21(1).png)
![](https://github.com/lmw95/MS4-greensleeves/blob/main/documentation/testing/us-21(2).png)

* Verdict: PASS

25) As site admin, I want to be able to edit most of the content of the website, so that I can keep my website up to date

![](https://github.com/lmw95/MS4-greensleeves/blob/main/documentation/testing/us-20(1).png)
![](https://github.com/lmw95/MS4-greensleeves/blob/main/documentation/testing/us-20(2).png)

* Verdict: PASS

26) As site admin, I want to manage orders from the console so I can keep up to date with them

![](https://github.com/lmw95/MS4-greensleeves/blob/main/documentation/testing/us-21.png)

## **Bugs & issues**

The list of persistant issues throughout the project are listed below:

1) 
* ISSUE: A major and persisitant issue during development involved confirmation emails not being sent to the user upon successful checkout, sending verification emails to the user upon sign up
* FIX: Changing the gmail configuation settings in settings.py by adding forgotten envionment variables to condition when development is off
* [Commit]()

2)
* ISSUE: A parallel issue to the confirmation emails was that the emails were still not being sent upon order confirmation
* FIX: There was a typo with the email files, which were fixed and sorted the issue
* [Commit 1](https://github.com/lmw95/MS4-greensleeves/commit/baef4ebfd53badeec4a84a68f3ad2f0a0b638769)
* [Commit 2](https://github.com/lmw95/MS4-greensleeves/commit/9b3f8e8d48dcb2bc9f57386ce62133b1df45c928)

3)
* ISSUE: Trying to conduct a search query would throw a 500 error
* FIX: Old model fields that were not deleted from the query fields, these were deleted and fixed the error
* [Commit](https://github.com/lmw95/MS4-greensleeves/commit/015f4dd7e8c470c2ac214821602057c3b4f980f2)

4)
* ISSUE: The payments would not process, Stripe would throw an error that declared 'unknown parameters: country, postcode' on attempt to checkout 
* FIX: I had to change 'state' to 'country' in stripe_elements.js
* [Commit](https://github.com/lmw95/MS4-greensleeves/commit/b6ffb62c413657d2f2557d21e5240c8118279802)