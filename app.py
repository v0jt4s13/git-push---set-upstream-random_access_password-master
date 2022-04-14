from flask import Flask, render_template
from flask import request

from secret import get_pass, get_datetimenow

app = Flask(__name__)

def check_password(pass_str,pstr):
	if pass_str != "":
		pass_gen = get_pass(pstr)
		if pass_gen == pass_str:
			return "OK"
		else:
			return "Podane hasło jest błędne"
	else:
		return "Nie podano hasła"

# Main

@app.route('/', methods = ['POST','GET'])
def index():
  
	return_resp = ""
	datetimenow = get_datetimenow()
	print('abbb',return_resp)
	if request.method == 'POST':
		pass_str = request.form['pass']
		user_str = request.form['user_name']

		if check_password(pass_str,user_str) == 'OK':
			return_resp = "Gratulacje, hasło poprawne."
			print('abbb2',return_resp)
		else:
			return_resp = 'fail'
			print('abbb3',return_resp)

	return render_template("index.html", return_resp=return_resp, datetimenow=datetimenow)


if __name__ == "__main__":
	app.run()
