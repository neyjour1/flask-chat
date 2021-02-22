var socket = io();

let messages = [];

let lastScrolledIndex;
let currentScrolledIndex;


chatarea = document.getElementById("area");

socket.on('connect', () => {
  socket.emit('msg', "hola amigo:3")
});

socket.on('firstmessage', data => {
  console.log("recibi firstmessage");
  messages = data;
  totalMessageUpdate();
});

socket.on('chatmessage', data => {
  messages.push(data);
  partialMessageUpdate(data);
});

async function get_name(){
  return fetch('/get_name')
    .then(response => response.json())
    .then(data => data.name)
    .catch(error => {
      console.log("Error: " + error);
      window.location.href = "/";
    });
}

async function totalMessageUpdate(){
  chatarea.innerHTML = "";
  for(let index in messages){
    let name = await get_name();
    console.log(name);
    mensaje = messages[index];
    let content = mensaje.name === name ? '<div class="container"><div class="clientmessage"' +
      '<p><h5 style="color:#888">' +
      mensaje.name + "<span class='float-right'>" + formatDate(new Date(mensaje.UTCdate)) +
      "</span>" +
      "</h5></p><p class='text-break'>" + " " +
      mensaje.message +
      '</p></div></div>' : '<div class="container"><div class="servermessage"' +
        '<p><h5 class="text-right" style="color:#888">' +
        mensaje.name + "<span class='float-left'>" + formatDate(new Date(mensaje.UTCdate)) +
        "</span>" +
        "</h5></p>" + '<p class="text-right text-break">' + " " +
        mensaje.message +
        "</p></div></div>";
      // console.log(content);
      chatarea.innerHTML += content;
  }
  refreshMessagesRender();
}



async function partialMessageUpdate(mensaje){
  let name = await get_name();
  console.log(name);
  let content = mensaje.name === name ? '<div class="container"><div class="clientmessage"' +
    '<p><h5 style="color:#888">' +
    mensaje.name + "<span class='float-right'>" + formatDate(new Date(mensaje.UTCdate)) +
    "</span>" +
    "</h5></p><p class='text-break'>" + " " +
    mensaje.message +
    '</p></div></div>' : '<div class="container"><div class="servermessage"' +
      '<p><h5 class="text-right" style="color:#888">' +
      mensaje.name + "<span class='float-left'>" + formatDate(new Date(mensaje.UTCdate)) +
      "</span>" +
      "</h5></p>" + '<p class="text-right text-break">' + " " +
      mensaje.message +
      "</p></div></div>";
    chatarea.innerHTML += content;
  refreshMessagesRender();
}

function refreshMessagesRender(){

  let sh = chatarea.scrollHeight;
  let ch = chatarea.clientHeight;
  currentScrolledIndex = messages[messages.length-1];
  $("#area").animate({scrollTop: sh-ch}, 0);
}

document.getElementById("txtMessage").addEventListener('keydown', e => {
  if(e.keyCode == 13){ // enter
    sendMessage(e.target);
  }
});

document.getElementById("btnSend").addEventListener("click", () => {
  sendMessage(document.getElementById("txtMessage"));
});

function sendMessage(target){
  socket.emit('chatmessage', {"message": target.value, "UTCdate": getUTCTimeString()});
  target.value = "";
}

function formatDate(date){
  return date.toISOString().slice(0, 19).replace(/-/g, "/").replace("T", " ");
}

function getUTCTimeString(){
  return new Date().toUTCString();
}

let c = () => {
  socket.emit('clear', "");
  console.log('sendie clear');
}
