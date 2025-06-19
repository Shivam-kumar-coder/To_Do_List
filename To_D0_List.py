import streamlit as st
import sqlite3 as sq
conn=sq.connect("register.db")
cur=conn.cursor()
cur.execute("create table if not  exists dose( date date, work text,time time ) ")
st.title(" To Do App ")
st.success(" Create TO DO LIST")
with st.form(" to do list create"):
    a=st.text_input("what is to do is today")
    #b=st.text_input("enter ypur id")
    c=st.date_input("emter the date on do")
    d=st.time_input("enter tmie this work")
    s=str(d)
    value=(c,a,s)
    query="insert into dose (date,work,time) values(?,?,?)" 
    button=st.form_submit_button("do submit")
    #display=st.form_submit_button(" view to do ?")
if button:
    #cur.execute('start transaction')
    cur.execute(query,value)
    #conn.commit()
    cur.execute("commit")
    st.success("succesfully create what do ")
    #cur.execute("select * from dose")
    #for i in cur:
        #st.write(cur)

st.success("view What  to do ? enter the date")

f=st.date_input(" select to do date ")
display=st.button(" view to do ?")
#n=str(f)
if display:
    q="select work,time from dose where date=?"
    g=cur.execute(q,(f,))
    if cur is not None:
        for i in cur:
            if i is not None:
                st.write(cur)
            else:
                st.info("not to do list in date")
    else:

        st.write("not to do list in date")


    
    