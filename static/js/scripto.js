const btn_close = document.querySelector('#close')
const cont_cookies = document.querySelector('.cookies-box')
const modal = document.querySelector('.modal')
const ver_p = document.querySelector('#ver_pol')

const c_modal = document.querySelector('#close_modal')

const ac_cookie = document.querySelector('#aceptar_cookie');
const ac_cookie2 = document.querySelector('#aceptar_modal');


(function comprobarCookies() {
    if (localStorage.cookies1 == 'true') {
        cont_cookies.style.bottom = '-200px'
    }
})()

function aceptarCookies() {
    localStorage.cookies1 = 'true'
    cont_cookies.style.bottom = '-200px'

    let expire = new Date()
    expire = new Date(expire.getTime() + 776000000)
    document.cookies = 'cookies1=aceptada; expire='+expire
}

ac_cookie.addEventListener('click', () => {
    aceptarCookies();
})

ac_cookie2.addEventListener('click', () => {
    aceptarCookies();
    modal.style.visibility = 'hidden'
    modal.style.opacity = '0'
})




btn_close.addEventListener('click', () => {
    cont_cookies.style.bottom = '-200px'
})


ver_p.addEventListener('click', () => {
    modal.style.visibility = 'visible'
    modal.style.opacity = '1'
})

c_modal.addEventListener('click', () => {
    modal.style.visibility = 'hidden'
    modal.style.opacity = '0'
})