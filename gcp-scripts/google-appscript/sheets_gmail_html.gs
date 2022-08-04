function enviarDica() {

  var ss = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  var data = ss.getDataRange().getValues();
  var user = Session.getActiveUser().getEmail();
  var html = HtmlService.createTemplateFromFile('email2');


  for(var i=1;i<data.length;i++){
    var row = data[i]
    var status = row[4].toString()
    if(!status.includes("Enviado")){

      var userEmail = row[0];
      var emailMsg = row[2];
      var idDica = row[3];


      var file = DriveApp.getFileById(idDica);
      var fileLink = file.getUrl();

      // Substitui as variáveis do template de e-mail
      html.msg = emailMsg;
      html.link = fileLink;

      var htmlMessage = html.evaluate().getContent();
      var senderName = "GetEdu";
      var replyEmail = "formacao@getedu.com.br"


      var email = GmailApp.createDraft(userEmail, 'Dica semanal GetEdu', emailMsg, {
        // attachments: [file.next()],
        htmlBody: htmlMessage,
        name: senderName,
        replyTo: replyEmail
      });


      var date = new Date();
    
      ss.getRange(i+1,5).setValue('Enviado');
      ss.getRange(i+1,6).setValue(date);
      ss.getRange(i+1,7).setValue(user);
      ss.getRange(i+1,8).setValue(fileLink);


      file.addViewer(userEmail);
      email.send();
    }
  }
}
