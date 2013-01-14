
#go to your downloads directory
cd ~/Downloads/

# download last version of google app engine sdk
# verify the last version here: https://developers.google.com/appengine/downloads
wget http://googleappengine.googlecode.com/files/google_appengine_1.7.4.zip

#you might need to change the version of App Engine Python SDK
unzip google_appengine_1.7.4.zip

#lets move unziped files to /opt
sudo mv google_appengine /opt/google/appengine