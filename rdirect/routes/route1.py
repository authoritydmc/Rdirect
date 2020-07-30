from flask import render_template,redirect,url_for,Blueprint,request
from ..utility import utility


bp=Blueprint('route1',__name__)

    
@bp.route('/')
def home():
        return render_template('base.html',location=utility.redirect_data())

@bp.route('/redirect')
def rdirect():
        data="no value"
        data=utility.redirect_data()
        return redirect(data)

@bp.route('/set')
def setdirect():
        host=request.args.get('host','google.com')
        port=request.args.get('port',None)
        key=request.args.get('key',None)

        if key==None:
                return "k3D3RR#"
        elif key!="r3dw0lf":
                return "z3r0CH1NC3"

        print(host,port,key)

        utility.set_redirection(host,port)        

        return "Set Successfully to "+host+":"+str(port) 




