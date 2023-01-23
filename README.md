# The Seafood Shop - a catalog app
This is a catalog app with a content management system based on Wagtail and Django.

## Table of contents
- [Table of contents](#table-of-contents)
- [Introduction](#introduction)
- [Web page](#web-page)
- [Technologies](#technologies)
- [Features](#features)
- [Illustrations](#illustrations)

## Introduction
My friend asked me if I could create a simple catalog app with WordPress. I haven't ever worked with WordPress. So I wondered if there exists a Python framework or module that could give the same or even better functionality.
And I've found two Django-based modules: Django CMS and Wagtail. After testing both, I've chosen Wagtail as the perfect one. So this app has been created to try the module's functionality. And I really like the result.

So, let me introduce **The Seafood Shop** — a site catalog with a content management system.

## Web page
https://pycaramba.pythonanywhere.com/

## Technologies
- Python 3.10
- Django 4.1
- Wagtail 4.1
- Witenoise 6.3
- HTML 5
- CSS 3
- Bootstrap themes

## Features
For non-staff users, it's a simple site catalog with several addresses: Home, Products, About, and Contacts.

But authorized CMS staff can:
- Create, update or delete:
	- Pages
	- Elements for any page
	- Snippets: background image, favicon, header, navbar title
	- Navbar items
	- URLs and their names
- Change the order of elements for any page
- Publish, unpublish the pages and save their drafts
- Manage SEO elements for any page

For every element have been set the fields required to add the block. The maximum number of possible additional pages and their elements are provided in the backend. So it's a pretty flexible app for a customer.

## Illustrations
Managing:
- Home page:
  - Intro
  ![1 intro](https://user-images.githubusercontent.com/44866199/214112018-ee52e410-a8ee-4772-8d2a-ae92754c1637.gif)

  - Message
  ![2 message](https://user-images.githubusercontent.com/44866199/214112518-15132189-7db6-4691-910c-0dd68d5add24.gif)


- Snippets:
  - Background image
  ![1 bg](https://user-images.githubusercontent.com/44866199/214112939-a84df812-93c6-44b7-bd1e-b0d6fe9418bc.gif)

  - Header
  ![2 header](https://user-images.githubusercontent.com/44866199/214112969-70648eb0-f28f-4125-b2bb-7eefeb058658.gif)

  - Footer
  ![3 footer](https://user-images.githubusercontent.com/44866199/214112989-ba154a9a-8824-4892-9ff4-2dd6efacde4d.gif)

  - Favicon
  ![4 favicon](https://user-images.githubusercontent.com/44866199/214113013-cd8a5503-0d8a-43e4-84d2-a993839d3b51.gif)

  - Navbar title
  ![5 nav_title](https://user-images.githubusercontent.com/44866199/214113047-23b563af-22b5-4ef9-a225-55d46fa78931.gif)


- Products page:
  ![1 products](https://user-images.githubusercontent.com/44866199/214113455-c781814c-81e5-4a02-b9e6-61559a02e9df.gif)
  ![2 products](https://user-images.githubusercontent.com/44866199/214113465-fc642381-f39c-42cb-82ac-924591118b15.gif)


- About page:
  ![about](https://user-images.githubusercontent.com/44866199/214113797-95b2b379-a6be-4060-90b1-9ae84bf3dbfe.gif)


- Contacts page:
  ![contacts](https://user-images.githubusercontent.com/44866199/214113953-075bf8f5-50ba-4127-8962-2bc4b0d7bde1.gif)


- Navigation:
  ![nav](https://user-images.githubusercontent.com/44866199/214114308-6aed1228-7cef-4d14-8449-6829cbc3493a.gif)


- Redirection button for Home page:
  ![3 button](https://user-images.githubusercontent.com/44866199/214114482-a816d19d-76f9-427b-82d0-2fcf6c00532f.gif)
