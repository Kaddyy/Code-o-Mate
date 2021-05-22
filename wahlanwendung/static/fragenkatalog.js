function checkTonio(){
    alert('Ich bin Tonio');
    checkAnswer3 = antworten.antwort3;

    if (element.innerText !=  null){
        element.innerText = 'Tonio';
        alert('Ich bin die Funktion');
        document.getElementById('optAnswer3').style.display = "none";
    } else {
        element.innerText = 'Kaddy';
    }
}