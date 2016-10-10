/**
 * Created by es11400 on 25/9/16.
 */
/* PARA MOSTRAR EL MENU EN MODO MOVIL */
$(".button-collapse").sideNav();
/* SMOOTHSCROL Y BOTON PARA SUBIR CON EFECTO FADE AL BAJAR */
$(window).scroll(function(){
	if ($(this).scrollTop() > 100) {
		$('.subir').fadeIn();
	} else {
		$('.subir').fadeOut();
	}
});

$('.subir').click(function(){
	$("html, body").animate({ scrollTop: 0 }, 600);
	return false;
});

/* PARA MOSTRAR EL MODAL DE LOGIN */
$('#Acceso, #Acceso_sidenav, #Acceso_sidenav3').on('click', function(){
	$('.button-collapse').sideNav('hide');
	$('#modalAcceso').openModal();
});

/* PARA MOSTRAR EL MODAL DEL REGISTRO */
$('#Registro, #Registro_sidenav').on('click', function(){
	$('.button-collapse').sideNav('hide');
	$('#modalRegistro').openModal();
});

$('.datepicker').pickadate({
    selectMonths: true, // Creates a dropdown to control month
    selectYears: 15 // Creates a dropdown of 15 years to control year
});

$(document).ready(function() {
    $('select').material_select();
});