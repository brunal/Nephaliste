$(function() {
        $("#id_user").autocomplete({
                source: liste,
                minLength: 2,
                width: "184px"});

        function liste(req, callback) {
                $.get("/compte/liste", req.term, function(data) {
                        var result = [];
                        for(x in data) {
                                var user = data[x];
                                result.push({"label": user.username + " (" + user.solde + "€)", "value": user.username});
                        }
                        return callback(result);
                }, "json");
        }
});
