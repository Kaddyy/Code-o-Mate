var counter = 0;

function neueFrage() {
    text = "ich will FRAGEN!";
    counter++;
    var jetzt = text + counter;
    document.querySelector('#frageNormal').innerText = jetzt;
}

/*fragentext = "Frage2";

var updateFrage = function(fragentext) {
    document.querySelector('#frageNormal').innerText += fragentext;
}

updateFrage(fragentext);
*/
