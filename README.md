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

If you were to fork this repo you would need to install all libraries from the requirements.txt file, as well as get a TMBD api key and set it as an environmental variable called TMBD_API_KEY. 

After this you can run it locally on your machine by uncommenting <strong> app.run(debug=True) </strong> from the bottom of the movie-handler.py file. The movie-handler.py file contains all the backend code, the api_handler.py file contains all the logic related to the APIs and their functionality. The templates folder contains the html for the frontend of the website and the static folder contains the CSS used to style it.

 ### Technical Issues
 #### 1
 I ran into isssues when trying to deploy this app to fly.io, the flyctl command line tool incorrectly recognized my app as a django project and built the dockerfile under that assumption. I had to manually change a few lines in the file to get my code to deploy.
 #### 2
 I also had issue using the wikimedia API as I couldn't find much great documentation on it. At first I wasn't able to figure out how to extract links from the json request best I was able to come up with a decently clever solution for it. I also had an issue with sorting certain searches to only return films instead of search directories or possibly other media that had the same name. To fix this I maade a query that would return all items with that name, then I would return the page link of the result that contain the keyword film in its category list.

 ### Known problems/Possible improvements
 #### Problem
 Currently for certain searches where no results are found, the website crashes. I would like to fix this in the future by implemented try/except blocks to return safe data and informs the user that the entery they searched for was either invalid or does not exist.
#### Improvement
One improvement that I would like to make would be to improve the looks of the page. At the moment it is very basic and does not have much personallity but given some time I would love to beautify it and make it unique.

