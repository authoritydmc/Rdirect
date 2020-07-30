def redirect_data():   
     with open('.config','r') as f:
                data=f.read()
                print(data)
                return data


def set_redirection(host,port):
    with open('.config','w') as f:
                f.write(host)
                if port !=None:
                        f.write(":"+port)