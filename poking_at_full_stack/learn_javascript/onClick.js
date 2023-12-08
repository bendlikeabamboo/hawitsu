function buttonAlert() {
    alert("You have clicked the function");
    alert("This is another effect of clicking the button");
    alert(Date());
}

function changeText() {
    document.getElementById("header-id-001").innerHTML = "It did";

}

function changeBackground() {
    document.getElementById("header-id-002").innerHTML = "Yes you did!";
    document.getElementById("button-id-001").style.backgroundColor = "green";
}

function changeDivOne() {
    document.getElementById("divOne").style.backgroundColor = "orange";
}

function changeDivTwo() {
    document.getElementById("divTwo").style.backgroundColor = "orange";
}

function changeDivTwoBack() {
    document.getElementById("divTwo").style.backgroundColor = "yellow";
}