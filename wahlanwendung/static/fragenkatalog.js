var counter = 0;

function neueFrage() {
    fragentext = "ich will FRAGEN!";
    antworttext1 = "ich bin anw1";
    antworttext2 = "ich bin anw2";
    antworttext3 = "ich bin anw3";
    antworttext4 = "ich bin anw4";
    counter++;

    document.querySelector('#frageNormal').innerText = fragentext  + counter;
    document.querySelector('#label_01').innerText = antworttext1 + counter;
    document.querySelector('#label_02').innerText = antworttext2 + counter;
    document.querySelector('#label_03').innerText = antworttext3 + counter;
    document.querySelector('#label_04').innerText = antworttext4 + counter;
}
