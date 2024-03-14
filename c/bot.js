var child_process = require('child_process');
var TelegramBot = require('node-telegram-bot-api');

var token = '233586141:AAFcDNSxXxGJljkK3mrYa28zwxFykRdstYE';

var bot = new TelegramBot(token, { polling: true });

bot.onText(/^\/start$/, function(msg, match){
  var chatId = msg.chat.id;
  var resp = match[1]; 

  exec('start', chatId, null, function(){
      bot.sendMessage(chatId, "Game Start!");
  });
 
  console.log("start game", chatId);
});

bot.onText(/^[0-9]{4}$/, function(msg, match){
  var chatId = msg.chat.id;
  var num = match[0];
  console.log("%s guess %s", chatId, num);
  exec('guess', chatId, num, function(err, res){
          bot.sendMessage(chatId, res);
  });
});

function exec(cmd, who, parm, cb){
    var execFile = 'c/a.out';
    var data = child_process.spawnSync(execFile, [cmd, who, parm]);
    cb(data.stderr, data.stdout);
}
