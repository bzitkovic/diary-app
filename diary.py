from flask import render_template, request, redirect, url_for, flash
from sqlalchemy import and_, not_
from models import User, DiaryLog, Friendship
from globalSettings import *
from forms import *


@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()

    if(request.method == 'POST' and form.validate_on_submit()):
        DBUser = session.query(User).\
            filter(User.username==form.username.data).first()    

        if(DBUser != None):
            if(form.username.data == DBUser.username and form.password.data == DBUser.password):
                global LOGIN 
                global USER 
                LOGIN = True                
                USER = DBUser 

                return redirect(url_for('index'))
            else:
                flash('Wrong login credentials')
                
                return render_template('login.html', form=form)
        else:   
            flash('Wrong login credentials')

            return render_template('login.html', form=form)

    return render_template('login.html', form=form)

@app.route('/logOut')
def logOut():
    global LOGIN 
    global USER
    LOGIN = False
    USER = None

    session.close()

    return redirect(url_for('login'))

@app.route('/register', methods=['POST', 'GET'])
def register():
    form = RegisterForm()

    if(request.method == 'POST' and form.validate_on_submit()):
        user = User(form.username.data,\
            form.password.data,\
            form.age.data,\
            form.sex.data,\
            form.country.data,\
            form.city.data)
        session.add(user)
        session.commit()

        flash('You have successfully been registered!')

        return redirect(url_for('login'))

    if(form.errors != {}): 
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg[0]}')

    return render_template('register.html', form=form)

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

@app.route('/profile', methods=['POST', 'GET'])
def profile():
    loggedUser = session.query(User).\
        filter(User.username==USER.username).first()  

    form = ProfileForm(obj=loggedUser)

    if(request.method == 'POST' and form.validate_on_submit()):
        session.query(User).filter(User.id==USER.id).\
        update({"username": form.username.data,\
        "password": form.password.data,\
        "age": form.age.data,\
        "sex": form.sex.data,\
        "country": form.country.data,\
        "city": form.city.data},\
        synchronize_session="fetch")
        session.commit()

        flash('User updated!')

        return redirect(url_for('profile'))

    if(form.errors != {}): 
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg[0]}')

    return render_template('profile.html', user=loggedUser, form=form)


@app.route('/updateDiaryLogPage/<id>', methods=['POST', 'GET'])
def updateDiaryLogPage(id):
    currentDiaryLog = session.query(DiaryLog).\
        filter(DiaryLog.id==id).first()

    form = DiaryLogForm(obj=currentDiaryLog)

    if(request.method == 'POST' and form.validate_on_submit()):
        session.query(DiaryLog).\
                filter(DiaryLog.id == id).\
                update({"name": form.name.data,\
                "date": form.date.data,\
                "log": form.log.data,\
                "visible": form.visible.data},\
                synchronize_session="fetch")                
        session.commit()

        flash('Diary log updated!')

        return redirect(url_for('logs'))

    if(form.errors != {}): 
        for err_msg in form.errors.values():
            flash(f'There was an error with diary log update: {err_msg[0]}')

    return render_template('updateDiaryLog.html',\
        currentDiaryLog=currentDiaryLog,\
        user=USER.username,\
        form=form)

@app.route('/logs')
def logs():        
    global USER
    userLogs = session.query(DiaryLog).\
        filter_by(user_id=USER.id).all()

    return render_template('logs.html',\
        userLogs=userLogs,\
        user=USER.username)

@app.route('/newDiaryLogPage', methods=['POST', 'GET'])
def newDiaryLogPage():
    form = DiaryLogForm()

    if(request.method == 'POST' and form.validate_on_submit()):
        diaryLog = DiaryLog(form.name.data, form.date.data, form.log.data, form.visible.data, USER.id)

        session.add(diaryLog)
        session.commit()

        flash('You have successfully created new log!')

        return redirect(url_for('logs'))

    if(form.errors != {}): 
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a diary log: {err_msg[0]}')


    return render_template('newDiaryLog.html', user=USER.username, form=form)

@app.route('/deleteDiaryLog/<id>')
def deleteDiaryLog(id):
    session.query(DiaryLog).\
        filter(DiaryLog.id==id).\
        delete(synchronize_session="fetch")
    session.commit()

    flash('You have successfully deleted diary log!')

    return redirect(url_for('logs'))


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
    csrf.init_app(app)