/*
gsap.set("KachelHintergrundID");

document.getElementById("testID").addEventListener("click", function() {
    gsap.to("KachelHintergrundID", {
        fill: red,
        overwrite: true,
        duration: 1
    });
    });
*/


    if (document.querySelector('#testID').clicked == true){
    document.querySelector("#SprachenContainer").hidden = true;
    } else{
    document.querySelector("#aktSpracheContainer").hidden = true;
    }