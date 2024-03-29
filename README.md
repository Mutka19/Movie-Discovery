# project1-ies26
### Overview
This app was built using the flask framework written in python. It includes the followig libraries:
<ul>
    <li> random
    <li> requests
    <li> json
    <li> os
    <li> dotenv
    <li> flask
</ul>

If you were to fork this repo you would need to install all libraries from the requirements.txt file, as well as get a TMBD api key and set it as an environmental variable called TMBD_API_KEY. You also need a postgresql database that you will need to assign to an environment variable called DATABASE_URL to. Finally you will need an environment variable called SUPER_SECRET_KEY.

After this you can run it locally on your machine by uncommenting <strong> app.run(debug=True) </strong> from the bottom of the movie-handler.py file. The movie-handler.py file contains all the backend code, the api_handler.py file contains all the logic related to the APIs and their functionality. The templates folder contains the html for the frontend of the website and the static folder contains the CSS used to style it.

 ### Technical Issues
 #### 1
 I ran into isssues when trying to deploy this app to fly.io, the flyctl command line tool incorrectly recognized my app as a django project and built the dockerfile under that assumption. I had to manually change a few lines in the file to get my code to deploy.
 #### 2
 I also had issue using the wikimedia API as I couldn't find much great documentation on it. At first I wasn't able to figure out how to extract links from the json request best I was able to come up with a decently clever solution for it. I also had an issue with sorting certain searches to only return films instead of search directories or possibly other media that had the same name. To fix this I maade a query that would return all items with that name, then I would return the page link of the result that contain the keyword film in its category list.
 #### 3
 I had a hard time figuring out how to get the review objects to work in the postgresql. However once I figured that out, things went swimmingly.
 #### 4
 I ended up spending a lot of time troubleshooting deployment. I found it difficult to fix since my issue was with my database url. I had mistakenly added an extra 's' to postgress and since the fly.io secrets are only viewaable as digests I couldn't tell it was misspelled. After a while I tried reseting my secrets and it worked. It was frustrating after spedning so much time looking for errors elsewhere but I was relieved to  have finished on time
 ##### 5
 I also decided not to have my page locked by a login. Which was a little different than what was on the assignment directions. However I did restrict the users access so that they could not leave reviews on the site until they logged in. They are only able to look at the movies using the search bar until they sign up and log in.

 ### Known problems/Possible improvements
 #### Problem
 ##### 1
 Currently for certain searches where no results are found, the website crashes. I would like to fix this in the future by implemented try/except blocks to return safe data and informs the user that the entery they searched for was either invalid or does not exist.
 ##### 2
 When I try to open up more than 1 page I get an internal server error. I'm not sure how to fix this but it may just have to do witht the fact that I have the unpaid version of fly.io
 ##### 3
 I do not have any error for trying to turn in a review with and empty review textbox so that may cause an error. I would've liked to have fixed this and added error handling for the review page if I had more time.
#### Improvement
##### 1
One improvement that I would like to make would be to improve the looks of the page. At the moment it is very basic and does not have much personallity but given some time I would love to beautify it and make it unique.
##### 2
I would also like to add a way for all comments to be shown in a list, or maybe have a way to iterate through them. ANd then on top of that I would've liked to have made a way to rank comments by helpfullness.

##### fly.io link
[Click here to view website!](https://movie-discovery.fly.dev/)