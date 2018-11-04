sudo apt update
echo "DONT RUN AS SUDO (please)"
#required crap
sudo apt install libssl-dev  -y
sudo apt install python3 python3-pip libffi-dev -y
sudo apt install -y libsqlite3-dev

if [ $1 == "audio" ]; then
	sudo apt install libopus0 ffmpeg
	sudo python3 -m pip install -U discord.py[voice] 
fi
sudo apt install python-mysqldb mysql-server python-mysql.connector
sudo python3 -m pip install -U discord.py
sudo pip3 install mysql-connector-python-rf
#extra features: 
sudo pip3 install tinytag

#configure mysql
clear
echo "configuring MYSQL under $USER (ctrl C if already done)"
sleep 2
sudo mysql_secure_installation
#echo "making database and user... (ctrl c if already done)" 
#sleep 2
#printf "creating user SenvrBot2@localhost identified by (this is a password): "
#read identity -s

#done
echo "Done."


