
sudo ufw app info "Apache Full"

sudo ufw allow in "Apache Full"

sudo chown :www-data web_university
sudo chown :www-data web_university/db.sqlite3
sudo chown :www-data web_university/static/

sudo chown :www-data web_university/static/admin/
sudo chown :www-data web_university/media/
sudo chown :www-data web_university/media/blog/
sudo chown :www-data web_university/media/blog/thumb/
sudo chown :www-data web_university/media/courses/
sudo chown :www-data web_university/media/courses/thumb/
sudo chown :www-data web_university/media/staf/
sudo chown :www-data web_university/media/staf/profile_picture/
sudo chown :www-data web_university/media/tutorials/
sudo chown :www-data web_university/media/tutorials/download-dat



sudo chmod -R 775 web_university

sudo chmod -R 775 web_university/db.sqlite3
sudo chmod -R 775 web_university/static/

sudo chmod -R 775 web_university/static/admin/
sudo chmod -R 775 web_university/media/
sudo chmod -R 775 web_university/media/blog/
sudo chmod -R 775 web_university/media/courses/
sudo chmod -R 775 web_university/media/blog/thumb/
sudo chmod -R 775 web_university/media/courses/thumb/
sudo chmod -R 775 web_university/media/staf/

 sudo chmod -R 775 web_university/media/staf/profile_picture/
 sudo chmod -R 775 web_university/media/tutorials/
 sudo chmod -R 775 web_university/media/tutorials/download-dat


 sudo systemctl restart apache2