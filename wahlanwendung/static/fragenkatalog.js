    whatauchimmer = document.querySelector("#label_03").innerText;
    if (whatauchimmer == "None") {
    document.querySelector("#label_03").hidden = true;
    document.querySelector("#a01_3").hidden = true;
    }
    whatauchimmer2 = document.querySelector("#label_04").innerText;
    if (whatauchimmer2 == "None") {
    document.querySelector("#label_04").hidden = true;
    document.querySelector("#a01_4").hidden = true;
    }
    letzteFrage = document.querySelector("#frage").innerText;
    if (letzteFrage != "Hast du Interesse daran Roboter zu programmieren?"){
    document.querySelector("#auswertung").hidden = true;
    } else{
    document.querySelector("#weiterbtn").hidden = true;
    }

/*function checkTonio(){
    //checkAnswer3 = antworten.antwort3;
    document.querySelector("#label_03").innerText = element;
    if (element == "Ulla"){
        document.querySelector("#label_03").innerText = 'Tonio';
        //document.getElementById('optAnswer3').style.display = "none";
    } else {
        document.querySelector("#label_03").innerText = "Kaddy";
    }
}*/