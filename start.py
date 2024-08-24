from flask import Flask

def start():

    jug = Flask(__name__)
    jug.config['SERVER_NAME'] = 'paperdrift.com:443'
    # jug.config['SERVER_NAME'] = '127.0.0.1:5000'
      # If not use above, then can't reference subdomains below; will error;

    # jug.debug = True  # Saw this somewhere; not sure about it;


    def printHtml():
        return "<b>paperdrift 5.1</b>"

    def printImg():
        return "<img src=\"static/favicon.ico\" width=20px height=20px>"
        #return "<img src=\"static/train1.png\" width=20px height=20px>"



    #@jug.route("/", subdomain = "www")
    @jug.route("/")
    @jug.route("/", subdomain = "<sub>")
    def homesub(sub='root'):
        html = printImg() + printHtml() + f' /index @{sub}'
        return html

    # @jug.route("/")
    # def home():
    #     html = printHtml()
    #     return html


    #@jug.route("/<arg>")
    #def subpath(arg):
    #    return "<p>yahoo2 " + arg + "</p>"

    #@jug.route('/', defaults={'path1': ''})
    # if you also want to catch root; see URL Route Registrations

    @jug.route('/<path:path1>')
    @jug.route('/<path:path1>', subdomain="<sub>")
    def catch_all(path1, sub='root'):
        #html = "<img src=\"/static/favicon.ico\" width=20 height=20> "
        html = printImg() + printHtml() + f' /{path1} @{sub}'
        # return "The path is : %s" %path1
        return html

    return jug




# if __name__ == '__main__':
#     jug = start()
  # This doesn't seem to work... not sure if I forgot something or doing something wrong;


jug = start()
  # This seems to be optional, actually; can work without it;
  # If without above, then do:
  # $ flask -A start:start run --debug
    # first 'start' refers to the script; 2nd 'start' the class;
  # If have above, then can do start:start or :
  # $ flask -A start:jug run --debug

jug.run() # Saw this; not sure; Works with or without;



