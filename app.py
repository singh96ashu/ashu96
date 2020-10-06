#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask,render_template,request
app=Flask(__name__)
@app.route("/")
def xyz():
    return render_template("ashu.html")
@app.route("/inputdata",methods=['GET','POST'])
def hhh():
    if(request.method=='POST'):
        num1=int(request.form['n1'])
        num2=int(request.form['n2'])
        total=num1+num2
        return render_template("ashu.html",final=total)
if __name__=="__main__":
    app.run()


# In[ ]:




