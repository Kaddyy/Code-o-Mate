//Radio Buttons nicht anzeigen, wenn nicht gebraucht
   radio3Inhalt = document.querySelector("#label_03").innerText;
    if (radio3Inhalt == "None") {
    document.querySelector("#label_03").hidden = true;
    document.querySelector("#IDa03").hidden = true;
    document.querySelector("#li_03").hidden = true;
    }

    radio4Inhalt = document.querySelector("#label_04").innerText;
    if (radio4Inhalt == "None") {
    document.querySelector("#label_04").hidden = true;
    document.querySelector("#IDa04").hidden = true;
    document.querySelector("#li_04").hidden = true;
    }

    letzteFrage = document.querySelector("#frage").innerText;
    if (letzteFrage != "Hast du Interesse an der Roboterprogrammierung?"){
    document.querySelector("#auswertungsBtnID").className = "hiddenBtn";
    } else{
    document.querySelector("#weiterBtnID").className = "hiddenBtn";
    }

