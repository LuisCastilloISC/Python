from flask import Blueprint, request,jsonify
from sqlalchemy import exc
from models import User
from app import db,bcrypt
from auth import tokenCheck

appuser = Blueprint('appsuer',__name__,template_folder="templates")


@appuser.route('/auth/registro', methods =['POST'])
def registro():
    user  = request.get_json()
    userExists = User.query.filter_by(email=user['email']).first()
    if not userExists:
        usuario = User(email=user["email"],password=user["password"])
        try:
            db.session.add(usuario)
            db.session.commit()
            mensaje="Usuario creado"
        except exc.SQLAlchemyError as e:
            mensaje = "Error"
    else:
        mensaje="Usuario existente"     
    return jsonify({"message":mensaje})

@appuser.route('/auth/login' , methods =['POST'])
def login():
    user  = request.get_json()
    usuario = User(email=user["email"],password=user["password"])
    searchUser = User.query.filter_by(email = usuario.email).first()
    if searchUser:
        validation = bcrypt.check_password_hash(searchUser.password,user["password"])
        if validation:
            auth_token = usuario.encode_auth_token(user_id=searchUser.id)
            responseObject = {
                    'status': 'success',
                    'message': 'Loggin exitoso',
                    'auth_token': auth_token
                }
            return jsonify(responseObject)
    return jsonify({"message":"Datos incorrectos"})

@appuser.route('/usuarios', methods=['GET'])
@tokenCheck
def getUsers(usuario):
    print(usuario)
    print(usuario['admin'])
    if usuario['admin']:
        output = []
        usuarios = User.query.all()
        for usuario in usuarios:
            usuarioData = {}
            usuarioData['id'] = usuario.id
            usuarioData['email'] = usuario.email
            usuarioData['password'] = usuario.password
            usuarioData['registered_on'] = usuario.registered_on
            usuarioData['admin'] = usuario.admin
            output.append(usuarioData)
        return jsonify({'usuarios':output})
