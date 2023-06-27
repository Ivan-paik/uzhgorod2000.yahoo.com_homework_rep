// create elements

// friends counter
let friendCount = Math.floor(Math.random() * 20);
let myFriend = document.createTextNode("Друзів: " + friendCount);

document.getElementById("friend-div").appendChild(myFriend);

// add to friends, message, work buttons
const myButon = document.createElement("div");
myButon.idName = "buttons";
myButon.style.textAlign = "right";

btnNames = ["Додати в друзі", "Написати повідомлення", "Запропонувати роботу"];
btnNames.map(buttonName => {
    let button = document.createElement("button");
    button.className = "btn";
    button.innerText = buttonName;
    button.style.marginLeft = "15px";
    button.style.fontSize = "20px";
    myButon.appendChild(button);
})

document.getElementById("button-div").appendChild(myButon);

// add tasks buttons
const myButonTask = document.createElement("div");
myButonTask.idName = "buttons";
myButonTask.style.textAlign = "center";

btnNames = ["Додати завдання (JS)", "Додати завдання (JQuery)"];
btnNames.map(buttonName => {
    let button = document.createElement("button");
    button.className = "btnTask";
    button.innerText = buttonName;
    button.style.marginLeft = "15px";
    button.style.fontSize = "20px";
    myButonTask.appendChild(button);
})

document.getElementById("task-div").appendChild(myButonTask);


// events

// add to friends button listener
const btn0 = document.getElementsByTagName("button")[0];
btn0.addEventListener("click", (myButtonEvent) => {
    let element = document.getElementById("friend-div"); //can't make reload ((
    while (element.firstChild) {
        element.removeChild(element.firstChild);
    }

    ++friendCount;

    myFriend = document.createTextNode("Друзів: " + friendCount);
    document.getElementById("friend-div").appendChild(myFriend);

    myButtonEvent.target.innerText = "Очікується підтвердження";
    myButtonEvent.target.disabled = true;
});

// message button listener
document.getElementsByTagName("button")[1].addEventListener('click', (event) => {
    if (event.target.style.background === "" ) {
        event.target.style.background = "red";
    } else {
        event.target.style.background = "";
    }
})

// work button listener
const btn2 = document.getElementsByTagName("button")[2];
btn2.onclick = () => {
    if (btn0.style.display === "none") {
        btn0.style.display = "";
    } else {
        btn0.style.display = "none";
    }
}

//click event listener without variables
//JS function to add a row to the end of the table
document.getElementsByClassName("btnTask")[0].addEventListener('click', (event) => {
   addRow("result-table");
})

//JQ function to add a row to the end of the table
document.getElementsByClassName("btnTask")[1].addEventListener('click', (event) => {
   $('#result-table').append('<tr><td>№29</td><td style="text-align:left">«Створення веб-сторінки за допомогою JS»</td><td>- / -</td></tr>');
})

//own JS function to add a row to the end of the table
function addRow(tableID) {
  // Get a reference to the table
  let tableRef = document.getElementById(tableID);

  // Insert a row at the end of the table
  let newRow = tableRef.insertRow(-1);

  // Insert a cell in the row at index 0
  let newCell = newRow.insertCell(0);
  let newCell2 = newRow.insertCell(1);
  let newCell3 = newRow.insertCell(2);

  // Append a text node to the cell
  let newText = document.createTextNode("№28");
  let newText2 = document.createTextNode("«Базовий JS»");
  let newText3 = document.createTextNode("- / -");

  newCell2.style.textAlign = "left";

  newCell.appendChild(newText);
  newCell2.appendChild(newText2);
  newCell3.appendChild(newText3);
}
