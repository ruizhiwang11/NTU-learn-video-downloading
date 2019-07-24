# NTU-learn-video-downloading


# A dynamic python script to download lecture recorded videos posted on the NTU learn


## Requirements


#### python3

    pip3 install urllib
    pip3 install selenium
    pip3 install progressbar


#### Chrome Webdriver
    Follow the link of tutorial to download google chrome webdriver
    http://chromedriver.chromium.org/downloads
    Copy the driver path into your script


## Usage

1. Go to NTULearn, click one of your courses
2. On the left of the page, select "Recorded Lectures"
3. Copy the URL of this page.
    
    It should be in a format like
    https://ntulearn.ntu.edu.sg/webapps/blackboard/content/listContent.jsp?course_id=_301259_1&content_id=_1632972_1&mode=reset


4. Run the following command in your terminal
    python3 NTU-Learn-video(Please make sure you have copied the driver path into your script before running)
    Follow the steps By the scripts by entering your username,password and the link you just copied
**The progress will be shown. It may take quite a long time.**
    
