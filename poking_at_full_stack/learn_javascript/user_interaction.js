var value = 0;

var counterValue = 0;
function addOne() {
    value += 1;
    document.getElementById('number').innerHTML = value;
}

function counterMinusOne() {
    counterValue -= 1;
    document.getElementById('number2').innerHTML = ('Count: ' + counterValue);
}

function counterAddOne() {
    counterValue += 1;
    document.getElementById('number2').innerHTML = ('Count: ' + counterValue);
}

var rgbArray = [0,0,0]

function minusBgColor() {
    rgbArray[0] += 20;
    document.body.style.backgroundColor = rgb(rgbArray);
}

function plusBgColor() {
    rgbArray[1] += 20;
    document.body.style.backgroundColor = rgb(rgbArray);
}