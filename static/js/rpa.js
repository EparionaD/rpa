let contador = 0;
let boton = document.getElementById('clicMenu');

function agregarColor(){
    contador += 1;
    if(window.innerWidth <= 991){
        if(contador % 2 == 0){
            let addColor = document.getElementById('navigation');
            addColor.classList.remove("menu--color","menu--des")
            addColor.classList.toggle("menu--tra")
            setTimeout(() => {
                addColor.classList.remove("menu--tra");
            }, 500);
            agregarActive()
        }
        else{
            let addColor = document.getElementById('navigation');
            addColor.classList.add("menu--color","menu--des")
            quitarActive()
        }
    }
}

function agregarActive(){
    let efecto = document.getElementsByClassName("menu__item");
    for (let i = 0; i < efecto.length; i++) {
        efecto[i].classList.add('menu__item--color')
        if(efecto[i].classList.contains('active')){
            efecto[i].classList.add('active--color')
        }
    }
}
function quitarActive(){
    let efecto = document.getElementsByClassName("menu__item");
    for (let i = 0; i < efecto.length; i++) {
        efecto[i].classList.remove('menu__item--color')
        if(efecto[i].classList.contains('active')){
            efecto[i].classList.remove('active--color')
        }
    }
}
function agregarsocialColor(){
    let color = document.getElementsByClassName("social__link--desktop");
    for (let i = 0; i < color.length; i++) {
        color[i].classList.add('social__link--color')
    }
}
function quitarsocialColor(){
    let color = document.getElementsByClassName("social__link--desktop");
    for (let i = 0; i < color.length; i++) {
        color[i].classList.remove('social__link--color')
    }
}
function disminuirTamano(){
    let addTamano = document.getElementById('imgLogo')
    let link = document.getElementById('linkLogo')
    addTamano.classList.add("menu__logo--tamano","animate__animated","animate__zoomIn")
    link.classList.add('menu__link--tamano')
}
function quitarTamano(){
    let addTamano = document.getElementById('imgLogo')
    let link = document.getElementById('linkLogo')
    addTamano.classList.remove("menu__logo--tamano","animate__animated","animate__zoomIn")
    link.classList.remove('menu__link--tamano')
}

window.onscroll = function(){
    let scroll = document.documentElement.scrollTop || document.body.scrollTop

    if(scroll > 50){
        boton.removeAttribute('onclick','agregarColor()')
        document.getElementById("navigation").classList.add('menu--color','menu--des');

        quitarActive()
        agregarsocialColor()
        disminuirTamano()

    }else{
        boton.setAttribute('onclick','agregarColor()')
        document.getElementById("navigation").classList.remove('menu--color','menu--des');
        document.getElementById("navigation").classList.add('menu--tra');
        setTimeout(() => {
            document.getElementById("navigation").classList.remove('menu--tra');
        }, 100);

        agregarActive()
        quitarsocialColor()
        quitarTamano()
    }
}

function agregarAlerta(elemento1){
    let alerta = document.getElementById(elemento1)
    alerta.classList.add('animate__fadeInUp')
    alerta.classList.remove('d-none')
}
function quitarAlerta(elemento1){
    let alerta = document.getElementById(elemento1)
    alerta.classList.remove('animate__fadeInUp')
    alerta.classList.add('d-none')
}
function agregarAlertaUp(){
    let alerta = document.getElementById('alertaup')
    alerta.classList.add('animate__fadeInUp')
    alerta.classList.remove('d-none')
}
function quitarAlertaUp(){
    let alerta = document.getElementById('alertaup')
    alerta.classList.remove('animate__fadeInUp')
    alerta.classList.add('d-none')
}

function getLink(elemento){
    let campo = document.createElement('input')
    campo.setAttribute('value', window.location.href)

    document.body.appendChild(campo)
    campo.select()
    document.execCommand('copy')
    document.body.removeChild(campo)
    
    agregarAlerta(elemento)
    setTimeout(quitarAlerta,2000,elemento)
}

function getLinkUp(){
    let campo = document.createElement('input')
    campo.setAttribute('value', window.location.href)

    document.body.appendChild(campo)
    campo.select()
    document.execCommand('copy')
    document.body.removeChild(campo)
    
    agregarAlertaUp()
    setTimeout(quitarAlertaUp,2000)
}


function Links(elemento, elemento1){
    let valor = document.getElementById(elemento).getAttribute('campo')

    let valorLink = document.createElement('input')
    valorLink.setAttribute('value', valor)
    document.body.appendChild(valorLink)
    valorLink.select()
    document.execCommand('copy')
    document.body.removeChild(valorLink)

    agregarAlerta(elemento1)
    setTimeout(quitarAlerta,2000,elemento1)
}