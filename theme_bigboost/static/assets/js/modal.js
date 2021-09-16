$( document ).ready(function() {

    $(window).on('load', function() {
        $('#exampleModal').modal('show');
    });

    function openSearch() {
        document.getElementById("search-overlay").style.display = "block";
    }

    function closeSearch() {
        document.getElementById("search-overlay").style.display = "none";
    }

});
