$(function() {
        $("#id_user").autocomplete({
                source: "/compte/liste",
                minLength: 2,
                width: "184px"});
});
