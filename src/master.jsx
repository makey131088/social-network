import { createRoot } from "react-dom/client";
import { createElement } from "react";

let rootElement = document.getElementById("root");
let rootComponent = createRoot(rootElement);
rootComponent.render(
    createElement("h1", {}, "Hello world")
);
























// let form = document.querySelector("form");
// form.addEventListener("send", e => {
//     e.preventDefault();
//     let loginField = document.getElementById("login");
//     let passwordField = document.getElementById("password");

//     let login = loginField.value;
//     let password = passwordField.value;

//     let valid = true;
//     // тут валидация



//     if(valid) {
//         fetch("/api/v1/handler", {
//             method: "POST",
//             body: JSON.stringify({
//                 login, password
//             }),
//             headers: {
//                 "Content-Type": "application/json"
//             }
//         }).then(response => {
//             return response.text();
//         }).then(data => alert(data));
//     }
// })