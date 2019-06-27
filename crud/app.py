from flask import Flask, render_template, request, url_for, redirect, jsonify
from crud.model import db, app, Pessoa


from flask_sqlalchemy import SQLAlchemy

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/")
@app.route("/cadastrar")
def cadastrar():
    return render_template("cadastro.html")

def voltar():
    return render_template("home")


@app.route("/cadastro", methods=['GET', 'POST'])
def cadastro():
    if request.method == "POST":
        nome = (request.form.get("nome"))
        rua = (request.form.get("rua"))
        numero = (request.form.get("numero"))
        bairro = (request.form.get("bairro"))
        cidade = (request.form.get("cidade"))
        estado = (request.form.get("estado"))
        fone = (request.form.get("fone"))
        cpf = (request.form.get("cpf"))
        email = (request.form.get("email"))

        if nome and rua and numero and bairro and cidade and estado and fone and cpf and email:
            p = Pessoa(nome, rua, numero, bairro, cidade, estado, fone, cpf, email)
            db.session.add(p)
            db.session.commit()

    return redirect(url_for("home"))

@app.route("/cadastro/cliente", methods=['GET', 'POST'])
def cadastro_cliente():
    if request.method == "POST":
        nome = (request.form.get("nome"))
        rua = (request.form.get("rua"))
        numero = (request.form.get("numero"))
        bairro = (request.form.get("bairro"))
        cidade = (request.form.get("cidade"))
        estado = (request.form.get("estado"))
        fone = (request.form.get("fone"))
        cpf = (request.form.get("cpf"))
        email = (request.form.get("email"))

        if nome and rua and numero and bairro and cidade and estado and fone and cpf and email:
            p = Pessoa(nome, rua, numero, bairro, cidade, estado, fone, cpf, email)
            db.session.add(p)
            db.session.commit()
        return jsonify(name=nome, rua=rua, numero=numero, bairro=bairro, cidade=cidade, estado=estado, fone=fone, cpf=cpf,
                       email=email)


@app.route("/lista")
def lista():
    pessoas = Pessoa.query.all()
    return render_template("lista.html", pessoas=pessoas)

@app.route("/lista/cliente", methods=['GET'])
def lista_cliente():
    pessoas = Pessoa.query.all()
    json = []

    for pessoa in pessoas:
        json.append({'name': pessoa.nome, 'rua': pessoa.rua, 'numero': pessoa.numero, 'bairro': pessoa.bairro,
                     'cidade': pessoa.cidade, 'estado': pessoa.estado, 'fone': pessoa.fone,
                     'email': pessoa.email})
    return jsonify(values=json)


@app.route("/atualizar/<int:id>", methods=['GET', 'POST'])
def atualizar(id):
    pessoa = Pessoa.query.filter_by(_id=id).first()
    if request.method == "POST":
        nome = (request.form.get("nome"))
        rua = (request.form.get("rua"))
        numero = (request.form.get("numero"))
        bairro = (request.form.get("bairro"))
        cidade = (request.form.get("cidade"))
        estado = (request.form.get("estado"))
        fone = (request.form.get("fone"))
        email = (request.form.get("email"))

        if nome and rua and numero and bairro and cidade and estado and fone and email:
            pessoa.nome = nome
            pessoa.rua = rua
            pessoa.numero = numero
            pessoa.bairro = bairro
            pessoa.cidade = cidade
            pessoa.estado = estado
            pessoa.fone = fone
            pessoa.email = email
            db.session.commit()

    return render_template("atualizar.html", pessoa=pessoa)

@app.route("/atualizar/cadastro/<int:id>", methods=['GET', 'POST'])
def atualizar_api(id):
    pessoa = Pessoa.query.filter_by(_id=id).first()
    if request.method == "POST":
        nome = (request.form.get("nome"))
        rua = (request.form.get("rua"))
        numero = (request.form.get("numero"))
        bairro = (request.form.get("bairro"))
        cidade = (request.form.get("cidade"))
        estado = (request.form.get("estado"))
        fone = (request.form.get("fone"))
        email = (request.form.get("email"))

        if nome and rua and numero and bairro and cidade and estado and fone and email:
            pessoa.nome = nome
            pessoa.rua = rua
            pessoa.numero = numero
            pessoa.bairro = bairro
            pessoa.cidade = cidade
            pessoa.estado = estado
            pessoa.fone = fone
            pessoa.email = email
            db.session.commit()
        return jsonify(name=nome, rua=rua, numero=numero, bairro=bairro, cidade=cidade, estado=estado, fone=fone,
                       email=email)


@app.route("/excluir/<int:id>", methods=['GET', 'POST'])
def excluir(id):
    pessoa = Pessoa.query.filter_by(_id=id).first()
    db.session.delete(pessoa)
    db.session.commit()
    pessoas = Pessoa.query.all()
    return render_template("lista.html", pessoas=pessoas)

@app.route("/excluir/cliente/<int:id>", methods=['GET'])
def excluir_cliente(id):
    if request.method == "GET":
        pessoa = Pessoa.query.filter_by(_id=id).first()
        db.session.delete(pessoa)
        db.session.commit()
        pessoas = Pessoa.query.all()

        json = []

        for pessoa in pessoas:
            json.append({'name':pessoa.nome, 'rua':pessoa.rua, 'numero':pessoa.numero, 'bairro':pessoa.bairro, 'cidade':pessoa.cidade, 'estado':pessoa.estado, 'fone':pessoa.fone,
                       'email':pessoa.email})
        return jsonify(values=json)


if __name__ == "__main__":
    app.run(debug=True)