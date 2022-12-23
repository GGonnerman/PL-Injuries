base_path="/home/twoonesecond/Projects/Git/pl-football-injuries/"

#"${base_path}/venv/bin/python" "${base_path}/main.py"
/usr/bin/npm run build --prefix "${base_path}/webpage/"
rsync --recursive --inplace --delete --verbose --progress "${base_path}/webpage/dist/" ubuntu:/var/www/pl
ssh ubuntu 'chmod -R +rx /var/www/pl/css ; chmod -R +rx /var/www/pl/js'
