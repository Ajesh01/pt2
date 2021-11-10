from flask import Flask, render_template, request
from pymongo import MongoClient
import pymongo
import os



from dotenv import load_dotenv
from werkzeug.utils import redirect



load_dotenv()


def get_mongo_uri():
    
    mongo_uri = os.environ['MONGO_URI']
    # print(mongo_uri)

    return mongo_uri

MONGO_URI = get_mongo_uri()

# creating a MongoClient object  
client = MongoClient(MONGO_URI)  

# accessing the database  
DB_NAME = 'pt2'
database = client[DB_NAME]

coll_1 = database["articles"] 


app = Flask(__name__)



def get_last_article_id():
    article_id =coll_1.find().sort([('article_id', -1)]).limit(1)

    try:
        article_id = article_id[0]['article_id']
    except Exception as err:
        
        article_id = 0

    return article_id


@app.route('/') 
def home():

    llist = []
    cursor = coll_1.find()
    for article in cursor:
        llist.append(article)


    return render_template('index.html', articles = llist)



@app.route('/add') 
def add_article():



    return render_template('new_article.html')



@app.route('/article/add', methods=['POST'])
def add_article_post():
    editor_content = request.form['editor_content']
    coll_1.insert_one({
        "article_id" : get_last_article_id() + 1,
        "content" : str(editor_content)
        })
    # print(editor_content)
    return redirect("/")
    # return render_template('new_article.html')

@app.route('/delete-article/<article_id>') 
def delete_article(article_id):

    coll_1.delete_one({
        "article_id" : int(article_id)
        })




    return redirect("/")





if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True,port=80)