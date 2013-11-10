var WeddingForm = (function() {

	function init() {

		var $form = $("#frmRSVP");

		$form.on('change', "input[name=rdoAttending]", function() {
			checkForm();
			
		});

		$("#frmRSVP").submit(function() {
			var $this = $(this);

			$('.error', $this).removeClass('error');

			if (typeof $('input[name=rdoAttending]:checked', '#frmRSVP').val() == 'undefined'){
				$("#rdoAttending").parent().addClass("error");
				return false;
			}

			if ($("#txtNames").val() === '') {
				$("#txtNames").parent().addClass("error");
				return false;
			}

			$.post(
				$this.attr('action'),
				$this.serialize(),
				function() {
					alert('Thanks! Your RSVP has been saved.');
					$this[0].reset();
					checkForm();
				}
			);

			return false;
		});

		checkForm();

	}

	function checkForm() {
		var $form = $("#frmRSVP");

		if ($('input[name=rdoAttending]:checked', '#frmRSVP').val() == 'yes') {
			$("#namesLabel").html('Please enter the full names of attendees:');
		} else {
			$("#namesLabel").html('Please your name:');
		}
	}

	return {
		init: init
	};

}());