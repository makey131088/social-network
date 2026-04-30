let xhr = new XMLHttpRequest();

xhr.open("POST", "http://localhost:5000/api/v1/handler");
xhr.send();

console.log(xhr.responseText);