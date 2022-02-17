$( document ).ready(function() {

    AOS.init();
   
    // Sort by functionality
    $('#sort-selector').change(function() {
        var selector = $(this);
        var currentUrl = new URL(window.location);

        var selectedVal = selector.val();
        if(selectedVal != 'reset') {
            var sort = selectedVal.split("_")[0]
            console.log(sort)
            var direction = selectedVal.split("_")[1];

            currentUrl.searchParams.set('sort', sort);
            currentUrl.searchParams.set('direction', direction);

            window.location.replace(currentUrl);
        } else {
            currentUrl.searchParams.delete('sort');
            currentUrl.searchParams.delete('direction');

            window.location.replace(currentUrl);
        }
    });

    // Takes user to top of page
    $('.to-top-link').click(function(e) {
        window.scrollTo(0,0)
    });

    // Toggle About section buttons
    $('.about-link button').click(function() {
        $('.about-link .link-active').removeClass('link-active');
        $(this).addClass('link-active');
    });

    // Toggles statement section
    $('#statementButton').click(function() {
        $('#statements').removeClass('d-none');
        $('#policies').addClass('d-none');
        $('#about').addClass('d-none');
        $('.statement-box').addClass('animated fadeInDown');
    });

    // Toggles policy section
    $('#policyButton').click(function() {
        $('#policies').removeClass('d-none').addClass('animated fadeInDown');
        $('#statements').addClass('d-none');
        $('#about').addClass('d-none');
    });

    // Takes user back to About section
    $('.back-to-about').click(function() {
        $('#policies').addClass('d-none');
        $('#statements').addClass('d-none');
        $('#about').removeClass('d-none');
        $('.about-link .link-active').removeClass('link-active');
    });

    // Toggle matching statement text for overlay
    $('.toggle-statement').click(function() {
        var toggle = $(this).attr('id').split('toggle')[1];
        var attributes = $('.overlay-wrapper').map(function() {
            return $(this).attr('id').split('statement')[1];
            }).get();

        for (let i = 0; i < attributes.length; i++) {
            if (attributes[i] == toggle) {
                var statement = attributes.find(element => element == toggle);
            }  
        }

        var statementId = `statement${statement}`;
        if (toggle == statement) {
            $(`#${statementId}`).removeClass('d-none').addClass('animated slideInUp displayed');
        }

    });

    // Takes user back to statements
    $('.back-to-statements').click(function() {
        $('.displayed').addClass('d-none').removeClass('animated slideInUp displayed');
    });

    // Triggers Boostrap tool tips
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
    return new bootstrap.Tooltip(tooltipTriggerEl)
    });

    // Changes countryfield colour
    let countrySelected = $('#id_default_country').val();
      if (!countrySelected) {
          $('#id_default_country').css('color', '#989999');
      };
      $('#id_default_country').change(function() {
        countrySelected = $(this).val();
        if(!countrySelected) {
            $(this).css('color', '#989999');
        } else {
            $(this).css('color', '#313232');
        }
      });

    // Toggles review to full width
    $('#review-1').click(function() {
        $(this).toggleClass('text-truncate');
        $(this).toggleClass('scroll');
    });

    $('#review-2').click(function() {
        $(this).toggleClass('text-truncate');
        $(this).toggleClass('scroll');
    });

    $('#review-3').click(function() {
        $(this).toggleClass('text-truncate');
        $(this).toggleClass('scroll');
    });

});