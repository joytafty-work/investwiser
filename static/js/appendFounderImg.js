(function($) {
    $.fn.appendFounderImg(data) {
    var container = document.getElementById('people-info');
    alert("appendFounderImg was called with results " + data);
    $('#people-info').prepend('<img alt="" src="https://s3.amazonaws.com/photos.angel.co/startups/i/32217-9cef1dc3721cc42fcad1871cb99ef109-medium_jpg.jpg?buster=1326842472">');
})(jQuery);