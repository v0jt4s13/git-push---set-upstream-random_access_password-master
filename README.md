Secure random generated password. Don't needed db or users accounts. Easy to remember password generated from predetermined rules like key and salt.

ie.
every day new password 13 chars password:
rules:
1. From login form - first 4 characters user name
2. Today date (Nr and Weekday - three characters)
3. %^&

pass = 'Bi'+'%'+now.strftime('%d')+'^'+now.strftime('%a')+'&'+'hN' ==> Ea%13^Fri&sY


export FLASK_APP=app.py

python app.py