from flask import Flask

app = Flask(__name__)



@app.route('/') #ruta 2
def login():
    return """<body bgcolor="white">
    <center> <h1 style="color: red;">Iniciar Sesión</h1>
      <br><form action="/inicio" method="get"> 
      <p>Correo electronico: <input type="text"  size="40"></p>
        <p>Contraseña: <input></p></br>
          <a href="/nosotros"> <button href>Iniciar sesion</button> </a>
            <br>No tienes cuenta? <a href="/Register">Registrate</a><br></center>"""



@app.route('/Register') #ruta 2
def registro():
    return """<body bgcolor="white">
    <center> <h1 style="color: red;">Registrate</h1>
     <br><form action="/" method="get"> 
     <p>Nombre: <input type="text"  size="40"></p>
    <p>Apellido: <input type="text"  size="40"></p>
    <p>Edad: <input type="text"  size="40">
    <p>Correo Electronico: <input type="text"  size="40"> </p>
    <p>Contraseña: <input size="40"></p> 
    <p>Repite la contraseña: <input size="40"></p>
    </br> <a href="/nosotros"><button href>Registrarte</button> </a> </center>"""



@app.route('/inicio')
def hello():
    return '<body bgcolor="pink"> <img src="https://www.clasesnet.com/clases/imagenes/logo.png" alt="logo de nuestra pagina web"> <center> <img src="https://josmorbor.neocities.org/img/boton_inicio.png" style="width: 155px; height: 59px; "><a href="/nosotros"><img src="https://grupodispersa.com.gt/wp-content/uploads/2021/07/boton-nosotros.png" style="width: 155px; height: 59px; "></a> <img src="https://aete.org/wp-content/uploads/2016/07/BotonesServiciosAgua.png" style="width: 155px; height: 55px; "><img src="https://multicon.com.mx/wp-content/uploads/2019/08/boton-contacto.png" style="width: 155px; height: 55px; "></center> <center> <h1 style="color: red;">Hello, world</h1></center><center><img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQZ69MR2WkachtqqExQ1haf1E8kEq9j7agvKMujRDdR5A&s"></center> <center><p>Esto es un texto de prueba si, texto de prueba, texto de prueba, parrafo de prueba parrafo de prueba</p> </center> '





@app.route('/nosotros') #ruta 2
def nosotros():
    return '<body bgcolor="black"> <h1 style="color: red;">Hola, Esto es nosotros</h1>'


@app.route('/home/<name>')
def home(name):
    return f'<h1><center>Esto es la pagina de inicio {name}</center></h1>'

#suma 
@app.route('/suma/<int:num1>,<int:num2>')
@app.route('/suma/<int:num1>,<int:num2>,<int:num3>')
def suma(num1, num2, num3=None):
    if num3 is None:
        resultado = num1 + num2
        return f'<center><h1>{num1} + {num2} = {resultado}</h1></center>'
    else:
        resultado = num1 + num2 + num3
        return f'<center><h1>{num1} + {num2} + {num3} = {resultado}</h1></center>'

@app.route('/resta/<int:num1>,<int:num2>')
@app.route('/resta/<int:num1>,<int:num2>,<int:num3>')
def resta(num1, num2, num3=None):
    if num3 is None:
        resultado = num1 - num2
        return f'<center><h1>{num1} - {num2} = {resultado}</h1></center>'
    else:
        resultado = num1 - num2 - num3
        return f'<center><h1>{num1} - {num2} - {num3} = {resultado}</h1></center>'


if __name__ == '__main__':
    app.run(debug=True)
    app.run(port=6000)

    