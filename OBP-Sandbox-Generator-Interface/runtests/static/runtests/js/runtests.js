$(function() {

	$('.runner button.forGenerate').click(function() {
		country = $('.runner').find('input[name="Country"]').val();
		bank_num = $('.runner').find('input[name="BANK_NUMBER"]').val();
		branch_num = $('.runner').find('input[name="BRANCH_NUMBER"]').val();
		product_num = $('.runner').find('input[name="PRODUCT_NUMBER"]').val();
		atm_num = $('.runner').find('input[name="ATM_NUMBER"]').val();
		months = $('.runner').find('input[name="MONTHS"]').val();
		input_path = $('.runner').find('input[name="INPUT_PATH"]').val();
		output_path = $('.runner').find('input[name="OUTPUT_PATH"]').val();

		//main = $('.runner').find('input[name="main"]').val();
		//counterparty = $('.runner').find('input[name="counterpary"]').val();
		//customer = $('.runner').find('input[name="customer"]').val();
		//alert(input_path)
		$.post('/runtests/generate_file', {
			'country': country,
			'bank_num': bank_num,
			'branch_num' : branch_num,
			'product_num': product_num,
			'atm_num': atm_num,
			'months':months,
			'input_path':input_path,
			'output_path': output_path,
			'csrfmiddlewaretoken': window.CSRF
		}, function (response) {
			alert("Generation Successfully");
		});
	});

	$('.runner #main_file').click(function () {
		api_host = $('.runner').find('input[name="api_host"]').val();
		consumer_key = $('.runner').find('input[name="consumer_key"]').val();
		username = $('.runner').find('input[name="username"]').val();
		password = $('.runner').find('input[name="password"]').val();
		output_file = $('.runner').find('input[name="output_path"]').val();

		$.post('/runtests/import_json', {
			'api_host': api_host,
			'consumer_key': consumer_key,
			'username': username,
			'password': password,
			'output_file': output_file,
			'csrfmiddlewaretoken': window.CSRF
		}, function (response) {
			alert("Update Successfully");
		});
	});

	$('#counterparty').click(function () {
		api_host = $('.runner').find('input[name="api_host"]').val();
		consumer_key = $('.runner').find('input[name="consumer_key"]').val();
		username = $('.runner').find('input[name="username"]').val();
		password = $('.runner').find('input[name="password"]').val();
		output_file = $('.runner').find('input[name="output_path"]').val();

		$.post('/runtests/import_counterparty', {
			'api_host': api_host,
			'consumer_key': consumer_key,
			'username': username,
			'password': password,
			'output_file': output_file,
			'csrfmiddlewaretoken': window.CSRF
		}, function (response) {
			alert("Update Successfully");
		});
	});

	$('#customer').click(function () {
		api_host = $('.runner').find('input[name="api_host"]').val();
		consumer_key = $('.runner').find('input[name="consumer_key"]').val();
		username = $('.runner').find('input[name="username"]').val();
		password = $('.runner').find('input[name="password"]').val();
		output_file = $('.runner').find('input[name="output_path"]').val();

		$.post('/runtests/import_customer', {
			'api_host': api_host,
			'consumer_key': consumer_key,
			'username': username,
			'password': password,
			'output_file': output_file,
			'csrfmiddlewaretoken': window.CSRF
		}, function (response) {
			alert("Update Successfully");
		});
	});
});
