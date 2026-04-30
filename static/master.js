// Создаем кнопку
let btn = document.createElement('button');
// модифицируем элемент
btn.innerText = "Загрузить новости";
btn.classList.add("btn", "btn-primary");
// Получаем элемент
let root = document.querySelector("#root");
// Добавляем кнопку в точку монтирования
root.append(btn);
// Добавить обработчик
btn.addEventListener("click", async event => {
    let response = await fetch("/api/v1/news");
    let data = await response.json();
    let content = data.map(row => `<tr>
        <td>${row.title}</td>
        <td>${row.text}</td>
        <td>${row.author}</td>
        <td>${row.date}</td>
        </tr>`);
    root.insertAdjacentHTML('beforeend', `
        <table>
        <thead>
        <tr>
        <th>title</th>
        <th>text</th>
        <th>author</th>
        <th>date</th>
        </tr>
        </thead>
        <tbody>
        ${content.join("")}
        </tbody>
        </table>
        `)
});
