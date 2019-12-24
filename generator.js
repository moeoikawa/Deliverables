function searchMail() {
 
  var query = 'subject:(案件２)'; //メールのタイトルを入力
  var threads = GmailApp.search(query, 0, 30);
  //スレッドからメールを取得する
  var myMsgs = GmailApp.getMessagesForThreads(threads)[0]; 　
  
  var sign = RegExp('.*?' + ':');
  var sign2 = RegExp('.*?' + '：');
  var sign3 = RegExp('.*?' + '】');
  var sign4 = RegExp('.*?' + '＞');
  
  var init = "Initial Value";
  var word = "NONE HIT WORD"
  
  
  //案件(1)
  for(var i = 0;i < myMsgs.length;i++){
    var body = myMsgs[i].getBody();
    Logger.log(body);
    
    var regexp_1 = RegExp('案件名' + '.*?' + '<br>');
//    var regexp_2 = RegExp('案件' + '.*?' + '<br>');

    var item = init;
    var result1 = word;
  
    if (body.match(regexp_1)){
      var item = body.match(regexp_1)[0].replace('案件名', '').replace('<br>', '');
    }else{
      Logger.log("ヒットする言葉がありせん");
    }
    
    if (item.match(sign) || item.match(sign2) || item.match(sign3) || item.match(sign4)){
      var item = item.substring(item.indexOf(":")).replace(':', '');
      var item = item.substring(item.indexOf("：")).replace('：', '');
      var item = item.substring(item.indexOf("】")).replace('】', '');
      var item = item.substring(item.indexOf("＞")).replace('＞', '');
      var result1 = item;
    }
   
  
  //期間(2)
    var regexp2_1 = RegExp('期　間' + '.*?' + '<br>');
    var regexp2_2 = RegExp('期間' + '.*?' + '<br>');
    
    var item2_1 = init;
    var item2_2 = init;
    var result2 = word;
    
    if (body.match(regexp2_1)){
      var item2_1 = body.match(regexp2_1)[0].replace('期　間', '').replace('<br>', '');
    }else if (body.match(regexp2_2)){ 
      var item2_2 = body.match(regexp2_2)[0].replace('期間', '').replace('<br>', '');
    }else{
      Logger.log("ヒットする言葉がありせん");
    }
    
    if (item2_1.match(sign) || item2_1.match(sign2) || item2_1.match(sign3) || item2_1.match(sign4)){
      var item2_1 = item2_1.substring(item2_1.indexOf(":")).replace(':', '');
      var item2_1 = item2_1.substring(item2_1.indexOf("：")).replace('：', '');
      var item2_1 = item2_1.substring(item2_1.indexOf("】")).replace('】', '');
      var item2_1 = item2_1.substring(item2_1.indexOf("＞")).replace('＞', '');
      var result2 = item2_1;
    }else if (item2_2.match(sign) || item2_2.match(sign2) || item2_2.match(sign3) || item2_2.match(sign4)){
       var item2_2 = item2_2.substring(item2_2.indexOf(":")).replace(':', '');
       var item2_2 = item2_2.substring(item2_2.indexOf("：")).replace('：', '');
       var item2_2 = item2_2.substring(item2_2.indexOf("】")).replace('】', '');
       var item2_2 = item2_2.substring(item2_2.indexOf("＞")).replace('＞', '');
       var result2 = item2_2;
      }else{
        Logger.log("ヒットするアイテムがありません");
       }

    
   //単金(3)
     var regexp3_1 = RegExp('単　金' + '.*?' + '<br>');
     var regexp3_2 = RegExp('単金' + '.*?' + '<br>');
     var regexp3_3 = RegExp('単　価' + '.*?' + '<br>');
     var regexp3_4 = RegExp('単価' + '.*?' + '<br>');

     var item3_1 = init;
     var item3_2 = init;
     var item3_3 = init;
     var item3_4 = init;
     var result3 = word;
  
     if (body.match(regexp3_1)){
      var item3_1 = body.match(regexp3_1)[0].replace('単　金', '').replace('<br>', '');
    }else if (body.match(regexp3_2)){
      var item3_2 = body.match(regexp3_2)[0].replace('単金', '').replace('<br>', '');
    }else if (body.match(regexp3_3)){
      var item3_3 = body.match(regexp3_3)[0].replace('単　価', '').replace('<br>', '');
    }else if (body.match(regexp3_4)){
      var item3_4 = body.match(regexp3_4)[0].replace('単価', '').replace('<br>', ''); 
    }else{
      Logger.log("ヒットする言葉がありせん");
    }
    
    if (item3_1.match(sign) || item3_1.match(sign2) || item3_1.match(sign3) || item3_1.match(sign4)){
      var item3_1 = item3_1.substring(item3_1.indexOf(":")).replace(':', '');
      var item3_1 = item3_1.substring(item3_1.indexOf("：")).replace('：', '');
      var item3_1 = item3_1.substring(item3_1.indexOf("】")).replace('】', '');
      var item3_1 = item3_1.substring(item3_1.indexOf("＞")).replace('＞', '');
      var result3 = item3_1
    }else if (item3_2.match(sign) || item3_2.match(sign2) || item3_2.match(sign3) || item3_2.match(sign4)){
      var item3_2 = item3_2.substring(item3_2.indexOf(":")).replace(':', '');
      var item3_2 = item3_2.substring(item3_2.indexOf("：")).replace('：', '');
      var item3_2 = item3_2.substring(item3_2.indexOf("】")).replace('】', '');
      var item3_2 = item3_2.substring(item3_2.indexOf("＞")).replace('＞', '');
      var result3 = item3_2
    }else if (item3_3.match(sign) || item3_3.match(sign2) || item3_3.match(sign3) || item3_3.match(sign4)){
      var item3_3 = item3_3.substring(item3_3.indexOf(":")).replace(':', '');
      var item3_3 = item3_3.substring(item3_3.indexOf("：")).replace('：', '');
      var item3_3 = item3_3.substring(item3_3.indexOf("】")).replace('】', '');
      var item3_3 = item3_3.substring(item3_3.indexOf("＞")).replace('＞', '');
      var result3 = item3_3
    }else if (item3_4.match(sign) || item3_4.match(sign2) || item3_4.match(sign3) || item3_4.match(sign4)){
      var item3_4 = item3_4.substring(item3_4.indexOf(":")).replace(':', '');
      var item3_4 = item3_4.substring(item3_4.indexOf("：")).replace('：', '');
      var item3_4 = item3_4.substring(item3_4.indexOf("】")).replace('】', '');
      var item3_4 = item3_4.substring(item3_4.indexOf("＞")).replace('＞', '');
      var result3 = item3_4
    }else{
      Logger.log("ヒットするアイテムがありません");
    }
    
    
   //場所(4)
     var regexp4_1 = RegExp('場　所' + '.*?' + '<br>');
     var regexp4_2 = RegExp('場所' + '.*?' + '<br>');
    
     var item4_1 = init;
     var item4_2 = init;
     var result4= word;
    
     if (body.match(regexp4_1)){
      var item4_1 = body.match(regexp4_1)[0].replace('場　所', '').replace('<br>', '');
    }else if (body.match(regexp4_2)){
      var item4_2 = body.match(regexp4_2)[0].replace('場所', '').replace('<br>', '');
    }else{
      Logger.log("ヒットする言葉がありせん");
    }
    
    if (item4_1.match(sign) || item4_1.match(sign2) || item4_1.match(sign3) || item4_1.match(sign4)){
      var item4_1 = item4_1.substring(item4_1.indexOf(":")).replace(':', '');
      var item4_1 = item4_1.substring(item4_1.indexOf("：")).replace('：', '');
      var item4_1 = item4_1.substring(item4_1.indexOf("】")).replace('】', '');
      var item4_1 = item4_1.substring(item4_1.indexOf("＞")).replace('＞', '');
      var result4 = item4_1
    }else if (item4_2.match(sign) || item4_2.match(sign2) || item4_2.match(sign3) || item4_2.match(sign4)){
      var item4_2 = item4_2.substring(item4_2.indexOf(":")).replace(':', '');
      var item4_2 = item4_2.substring(item4_2.indexOf("：")).replace('：', '');
      var item4_2 = item4_2.substring(item4_2.indexOf("】")).replace('】', '');
      var item4_2 = item4_2.substring(item4_2.indexOf("＞")).replace('＞', '');
      var result4 = item4_2
    }else{
      Logger.log("ヒットするアイテムがありません");
    }
    

   //人数(5)
     var regexp5_1 = RegExp('人　数' + '.*?' + '<br>');
     var regexp5_2 = RegExp('人数' + '.*?' + '<br>');
    
     var item5_1 = init;
     var item5_2 = init;
     var result5 = word;
    
     if (body.match(regexp5_1)){
      var item5_1 = body.match(regexp5_1)[0].replace('人　数', '').replace('<br>', '');
    }else if (body.match(regexp5_2)){
      var item5_2 = body.match(regexp5_2)[0].replace('人数', '').replace('<br>', '');
    }else{
      Logger.log("ヒットする言葉がありせん");
    }
    
    if (item5_1.match(sign) || item5_1.match(sign2) || item5_1.match(sign3) || item5_1.match(sign4)){
      var item5_1 = item5_1.substring(item5_1.indexOf(":")).replace(':', '');
      var item5_1 = item5_1.substring(item5_1.indexOf("：")).replace('：', '');
      var item5_1 = item5_1.substring(item5_1.indexOf("】")).replace('】', '');
      var item5_1 = item5_1.substring(item5_1.indexOf("＞")).replace('＞', '');
      var result5 = item5_1
    }else if (item5_2.match(sign) || item5_2.match(sign2) || item5_2.match(sign3) || item5_2.match(sign4)){
      var item5_2 = item5_2.substring(item5_2.indexOf(":")).replace(':', '');
      var item5_2 = item5_2.substring(item5_2.indexOf("：")).replace('：', '');
      var item5_2 = item5_2.substring(item5_2.indexOf("】")).replace('】', '');
      var item5_2 = item5_2.substring(item5_2.indexOf("＞")).replace('＞', '');
      var result5 = item5_2
    }else{
      Logger.log("ヒットするアイテムがありません");
    }
    
    
   //面談(6)
     var regexp6_1 = RegExp('面　談' + '.*?' + '<br>');
     var regexp6_2 = RegExp('面談' + '.*?' + '<br>');
    
     var item6_1 = init;
     var item6_2 = init;
     var result6 = word;
    
     if (body.match(regexp6_1)){
      var item6_1 = body.match(regexp6_1)[0].replace('面　談', '').replace('<br>', '');
    }else if (body.match(regexp6_2)){
      var item6_2 = body.match(regexp6_2)[0].replace('面談', '').replace('<br>', '');
    }else{
      Logger.log("ヒットする言葉がありせん");
    }
    
    if (item6_1.match(sign) || item6_1.match(sign2) || item6_1.match(sign3) || item6_1.match(sign4)){
      var item6_1 = item6_1.substring(item6_1.indexOf(":")).replace(':', '');
      var item6_1 = item6_1.substring(item6_1.indexOf("：")).replace('：', '');
      var item6_1 = item6_1.substring(item6_1.indexOf("】")).replace('】', '');
      var item6_1 = item6_1.substring(item6_1.indexOf("＞")).replace('＞', '');
      var result6 = item6_1
    }else if (item6_2.match(sign) || item6_2.match(sign2) || item6_2.match(sign3) || item6_2.match(sign4)){
      var item6_2 = item6_2.substring(item6_2.indexOf(":")).replace(':', '');
      var item6_2 = item6_2.substring(item6_2.indexOf("：")).replace('：', '');
      var item6_2 = item6_2.substring(item6_2.indexOf("】")).replace('】', '');
      var item6_2 = item6_2.substring(item6_2.indexOf("＞")).replace('＞', '');
      var result6 = item6_2
    }else{
      Logger.log("ヒットするアイテムがありません");
    }    


   //勤務時間(7)
     var regexp7_1 = RegExp('勤務時間' + '.*?' + '<br>');
     var regexp7_2 = RegExp('時間' + '.*?' + '<br>');
    
     var item7_1 = init;
     var item7_2 = init;
     var result7 = word;
    
     if (body.match(regexp7_1)){
      var item7_1 = body.match(regexp7_1)[0].replace('勤務時間', '').replace('<br>', '');
    }else if (body.match(regexp7_2)){
      var item7_2 = body.match(regexp7_2)[0].replace('時間', '').replace('<br>', '');
    }else{
      Logger.log("ヒットする言葉がありせん");
    }
    

    if (item7_1.match(sign) || item7_1.match(sign2) || item7_1.match(sign3) || item7_1.match(sign4)){
      var item7_1 = item7_1.substring(item7_1.indexOf(":")).replace(':', '');
      var item7_1 = item7_1.substring(item7_1.indexOf("：")).replace('：', '');
      var item7_1 = item7_1.substring(item7_1.indexOf("】")).replace('】', '');
      var item7_1 = item7_1.substring(item7_1.indexOf("＞")).replace('＞', '');
      var result7 = item7_1
    }
    
    
   items = [":", "：", "】", "＞"]
    
    
    if (item7_2.match(sign) || item7_2.match(sign2) || item7_2.match(sign3) || item7_2.match(sign4)){
      for(var i = 0;i < item7_2.length;i++){    
        if (item7_2.substring(item7_2.indexOf(":"))){
          var item7_2 = item7_2.replace(":", '');
          continue;
        }else if (item7_2.substring(item7_2.indexOf("："))){
          var item7_2 = item7_2.replace("：", '');
          continue;
        }else if (item7_2.substring(item7_2.indexOf("】"))){
          var item7_2 = item7_2.replace("】", "");
          continue;
        }else if (item7_2.substring(item7_2.indexOf("＞"))){
          var item7_2 = item7_2.replace("＞", "");
          continue;
        }else{
          Logger.log("ヒットするアイテムがありません");
        }  
      }
    }
    
    Logger.log(item7_2);
    
      
      
//      var item7_2 = item7_2.substring(item7_2.indexOf(":")).replace(':', '');
//      var item7_2 = item7_2.substring(item7_2.indexOf("：")).replace('：', '');
//      var item7_2 = item7_2.substring(item7_2.indexOf("】")).replace('】', '');
//      var item7_2 = item7_2.substring(item7_2.indexOf("＞")).replace('＞', '');
//      var result7 = item7_2
//      Logger.log(result7);
//    }else{
//      Logger.log("ヒットするアイテムがありません");
//    } 








    
  }
       
   
  /* スプレッドシートに出力 */
  
  if (result1 == word){
    Logger.log("文中に「案件」という言葉がありません");
  }else{
  SpreadsheetApp.getActiveSheet().getRange("A1").setValue("案件");
  SpreadsheetApp.getActiveSheet().getRange("B1").setValue(":" + result1.trim());
  }
  
  SpreadsheetApp.getActiveSheet().getRange("A2").setValue("内容");

  SpreadsheetApp.getActiveSheet().getRange("A3").setValue("スキル");
  
  if (result2 == word){
    Logger.log("文中に「期間」という言葉がありません");
  }else{
  SpreadsheetApp.getActiveSheet().getRange("A4").setValue("期間");
  SpreadsheetApp.getActiveSheet().getRange("B4").setValue(":" + result2.trim());
  }
  
  if (result3 == word){
    Logger.log("文中に「単金」という言葉がありません");
  }else{
  SpreadsheetApp.getActiveSheet().getRange("A5").setValue("単金");
  SpreadsheetApp.getActiveSheet().getRange("B5").setValue(":" + result3.trim());
  }
  
  if (result4 == word){
    Logger.log("文中に「場所」という言葉がありません");
  }else{
  SpreadsheetApp.getActiveSheet().getRange("A6").setValue("場所");
  SpreadsheetApp.getActiveSheet().getRange("B6").setValue(":" + result4.trim());
  }
  
  if (result5 == word){
    Logger.log("文中に「人数」という言葉がありません");
  }else{
  SpreadsheetApp.getActiveSheet().getRange("A7").setValue("人数");
  SpreadsheetApp.getActiveSheet().getRange("B7").setValue(":" + result5.trim());
  }
  
  if (result6 == word){
    Logger.log("文中に「面談」という言葉がありません");
  }else{
  SpreadsheetApp.getActiveSheet().getRange("A8").setValue("面談");
  SpreadsheetApp.getActiveSheet().getRange("B8").setValue(":" + result6.trim());
  }
  
  if (result7 == word){
    Logger.log("文中に「勤務時間」という言葉がありません");
  }else{
  SpreadsheetApp.getActiveSheet().getRange("A9").setValue("勤務時間");
  SpreadsheetApp.getActiveSheet().getRange("B9").setValue(":" + item7_2.trim());
  }  
  
  SpreadsheetApp.getActiveSheet().getRange("B9").setValue(":" + item7_2.trim());
  
  
  
  
  
  
  
  
  
  
}
  

