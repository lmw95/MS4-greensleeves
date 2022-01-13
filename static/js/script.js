$( document ).ready(function() {
   
    // Sort by functionality
    $('#sort-selector').change(function() {
        var selector = $(this);
        var currentUrl = new URL(window.location);

        var selectedVal = selector.val();
        if(selectedVal != 'reset') {
            var sort = selectedVal.split("_")[0]
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

    // Toggle about buttons
    $('.about-link button').click(function() {
        console.log('clicked');
        $('.about-link .link-active').removeClass('link-active');
        $(this).addClass('link-active');
    });

    // Triggers Boostrap tool tips
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
    return new bootstrap.Tooltip(tooltipTriggerEl)
    });

});