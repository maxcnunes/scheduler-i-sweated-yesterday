scheduler-i-sweated-yesterday
=============================

This application is hosted on Google App Engine and just used to run schedules for this another application [i-sweated-yesterday](https://github.com/maxcnunes/i-sweated-yesterday).

To work well is necessary change to valid values for these variables: `user = 'secrete_user'` and `password = 'secrete_password'`

Common Commands
===============


- **Run locally project on the GAE:** `/opt/google/appengine/dev_appserver.py .`
-  **Update project on the GAE:** `/opt/google/appengine/appcfg.py update .`
-  **Update just the cron on the GAE:** `/opt/google/appengine/appcfg.py update_cron .`
-  **Install GAE SDK on the Linux:** `bash config-environment/install_google_app_engine_sdk.sh`
-  **Install packages dependencies:** `bash config-environment/install_packages_dependencies.sh`