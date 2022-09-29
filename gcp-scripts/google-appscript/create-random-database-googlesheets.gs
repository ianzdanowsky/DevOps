function myFunction() {
  var spreadsheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  var sheet = spreadsheet.getDataRange();
  var data_lenght = 999;
  var estados = Array("Bahia","São Paulo", "Distrito Federal", "Santa Catarina");
  var velocidades = Array("Rápida","Normal","Lenta")
  var dispositivos = Array("Computador próprio","Computador da escola","Tablet/Celular próprio","Tablet/Celular da escola")


  
  for (var i = 1; i < data_lenght; i++){
    var estado = estados[Math.floor(Math.random()*estados.length)];
    spreadsheet.getRange(1+i,1).setValue(estado);
    var velocidade = velocidades[Math.floor(Math.random()*velocidades.length)];
    spreadsheet.getRange(1+i,2).setValue(velocidade);
    var dispositivo = dispositivos[Math.floor(Math.random()*dispositivos.length)];
    spreadsheet.getRange(1+i,3).setValue(dispositivo);

  }
}
