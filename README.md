# Hillbox
Hillbox is a place for freeflight pilots (paraglider, hang-glider) to store information about locations to enjoy a flight. It allows pilots to share locations and hosts an image gallery for pilots to share beautiful moments with the community.

![Screenshot 2022-10-31 at 18 25 11](https://user-images.githubusercontent.com/98256205/199082074-0a301637-4497-44d1-86f5-61fdce8cdaef.png)

Please view the live website here: [Hillbox](https://hillbox-pp4.herokuapp.com/ "Hillbox Homepage").

## Table of contents

## UX
### Site Purpose
The site allows for information about a freeflight location to be uploaded and shared with other users. There is an image gallery also. Both of these features allow commenting in order to allow users to add important information to uploaded items.

### Site Goal
The intent of the site is to allow paragliding and hangglider pilot's to share their knowledge of flying sites and hazards. The site looks to be simple and easy to use when out on the trails or whilst piloting an aircraft.

### Audience
This site is intended for use by paragliding and hanggliding pilots of all ages.

### Communication
The UI is intended to be simplistic as clarity of information is paramount when planning flights. I wanted each action to be a clear as possible and easy to find without taking up too much brain power. This is incase the app needed to be used in an emergency to plan a landing.

### Current User Goals
For pilot's to be able to share important information. This makes flying safer for visiting pilot's and locals alike.

### New User Goals
To find it simple to navigate and find information as well as add to existing information.

### Future Goals
- Users can choose the location of a site by dropping a pin on a map. This would be relayed to the database.
- Users can view all sites on a map. 
- Users can search by wind direction.
- Users can view local weather information for a site.

## User Stories
I have used a scale of 1 to 5 for story points. 1 being the least effort involved.

### Pilot 
- As a user I want a contact form so that I can contact the admin team. 3
- As a user I want to be able to access an upload form so that I can upload a flying site. 4
- As a user I want access an edit form so that edit a flying site. 4
- As a user I want access an delete form so that delete a flying site. 3
- As a user I want to be able to access an upload form so that I can upload a gallery image. 4
- As a user I want access an edit form so that edit a gallery image. 4
- As a user I want access an delete form so that delete a flying site. 3
- As a user I want a comment form so that I can leave comments on a flying site. 4
- As a user I want a delete button so that I can delete my comments on flying sites. 3
- As a user I want an edit comment button so that I can edit comments on a flying site. 4
- As a user I want a comment form so that I can leave comments on a gallery image. 4
- As a user I want a delete button so that I can delete my comments on gallery images. 3
- As a user I want an edit comment button so that I can edit comments on a gallery image. 4
- Can sign up/login. 2

### Admin
- As an admin I want an admin panel so that I can moderate the uploaded content and accounts. 1

## Design
### Wireframes
![Screenshot 2022-10-31 at 19 40 49](https://user-images.githubusercontent.com/98256205/199098676-8eec68d0-13ed-42dd-bd33-db191085ca8c.png)
![Screenshot 2022-10-31 at 19 52 14](https://user-images.githubusercontent.com/98256205/199098744-0482daf9-192b-4d20-ad0e-97cb07ed4cfa.png)
![Screenshot 2022-10-31 at 19 50 26](https://user-images.githubusercontent.com/98256205/199098748-a8fd436e-63bf-4368-a04b-e90445e5e930.png)
![Screenshot 2022-10-31 at 19 49 59](https://user-images.githubusercontent.com/98256205/199098750-db329711-089e-4995-abe2-f800f1e4ecfc.png)
![Screenshot 2022-10-31 at 19 50 26](https://user-images.githubusercontent.com/98256205/199098893-e3b23efd-6060-424c-ac08-caa9b4bf839e.png)
![Screenshot 2022-10-31 at 19 48 14](https://user-images.githubusercontent.com/98256205/199098896-89b9db9e-b344-4cde-83ba-24ee3a9314dc.png)
![Screenshot 2022-10-31 at 19 47 48](https://user-images.githubusercontent.com/98256205/199098899-bf88b105-f916-42fc-ba88-a842967c9e54.png)

### Site Navigation
![Screenshot 2022-10-31 at 20 14 36](https://user-images.githubusercontent.com/98256205/199101888-6c6888a0-eb62-43b9-8e41-c0cf62fa62a6.png)

### Database Schema
![Screenshot 2022-10-31 at 20 34 37](https://user-images.githubusercontent.com/98256205/199105261-70eaa53f-1f70-4d2a-8707-141dbcc1f00a.png)

### Color Scheme
![Screenshot 2022-10-31 at 20 40 03](https://user-images.githubusercontent.com/98256205/199106205-32e6aa31-5c54-4f68-a2e0-b5e718658aee.png)

### Typography:
All fonts were obtained from the Google Fonts library. I chose the following fonts for the page:

Monserrat: Site heading/logo, homepage.
Lato: upload and contact forms.

### Imagery:
- The homepage features a paragliding image from Pexels.
- There is a wiki image on the sample site "Claragh" from their page about the mountain.
- There is an image taken by one of the club members in the gallery under the title "Old Head".

## Features
### Homepage
![127 0 0 1_8000_](https://user-images.githubusercontent.com/98256205/199226713-d1d921d0-1425-4e39-86ca-c85ec9adb83f.png)

### Flying Sites
![127 0 0 1_8000_sites_](https://user-images.githubusercontent.com/98256205/199226892-9a2eb18e-9cdc-4618-ac06-0b98aa361cf6.png)

### Site detail
![127 0 0 1_8000_sites_7_](https://user-images.githubusercontent.com/98256205/199227016-3406cd4b-ba74-4d1f-a255-984113d44687.png)

### Gallery
![127 0 0 1_8000_gallery_](https://user-images.githubusercontent.com/98256205/199227084-f6a7926a-f5d7-4ae0-8101-e5171f85017d.png)

### Gallery detail
![127 0 0 1_8000_gallery_4_](https://user-images.githubusercontent.com/98256205/199227176-69d89251-4538-4796-a477-53634bfcd7ec.png)

### Contact Page
![127 0 0 1_8000_contact_](https://user-images.githubusercontent.com/98256205/199227280-779d8fc7-f226-43ed-b2e0-0e258a2710f7.png)

### Sign-in
![127 0 0 1_8000_accounts_login_](https://user-images.githubusercontent.com/98256205/199227390-e8823f99-ab77-4bfb-aa12-0a58b7259b55.png)

### Sign-out
![127 0 0 1_8000_accounts_logout_](https://user-images.githubusercontent.com/98256205/199227701-1fa01702-47e1-4ac6-9b31-a7975ffcd82b.png)

### Sign-up
![127 0 0 1_8000_accounts_signup_](https://user-images.githubusercontent.com/98256205/199227834-a5a9ba07-2a7c-47f3-a20e-fecd532b1f64.png)

## C.R.U.D.
### Create
### Site Upload
![127 0 0 1_8000_site_upload_](https://user-images.githubusercontent.com/98256205/199229097-2ffdf722-30c7-44f7-9114-b95ed4863df6.png)

### Gallery Upload
![127 0 0 1_8000_gallery_upload_](https://user-images.githubusercontent.com/98256205/199261093-f8a7b93b-82d5-4fc9-89ff-d08e2ffac493.png)

### Site comments (gallery comments are the same)
![Screenshot 2022-11-01 at 14 46 00](https://user-images.githubusercontent.com/98256205/199261707-a1209873-aa8a-4f2a-baf6-c780780030b6.png)

## Read
See above for flying site and gallery image pages.

## Update
When the logged in user is the author, they may edit the posts.

### Edit Site
![Screenshot 2022-11-01 at 14 48 32](https://user-images.githubusercontent.com/98256205/199262261-bdab8af1-b086-46be-b31c-d9172a11c1f3.png)

### Edit Gallery Image
![Screenshot 2022-11-01 at 14 49 35](https://user-images.githubusercontent.com/98256205/199262434-9df72544-fd66-41ad-971d-ae67d3ad6d1a.png)

### Edit Comment
![127 0 0 1_8000_site_comment_edit_4](https://user-images.githubusercontent.com/98256205/199265774-5794d3d4-a49a-4aa6-9c75-52d3da6a4397.png)

## Delete
### Delete Gallery Image
![127 0 0 1_8000_gallery_delete_Admin_4](https://user-images.githubusercontent.com/98256205/199264252-234c3513-e3a0-441d-97a0-0674358c014f.png)

### Delete Flying Site
![127 0 0 1_8000_delete_7](https://user-images.githubusercontent.com/98256205/199264636-4e0027c7-25af-4c21-928e-d7d154e1fcca.png)

### Delete a comment
![127 0 0 1_8000_gallery_comment_delete_3](https://user-images.githubusercontent.com/98256205/199266930-97a1a215-2225-405c-9eec-b14735434d8e.png)

## Future features
- Password reset
- Social media sign-in
- Map location input and output for flying site upload form
- Search by location/ wind direction
- Pilot profiles

## Testing
### Homepage
- I have manually tested every link on the homepage to ensure that it redirects to the appropriate url. 
- I have tested that the "Sign in" buttons appear appropriately depending on login state.

### Flying Sites
- I have tested that only the approved sites can be seen in the listing.
- I have tested that the "EDIT"/"DELETE" buttons only show for the user that is authenticated and is the creator.
- I have tested that the "EDIT"/"DELETE" buttons perform the required function.
- I have tested that images are resized appropriately prior to display for a good UX/UI.
- I tested that the add site link performs its function and is exchanged for a sign in link if the user is not authenticated.
- Checked that authentication related changes are in line with design.

### Gallery Images
- I have tested that only the approved images can be seen in the listing.
- I have tested that the "EDIT"/"DELETE" buttons only show for the user that is authenticated and is the creator.
- I have tested that the "EDIT"/"DELETE" buttons perform the required function.
- I have tested that images are resized appropriately prior to display for a good UX/UI.
- I tested that the add site link performs its function and is exchanged for a sign in link if the user is not authenticated.
- Checked that authentication related changes are in line with design.

### Comments
- I have tested that only the approved comments can be seen in the listing.
- I have tested that the "EDIT"/"DELETE" buttons only show for the user that is authenticated and is the creator.
- I have tested that the "EDIT"/"DELETE" buttons perform the required function.
- I have tested that images are resized appropriately prior to display for a good UX/UI.
- I tested that the add site link performs its function and is exchanged for a sign in link if the user is not authenticated.
- Checked that authentication related changes are in line with design.

### Browsers
- I checked the site for compatibility on different browsers.
- I have checked the responsiveness on different window sizes.

## Validator Testing
- HTML files pass through the W3C validator with no issues found.
- CSS files pass through the Jigsaw validator with no issues found.
- Python files have been through the validator and have no issues.

## Accessibility
![Screenshot 2022-11-02 at 20 35 23](https://user-images.githubusercontent.com/98256205/199597336-66794243-83a0-4258-9ae1-37f26402fd43.png)



 








