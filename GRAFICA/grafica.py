import pandas as pd
import webbrowser



#PARA EL PRIMER CSV------------------------------------------------------------------------------------------------------------------------------
datos = pd.read_csv("datos.csv")
df = pd.DataFrame(datos)
script = ""
i=0
while i<12:
        script = script+"{x:'"+datos['Municipio'].loc[i]+"', y:"+str(datos['IMC'].loc[i])+", z:"+str(i+1)+"},\n"
        i+=1
print (script)


f = open('Datos_obesidad.html','w')

mensaje = """<html>
<head>
<title>GRAFICA INDIVIUDAL</title>
<meta charset='utf-8'>
<link rel='stylesheet' href='https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css' integrity='sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T' crossorigin='anonymous'>
<link rel='stylesheet' type='text/css' href='morris.css'>	
<script src='http://ajax.googleapis.com/ajax/libs/jquery/1.9.0/jquery.min.js'></script>
<script src='http://cdnjs.cloudflare.com/ajax/libs/raphael/2.1.0/raphael-min.js'></script>
<script src='https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js' integrity='sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM' crossorigin='anonymous'></script>	
<script src='Morris.js'></script>
<script>    
function grafica1(){
  new Morris.Line({
  element: 'graph',
  data: ["""+script+"""
          ],
  xkey: 'x',
      parseTime: false,
      ykeys: ['y'],
    labels: ['IMC'],
    lineColors:['black']
    });
  
      document.getElementById('div1').style.display='';
    document.getElementById('boton1').style.display='none';
}
</script>
</head>
<body>
<h1>Graficas sobre IMC y Obesidad en la Ciudad de Mexico</h1>
<br>
<br>
<br>
<h2>Presiona para mostrar la grafica</h2>
<br>
<br>
<br>
<h3 texto1></h3>
<div id='graph'>
  <div id="div1" style="display:none">
  <br>
  <br>
    <p><h2>Esta grafica muestra el promedio del Imc de las diferentes alcaldias de la Ciudad de Mexico en el año de 2018</h2></p>
  </div>
</div>

<div id='botones'>
<input type='button' style="display:'';" id='boton1' value='grafica 1'  class="rainbow-button"  onclick='grafica1()'>

</div>
</body>
</html>"""
f.write(mensaje)
f.close()

webbrowser.open_new_tab('Datos_obesidad.html')