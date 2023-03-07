# Security-Sistem
Security sistem made in raspberry pi 4 and python. This project is based in movement detection. When the movement is detected jump a photo and send it to mail. 
Then a record will be save on MongoDB Atlas. The record have the fields: "email"(the user mail encrypted with sha256), "hour"(the hour that the photo was made), "day"(the day that the photo was made), "image" and "location", where on location we can found: "latitude" and "longitude"(where is located the raspberry), "ountry" and "city".
