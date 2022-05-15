# from flask import Flask, render_template, request, redirect

# app=Flask(__name__,template_folder='template')

# @app.route("/")
# def home():
#     return render_template('compression.html')


# @app.route('/home')
# def upload():
#    return render_template('compression.html')
	
# @app.route('/upload', methods = ['GET', 'POST'])
# def upload_file():
#    if request.method == 'POST':
#       f = request.files['file']
#       f.save(f.filename)
#       return 'file uploaded successfully'

# @app.route("/upload-image", methods=["GET", "POST"])
# def upload_image():

#     if request.method == "POST":

#         if request.files:

#             image = request.files["image"]

#             print(image)

#             return redirect(request.url)


#     return render_template("compression.html")
		


from flask import Flask, render_template, request
from photocompression import compress
app = Flask(__name__)

@app.route("/")
def hello_world(name=None):
    return render_template('compression.html', name=name)

@app.route('/upload', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(f.filename)
      compress(f.filename)
      return 'file uploaded successfully'

if __name__ == '__main__':
       app.run(debug = True)
