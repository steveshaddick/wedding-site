var WeddingForm = (function() {

    function init() {

        var $form = $("#frmRSVP");

        $form[0].reset();
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
            $("#namesField").slideDown();
            $("#dietField").slideDown();
            $("#submitRSVP").slideDown();
        } else if ($('input[name=rdoAttending]:checked', '#frmRSVP').val() == 'no') {
            $("#namesLabel").html('Please enter your name:');
            $("#namesField").slideDown();
            $("#dietField").slideUp();
            $("#submitRSVP").slideDown();
        } else {
            $("#namesField").slideUp();
            $("#dietField").slideUp();
            $("#submitRSVP").slideUp();
        }
    }

    return {
        init: init
    };

}());


var WeddingMaps = (function() {

    function init() {
        var mapOptions = {
            center: new google.maps.LatLng(43.643319, -79.421981),
            zoom: 15,
            mapTypeId: google.maps.MapTypeId.ROADMAP
        };
        var map = new google.maps.Map(document.getElementById("mapCanvas"), mapOptions);
        var styles = [
        {
            stylers: [
                { saturation: -50 }
            ]
        },{
            featureType: "road",
            elementType: "geometry",
            stylers: [
                { lightness: 100 },
                { visibility: "simplified" }
            ]
        }
        ];

        map.setOptions({styles: styles});

        var marker = new google.maps.Marker({
            position: new google.maps.LatLng(43.643374, -79.422101),
            map: map,
            title:"The Great Hall",
            icon: '/static/img/heart-small.png'
        });
        var infowindow = new google.maps.InfoWindow({
            content: "<div style=\"width:300px;\"><h4>The Great Hall</h4><img style=\"width:200px;\" src=\"/static/img/great-hall-street.jpg\"><p>1087 Queen St W<br>647 341 5526<br><a href=\"http://www.thegreathall.ca\" target=\"_blank\">thegreathall.ca</a></p></div>"
        });
        google.maps.event.addListener(marker, 'click', function() {
            infowindow.open(map,marker);
        });
    }

    return {
        init: init
    };

}());