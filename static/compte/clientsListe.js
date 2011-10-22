$(function() {
        $("#id_user").autocomplete("/compte/liste/", {
                max: 0,
                minChars: 2,
                width: "184px"});
});
