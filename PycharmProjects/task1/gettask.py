from flask import Flask,request,jsonify

app = Flask(__name__)

#passing the data through a browser in a unsecure mode--->get
@app.route("/testfun")
def test():
    get_name = request.args.get("get_name")
    mobile_number= request.args.get("mobile")
    email_id=request.args.get('email_id')
    return "this is my first function for get {} {} {} ".format(get_name,mobile_number,email_id)


if __name__ =='__main__':
    app.run(port=5002)