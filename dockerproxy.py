from flask import Flask, request, send_file
import os
app = Flask(__name__)

@app.route('/')
def myimage():
    myimage = request.args.get('myimage', type = str)
    print 'myimage is: ' + myimage
    print 'Pulling ' + myimage + ' ...'
    os.system('docker pull ' + myimage)
    print 'Pulling ' + myimage + ': [OK]'
    print 'Saving ' + myimage + ' ...'
    myimage2 = myimage.replace("/", "~")
    os.system('docker save ' + myimage + ' > /tmp/' + myimage2 + '.tar')
    print 'Saving ' + myimage + ': [OK]'
    print 'Serving file...'
    return send_file('/tmp/' + myimage2 +'.tar', mimetype='application/octet-stream', as_attachment=True, attachment_filename=myimage2 +'.tar')
