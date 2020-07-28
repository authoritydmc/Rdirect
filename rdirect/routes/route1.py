from flask import render_template,redirect,url_for,Blueprint,request



bp=Blueprint('route1',__name__)

    
# @bp.route('/')
# def home():
#         return render_template('base.html')
@bp.route('/')
@bp.route('/redirect')
def rdirect():
        data="no value"
        with open('.config','r') as f:
                data=f.read()
                print(data)
        
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

        with open('.config','w') as f:
                f.write(host)
                if port !=None:
                        f.write(":"+port)
                

        return "Set Successfully to "+host+":"+str(port) 




