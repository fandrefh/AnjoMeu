jQuery(function($){
	$("#id_cpf").mask("999.999.999-99");
	$("#id_birthday").mask("99/99/9999");
	$("#id_code_postal").mask("99.999-999");
	$("#id_phone_number").mask("(99)?9999-9999");
	$("#id_goal").maskMoney({thousands: '.', decimal: ','});
	$("#id_donations").maskMoney({thousands: ',', decimal: '.'});
});