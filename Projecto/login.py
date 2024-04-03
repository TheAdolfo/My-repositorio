from flask import Flask

app = Flask(__name__)

@app.route('/Login')
def hello():
    return '<body bgcolor="pink"> <img src="https://www.clasesnet.com/clases/imagenes/logo.png" alt="logo de nuestra pagina web"> <center> <img src="https://josmorbor.neocities.org/img/boton_inicio.png" style="width: 155px; height: 59px; "><a href="/nosotros"><img src="https://grupodispersa.com.gt/wp-content/uploads/2021/07/boton-nosotros.png" style="width: 155px; height: 59px; "></a> <img src="https://aete.org/wp-content/uploads/2016/07/BotonesServiciosAgua.png" style="width: 155px; height: 55px; "><img src="https://multicon.com.mx/wp-content/uploads/2019/08/boton-contacto.png" style="width: 155px; height: 55px; "></center> <center> <h1 style="color: red;">Hello, world</h1></center><center><img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQZ69MR2WkachtqqExQ1haf1E8kEq9j7agvKMujRDdR5A&s"></center> <center><p>Esto es un texto de prueba si, texto de prueba, texto de prueba, parrafo de prueba parrafo de prueba</p> </center> '




if __name__ == '__main__':
    app.run(debug=True)
