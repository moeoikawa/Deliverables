function searchMail() {
 
  var query = 'subject:(�Č��Q)'; //���[���̃^�C�g�������
  var threads = GmailApp.search(query, 0, 30);
  //�X���b�h���烁�[�����擾����
  var myMsgs = GmailApp.getMessagesForThreads(threads)[0]; �@
  
  var sign = RegExp('.*?' + ':');
  var sign2 = RegExp('.*?' + '�F');
  var sign3 = RegExp('.*?' + '�z');
  var sign4 = RegExp('.*?' + '��');
  
  var init = "Initial Value";
  var word = "NONE HIT WORD"
  
  
  //�Č�(1)
  for(var i = 0;i < myMsgs.length;i++){
    var body = myMsgs[i].getBody();
    Logger.log(body);
    
    var regexp_1 = RegExp('�Č���' + '.*?' + '<br>');
//    var regexp_2 = RegExp('�Č�' + '.*?' + '<br>');

    var item = init;
    var result1 = word;
  
    if (body.match(regexp_1)){
      var item = body.match(regexp_1)[0].replace('�Č���', '').replace('<br>', '');
    }else{
      Logger.log("�q�b�g���錾�t�����肹��");
    }
    
    if (item.match(sign) || item.match(sign2) || item.match(sign3) || item.match(sign4)){
      var item = item.substring(item.indexOf(":")).replace(':', '');
      var item = item.substring(item.indexOf("�F")).replace('�F', '');
      var item = item.substring(item.indexOf("�z")).replace('�z', '');
      var item = item.substring(item.indexOf("��")).replace('��', '');
      var result1 = item;
    }
   
  
  //����(2)
    var regexp2_1 = RegExp('���@��' + '.*?' + '<br>');
    var regexp2_2 = RegExp('����' + '.*?' + '<br>');
    
    var item2_1 = init;
    var item2_2 = init;
    var result2 = word;
    
    if (body.match(regexp2_1)){
      var item2_1 = body.match(regexp2_1)[0].replace('���@��', '').replace('<br>', '');
    }else if (body.match(regexp2_2)){ 
      var item2_2 = body.match(regexp2_2)[0].replace('����', '').replace('<br>', '');
    }else{
      Logger.log("�q�b�g���錾�t�����肹��");
    }
    
    if (item2_1.match(sign) || item2_1.match(sign2) || item2_1.match(sign3) || item2_1.match(sign4)){
      var item2_1 = item2_1.substring(item2_1.indexOf(":")).replace(':', '');
      var item2_1 = item2_1.substring(item2_1.indexOf("�F")).replace('�F', '');
      var item2_1 = item2_1.substring(item2_1.indexOf("�z")).replace('�z', '');
      var item2_1 = item2_1.substring(item2_1.indexOf("��")).replace('��', '');
      var result2 = item2_1;
    }else if (item2_2.match(sign) || item2_2.match(sign2) || item2_2.match(sign3) || item2_2.match(sign4)){
       var item2_2 = item2_2.substring(item2_2.indexOf(":")).replace(':', '');
       var item2_2 = item2_2.substring(item2_2.indexOf("�F")).replace('�F', '');
       var item2_2 = item2_2.substring(item2_2.indexOf("�z")).replace('�z', '');
       var item2_2 = item2_2.substring(item2_2.indexOf("��")).replace('��', '');
       var result2 = item2_2;
      }else{
        Logger.log("�q�b�g����A�C�e��������܂���");
       }

    
   //�P��(3)
     var regexp3_1 = RegExp('�P�@��' + '.*?' + '<br>');
     var regexp3_2 = RegExp('�P��' + '.*?' + '<br>');
     var regexp3_3 = RegExp('�P�@��' + '.*?' + '<br>');
     var regexp3_4 = RegExp('�P��' + '.*?' + '<br>');

     var item3_1 = init;
     var item3_2 = init;
     var item3_3 = init;
     var item3_4 = init;
     var result3 = word;
  
     if (body.match(regexp3_1)){
      var item3_1 = body.match(regexp3_1)[0].replace('�P�@��', '').replace('<br>', '');
    }else if (body.match(regexp3_2)){
      var item3_2 = body.match(regexp3_2)[0].replace('�P��', '').replace('<br>', '');
    }else if (body.match(regexp3_3)){
      var item3_3 = body.match(regexp3_3)[0].replace('�P�@��', '').replace('<br>', '');
    }else if (body.match(regexp3_4)){
      var item3_4 = body.match(regexp3_4)[0].replace('�P��', '').replace('<br>', ''); 
    }else{
      Logger.log("�q�b�g���錾�t�����肹��");
    }
    
    if (item3_1.match(sign) || item3_1.match(sign2) || item3_1.match(sign3) || item3_1.match(sign4)){
      var item3_1 = item3_1.substring(item3_1.indexOf(":")).replace(':', '');
      var item3_1 = item3_1.substring(item3_1.indexOf("�F")).replace('�F', '');
      var item3_1 = item3_1.substring(item3_1.indexOf("�z")).replace('�z', '');
      var item3_1 = item3_1.substring(item3_1.indexOf("��")).replace('��', '');
      var result3 = item3_1
    }else if (item3_2.match(sign) || item3_2.match(sign2) || item3_2.match(sign3) || item3_2.match(sign4)){
      var item3_2 = item3_2.substring(item3_2.indexOf(":")).replace(':', '');
      var item3_2 = item3_2.substring(item3_2.indexOf("�F")).replace('�F', '');
      var item3_2 = item3_2.substring(item3_2.indexOf("�z")).replace('�z', '');
      var item3_2 = item3_2.substring(item3_2.indexOf("��")).replace('��', '');
      var result3 = item3_2
    }else if (item3_3.match(sign) || item3_3.match(sign2) || item3_3.match(sign3) || item3_3.match(sign4)){
      var item3_3 = item3_3.substring(item3_3.indexOf(":")).replace(':', '');
      var item3_3 = item3_3.substring(item3_3.indexOf("�F")).replace('�F', '');
      var item3_3 = item3_3.substring(item3_3.indexOf("�z")).replace('�z', '');
      var item3_3 = item3_3.substring(item3_3.indexOf("��")).replace('��', '');
      var result3 = item3_3
    }else if (item3_4.match(sign) || item3_4.match(sign2) || item3_4.match(sign3) || item3_4.match(sign4)){
      var item3_4 = item3_4.substring(item3_4.indexOf(":")).replace(':', '');
      var item3_4 = item3_4.substring(item3_4.indexOf("�F")).replace('�F', '');
      var item3_4 = item3_4.substring(item3_4.indexOf("�z")).replace('�z', '');
      var item3_4 = item3_4.substring(item3_4.indexOf("��")).replace('��', '');
      var result3 = item3_4
    }else{
      Logger.log("�q�b�g����A�C�e��������܂���");
    }
    
    
   //�ꏊ(4)
     var regexp4_1 = RegExp('��@��' + '.*?' + '<br>');
     var regexp4_2 = RegExp('�ꏊ' + '.*?' + '<br>');
    
     var item4_1 = init;
     var item4_2 = init;
     var result4= word;
    
     if (body.match(regexp4_1)){
      var item4_1 = body.match(regexp4_1)[0].replace('��@��', '').replace('<br>', '');
    }else if (body.match(regexp4_2)){
      var item4_2 = body.match(regexp4_2)[0].replace('�ꏊ', '').replace('<br>', '');
    }else{
      Logger.log("�q�b�g���錾�t�����肹��");
    }
    
    if (item4_1.match(sign) || item4_1.match(sign2) || item4_1.match(sign3) || item4_1.match(sign4)){
      var item4_1 = item4_1.substring(item4_1.indexOf(":")).replace(':', '');
      var item4_1 = item4_1.substring(item4_1.indexOf("�F")).replace('�F', '');
      var item4_1 = item4_1.substring(item4_1.indexOf("�z")).replace('�z', '');
      var item4_1 = item4_1.substring(item4_1.indexOf("��")).replace('��', '');
      var result4 = item4_1
    }else if (item4_2.match(sign) || item4_2.match(sign2) || item4_2.match(sign3) || item4_2.match(sign4)){
      var item4_2 = item4_2.substring(item4_2.indexOf(":")).replace(':', '');
      var item4_2 = item4_2.substring(item4_2.indexOf("�F")).replace('�F', '');
      var item4_2 = item4_2.substring(item4_2.indexOf("�z")).replace('�z', '');
      var item4_2 = item4_2.substring(item4_2.indexOf("��")).replace('��', '');
      var result4 = item4_2
    }else{
      Logger.log("�q�b�g����A�C�e��������܂���");
    }
    

   //�l��(5)
     var regexp5_1 = RegExp('�l�@��' + '.*?' + '<br>');
     var regexp5_2 = RegExp('�l��' + '.*?' + '<br>');
    
     var item5_1 = init;
     var item5_2 = init;
     var result5 = word;
    
     if (body.match(regexp5_1)){
      var item5_1 = body.match(regexp5_1)[0].replace('�l�@��', '').replace('<br>', '');
    }else if (body.match(regexp5_2)){
      var item5_2 = body.match(regexp5_2)[0].replace('�l��', '').replace('<br>', '');
    }else{
      Logger.log("�q�b�g���錾�t�����肹��");
    }
    
    if (item5_1.match(sign) || item5_1.match(sign2) || item5_1.match(sign3) || item5_1.match(sign4)){
      var item5_1 = item5_1.substring(item5_1.indexOf(":")).replace(':', '');
      var item5_1 = item5_1.substring(item5_1.indexOf("�F")).replace('�F', '');
      var item5_1 = item5_1.substring(item5_1.indexOf("�z")).replace('�z', '');
      var item5_1 = item5_1.substring(item5_1.indexOf("��")).replace('��', '');
      var result5 = item5_1
    }else if (item5_2.match(sign) || item5_2.match(sign2) || item5_2.match(sign3) || item5_2.match(sign4)){
      var item5_2 = item5_2.substring(item5_2.indexOf(":")).replace(':', '');
      var item5_2 = item5_2.substring(item5_2.indexOf("�F")).replace('�F', '');
      var item5_2 = item5_2.substring(item5_2.indexOf("�z")).replace('�z', '');
      var item5_2 = item5_2.substring(item5_2.indexOf("��")).replace('��', '');
      var result5 = item5_2
    }else{
      Logger.log("�q�b�g����A�C�e��������܂���");
    }
    
    
   //�ʒk(6)
     var regexp6_1 = RegExp('�ʁ@�k' + '.*?' + '<br>');
     var regexp6_2 = RegExp('�ʒk' + '.*?' + '<br>');
    
     var item6_1 = init;
     var item6_2 = init;
     var result6 = word;
    
     if (body.match(regexp6_1)){
      var item6_1 = body.match(regexp6_1)[0].replace('�ʁ@�k', '').replace('<br>', '');
    }else if (body.match(regexp6_2)){
      var item6_2 = body.match(regexp6_2)[0].replace('�ʒk', '').replace('<br>', '');
    }else{
      Logger.log("�q�b�g���錾�t�����肹��");
    }
    
    if (item6_1.match(sign) || item6_1.match(sign2) || item6_1.match(sign3) || item6_1.match(sign4)){
      var item6_1 = item6_1.substring(item6_1.indexOf(":")).replace(':', '');
      var item6_1 = item6_1.substring(item6_1.indexOf("�F")).replace('�F', '');
      var item6_1 = item6_1.substring(item6_1.indexOf("�z")).replace('�z', '');
      var item6_1 = item6_1.substring(item6_1.indexOf("��")).replace('��', '');
      var result6 = item6_1
    }else if (item6_2.match(sign) || item6_2.match(sign2) || item6_2.match(sign3) || item6_2.match(sign4)){
      var item6_2 = item6_2.substring(item6_2.indexOf(":")).replace(':', '');
      var item6_2 = item6_2.substring(item6_2.indexOf("�F")).replace('�F', '');
      var item6_2 = item6_2.substring(item6_2.indexOf("�z")).replace('�z', '');
      var item6_2 = item6_2.substring(item6_2.indexOf("��")).replace('��', '');
      var result6 = item6_2
    }else{
      Logger.log("�q�b�g����A�C�e��������܂���");
    }    


   //�Ζ�����(7)
     var regexp7_1 = RegExp('�Ζ�����' + '.*?' + '<br>');
     var regexp7_2 = RegExp('����' + '.*?' + '<br>');
    
     var item7_1 = init;
     var item7_2 = init;
     var result7 = word;
    
     if (body.match(regexp7_1)){
      var item7_1 = body.match(regexp7_1)[0].replace('�Ζ�����', '').replace('<br>', '');
    }else if (body.match(regexp7_2)){
      var item7_2 = body.match(regexp7_2)[0].replace('����', '').replace('<br>', '');
    }else{
      Logger.log("�q�b�g���錾�t�����肹��");
    }
    

    if (item7_1.match(sign) || item7_1.match(sign2) || item7_1.match(sign3) || item7_1.match(sign4)){
      var item7_1 = item7_1.substring(item7_1.indexOf(":")).replace(':', '');
      var item7_1 = item7_1.substring(item7_1.indexOf("�F")).replace('�F', '');
      var item7_1 = item7_1.substring(item7_1.indexOf("�z")).replace('�z', '');
      var item7_1 = item7_1.substring(item7_1.indexOf("��")).replace('��', '');
      var result7 = item7_1
    }
    
    
   items = [":", "�F", "�z", "��"]
    
    
    if (item7_2.match(sign) || item7_2.match(sign2) || item7_2.match(sign3) || item7_2.match(sign4)){
      for(var i = 0;i < item7_2.length;i++){    
        if (item7_2.substring(item7_2.indexOf(":"))){
          var item7_2 = item7_2.replace(":", '');
          continue;
        }else if (item7_2.substring(item7_2.indexOf("�F"))){
          var item7_2 = item7_2.replace("�F", '');
          continue;
        }else if (item7_2.substring(item7_2.indexOf("�z"))){
          var item7_2 = item7_2.replace("�z", "");
          continue;
        }else if (item7_2.substring(item7_2.indexOf("��"))){
          var item7_2 = item7_2.replace("��", "");
          continue;
        }else{
          Logger.log("�q�b�g����A�C�e��������܂���");
        }  
      }
    }
    
    Logger.log(item7_2);
    
      
      
//      var item7_2 = item7_2.substring(item7_2.indexOf(":")).replace(':', '');
//      var item7_2 = item7_2.substring(item7_2.indexOf("�F")).replace('�F', '');
//      var item7_2 = item7_2.substring(item7_2.indexOf("�z")).replace('�z', '');
//      var item7_2 = item7_2.substring(item7_2.indexOf("��")).replace('��', '');
//      var result7 = item7_2
//      Logger.log(result7);
//    }else{
//      Logger.log("�q�b�g����A�C�e��������܂���");
//    } 








    
  }
       
   
  /* �X�v���b�h�V�[�g�ɏo�� */
  
  if (result1 == word){
    Logger.log("�����Ɂu�Č��v�Ƃ������t������܂���");
  }else{
  SpreadsheetApp.getActiveSheet().getRange("A1").setValue("�Č�");
  SpreadsheetApp.getActiveSheet().getRange("B1").setValue(":" + result1.trim());
  }
  
  SpreadsheetApp.getActiveSheet().getRange("A2").setValue("���e");

  SpreadsheetApp.getActiveSheet().getRange("A3").setValue("�X�L��");
  
  if (result2 == word){
    Logger.log("�����Ɂu���ԁv�Ƃ������t������܂���");
  }else{
  SpreadsheetApp.getActiveSheet().getRange("A4").setValue("����");
  SpreadsheetApp.getActiveSheet().getRange("B4").setValue(":" + result2.trim());
  }
  
  if (result3 == word){
    Logger.log("�����Ɂu�P���v�Ƃ������t������܂���");
  }else{
  SpreadsheetApp.getActiveSheet().getRange("A5").setValue("�P��");
  SpreadsheetApp.getActiveSheet().getRange("B5").setValue(":" + result3.trim());
  }
  
  if (result4 == word){
    Logger.log("�����Ɂu�ꏊ�v�Ƃ������t������܂���");
  }else{
  SpreadsheetApp.getActiveSheet().getRange("A6").setValue("�ꏊ");
  SpreadsheetApp.getActiveSheet().getRange("B6").setValue(":" + result4.trim());
  }
  
  if (result5 == word){
    Logger.log("�����Ɂu�l���v�Ƃ������t������܂���");
  }else{
  SpreadsheetApp.getActiveSheet().getRange("A7").setValue("�l��");
  SpreadsheetApp.getActiveSheet().getRange("B7").setValue(":" + result5.trim());
  }
  
  if (result6 == word){
    Logger.log("�����Ɂu�ʒk�v�Ƃ������t������܂���");
  }else{
  SpreadsheetApp.getActiveSheet().getRange("A8").setValue("�ʒk");
  SpreadsheetApp.getActiveSheet().getRange("B8").setValue(":" + result6.trim());
  }
  
  if (result7 == word){
    Logger.log("�����Ɂu�Ζ����ԁv�Ƃ������t������܂���");
  }else{
  SpreadsheetApp.getActiveSheet().getRange("A9").setValue("�Ζ�����");
  SpreadsheetApp.getActiveSheet().getRange("B9").setValue(":" + item7_2.trim());
  }  
  
  SpreadsheetApp.getActiveSheet().getRange("B9").setValue(":" + item7_2.trim());
  
  
  
  
  
  
  
  
  
  
}
  

