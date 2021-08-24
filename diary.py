from flask import render_template, request, redirect, url_for, flash
from sqlalchemy import and_, not_
from models import User, DiaryLog, Friendship
from globalSettings import *


@app.route('/login', methods=['POST', 'GET'])
def login():
    if(request.method == 'POST'):
        username = request.form['username']
        password = request.form['password']

        if(username == '' and password == ''):
            flash('Please enter required fields!')

            return render_template('login.html')
 
        DBUser = session.query(User).\
            filter_by(username=username).first()     

        if(DBUser != None):
            if(username == DBUser.username and password == DBUser.password):
                global LOGIN 
                global USER 
                LOGIN = True                
                USER = DBUser
                
                return redirect(url_for('index'))
            else:
                flash('Wrong login credentials')

                return render_template('login.html')
        else:   
            flash('Wrong login credentials')

            return render_template('login.html')
    else:
        return render_template('login.html')

@app.route('/logOut')
def logOut():
    global LOGIN 
    global USER
    LOGIN = False
    USER = None

    return redirect(url_for('login'))

@app.route('/registerPage', methods=['POST'])
def redirectRegister():
    return  render_template('register.html')

@app.route('/register', methods=['POST'])
def register():
    if(request.method == 'POST'):
        username = request.form['username']
        password = request.form['password']
        age = request.form['age']
        sex = request.form['sex']
        country = request.form['country']
        city = request.form['city']        

        if(username == '' or password == ''):
            flash('Please enter required fields')

            return render_template('register.html')

        user = User(username, password, age, sex, country, city)

        session.add(user)
        session.commit()

        flash('You have successfully been registered!')

        return render_template('login.html')

@app.route('/')
@app.route('/index')
def index():
    friendLogs = []
    addresses = []

    if(LOGIN==False):        
        return redirect(url_for('login'))
    else:   
        userFriends = session.query(Friendship, DiaryLog, User).\
            join(DiaryLog, DiaryLog.user_id==User.id).\
            filter(and_(Friendship.status==1,\
            Friendship.requester_id==USER.id,\
            DiaryLog.user_id==Friendship.addresse_id,\
            DiaryLog.user_id!=USER.id),\
            DiaryLog.visible==1).all()
        
    for log in userFriends:
        friendLogs.append(session.query(User).\
            filter_by(id=log[0].addresse_id).first())
        
    for friend in userFriends:
        addresses.append(friend[0].addresse_id)
    
    return render_template('index.html',\
        message=f'Welcome { USER.username }',\
        friends=userFriends,\
        user=USER.username)

@app.route('/profile')
def profile():
    logedUser = session.query(User).\
        filter_by(username=USER.username).first()  
    
    return render_template('profile.html', user=logedUser)


@app.route('/updateUser', methods=['POST'])
def updateUser():      
    username = request.form['username']
    password = request.form['password']
    age = request.form['age']
    sex = request.form['sex']
    country = request.form['country']
    city = request.form['city']

    session.query(User).filter(User.id == USER.id).\
        update({"username": username,\
        "password": password,\
        "age": age,\
        "sex": sex,\
        "country": country,\
        "city": city},\
        synchronize_session="fetch")
    session.commit()

    flash('User updated!')

    return redirect(url_for('profile'))


@app.route('/updateDiaryLogPage', methods=['POST'])
def updateDiaryLogPage():
    id = request.form['id']
   
    currentDiaryLog = session.query(DiaryLog).\
        filter_by(id=id).first()

    return render_template('updateDiaryLog.html',\
        currentDiaryLog=currentDiaryLog,\
        user=USER.username)

@app.route('/updateDiaryLog', methods=['POST'])
def updateDiaryLog():
    if(request.method == 'POST'):
        id = request.form['id']
        name = request.form['name']
        date = request.form['date']
        log = request.form['log']
        visible = request.form['visible']

        if(name == '' or date == '' or log == ''):
            flash('Please enter required fields')

            return render_template('updateDiaryLog.html')
        else:
            session.query(DiaryLog).\
                filter(DiaryLog.id == id).\
                update({"name": name,\
                "date": date,\
                "log": log,\
                "visible": visible},\
                synchronize_session="fetch")
                
            session.commit()

            flash('Diary log updated!')

            return redirect(url_for('logs'))


@app.route('/logs')
def logs():        
    global USER
    userLogs = session.query(DiaryLog).\
        filter_by(user_id=USER.id).all()

    return render_template('logs.html',\
        userLogs=userLogs,\
        user=USER.username)

@app.route('/newDiaryLogPage')
def newDiaryLogPage():
    return render_template('newDiaryLog.html', user=USER.username)

@app.route('/newDiaryLog', methods=['POST'])
def newDiaryLog():
    global USER
    if(request.method == 'POST'):
        name = request.form['name']
        date = request.form['date']
        log = request.form['log']
        visible = request.form['visible']

        if(name == '' or date == '' or log == ''):
            flash('Please enter required fields')

            return render_template('newDiaryLog.html')
        
        if(len(log) > 300):
            flash('The diary log can have maximum 300 characters!')

            return render_template('newDiaryLog.html')

        diaryLog = DiaryLog(name, date, log, visible, USER.id)

        session.add(diaryLog)
        session.commit()

        flash('You have successfully created new log!')

        return render_template('logs.html')

@app.route('/friends')
def friends():
    global USER
    friendLogs = []
    addresses = []
    notFriends = []
    friends = []
    pendingFriends = []
    
    userFriends = session.query(Friendship, User).\
        join(User, User.id==Friendship.requester_id).\
        filter(and_(Friendship.status==1),\
        Friendship.requester_id==USER.id)

    userFriendsPending =  session.query(Friendship, User).\
        join(User, User.id==Friendship.requester_id).\
        filter(and_(Friendship.status==0,\
        Friendship.addresse_id==USER.id)).all()

    dbNotFriends = session.query(User).\
        filter(not_(User.id==USER.id)).all()        
        
    for log in userFriends:
        friendLogs.append(session.query(User).\
            filter_by(id=log[0].addresse_id).first())
        
    for friend in userFriends:
        addresses.append(friend[0].addresse_id)

    for friend in addresses:
        f = session.query(User).\
            filter_by(id=friend).first()

        friends.append(f) if f not in friends else friends

    for pendingFriend in userFriendsPending:
        pendingFriends.append(pendingFriend[1])

    for user in dbNotFriends:
        if user not in friends and user not in pendingFriends: notFriends.append(user)

    return render_template('friends.html',\
        friends=friends,\
        notFriends=notFriends,\
        pendingFriends=pendingFriends,\
        user=USER.username)
    

@app.route('/unfriend', methods=['POST'])
def unfriend():
    if(request.method == 'POST'):
        id = request.form['id']

        session.query(Friendship).\
            filter(and_(Friendship.requester_id==USER.id, Friendship.addresse_id==id)).\
            delete(synchronize_session="fetch")
        
        session.query(Friendship).\
            filter(and_(Friendship.requester_id==id, Friendship.addresse_id==USER.id)).\
            delete(synchronize_session="fetch")

        session.commit()

        return redirect(url_for('friends'))

@app.route('/addFriend', methods=['POST'])
def addFriend():
    if(request.method == 'POST'):
        id = request.form['id']

        friendship = Friendship(USER.id, id, 0)

        session.add(friendship)
        session.commit()

        return redirect(url_for('friends'))

@app.route('/confirmFriend', methods=['POST'])
def confirmFriend():
    if(request.method == 'POST'):
        id = request.form['id']

        friendship = Friendship(USER.id, id, 1)

        session.add(friendship)

        session.query(Friendship).\
            filter(Friendship.requester_id == id).\
            update({"requester_id": id,\
            "addresse_id": USER.id,\
            "status": 1},\
            synchronize_session="fetch")

        session.commit()
   
        return redirect(url_for('friends'))

if __name__ == '__main__':
    app.run()