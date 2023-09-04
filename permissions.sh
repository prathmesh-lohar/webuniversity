
sudo ufw app info "Apache Full"

sudo ufw allow in "Apache Full"

sudo chown :www-data webuniversity
sudo chown :www-data webuniversity/db.sqlite3
sudo chown :www-data webuniversity/static/

sudo chown :www-data webuniversity/static/admin/
sudo chown :www-data webuniversity/media/
sudo chown :www-data webuniversity/media/blog/
sudo chown :www-data webuniversity/media/blog/thumb/
sudo chown :www-data webuniversity/media/courses/
sudo chown :www-data webuniversity/media/courses/thumb/
sudo chown :www-data webuniversity/media/staf/
sudo chown :www-data webuniversity/media/staf/profile_picture/
sudo chown :www-data webuniversity/media/tutorials/
sudo chown :www-data webuniversity/media/tutorials/download-dat



sudo chmod -R 775 webuniversity

sudo chmod -R 775 webuniversity/db.sqlite3
sudo chmod -R 775 webuniversity/static/

sudo chmod -R 775 webuniversity/static/admin/
sudo chmod -R 775 webuniversity/media/
sudo chmod -R 775 webuniversity/media/blog/
sudo chmod -R 775 webuniversity/media/courses/
sudo chmod -R 775 webuniversity/media/blog/thumb/
sudo chmod -R 775 webuniversity/media/courses/thumb/
sudo chmod -R 775 webuniversity/media/staf/

 sudo chmod -R 775 webuniversity/media/staf/profile_picture/
 sudo chmod -R 775 webuniversity/media/tutorials/
 sudo chmod -R 775 webuniversity/media/tutorials/download-dat


 sudo systemctl restart apache2