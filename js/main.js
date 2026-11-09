/*=========================================================
    Diritti al Lavoro
    main.js - apre e chiude l'indice su schermi piccoli
=========================================================*/

const bottoneIndice = document.getElementById("bottoneIndice");
const indice = document.getElementById("indice");

if(bottoneIndice && indice){

    bottoneIndice.addEventListener("click", () => {

        const aperto = indice.classList.toggle("aperto");

        bottoneIndice.setAttribute("aria-expanded", aperto ? "true" : "false");

    });

}
