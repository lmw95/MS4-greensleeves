# Testing

Find the testing for MS4 - Greensleeves

[Back to README](https://github.com/lmw95/MS4-greensleeves#ms4---greensleeves)

# Table of Contents
* [Validation](https://github.com/lmw95/MS4-greensleeves/blob/main/TESTING.md#validation)
* [Responsiveness](https://github.com/lmw95/MS4-greensleeves/blob/main/TESTING.md#responsiveness)
* [Browser compatability](https://github.com/lmw95/MS4-greensleeves/blob/main/TESTING.md#browser-compatability)
* [Testing user stories](https://github.com/lmw95/MS4-greensleeves/blob/main/TESTING.md#testing-user-stories)
* [Ongoing issues and bugs]()

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

7) As a site user, I want to be made aware of any deals or shipping discounts available

![](https://github.com/lmw95/MS4-greensleeves/blob/main/documentation/testing/us-7.png)

